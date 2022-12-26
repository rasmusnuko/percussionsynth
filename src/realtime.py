import threading, sys, tty, time, random
import numpy as np
import pyaudio

DEBUG = True

### AUDIO VARS
SAMPLE_RATE = 44100
CHUNK       = 64
CHANNELS    = 1
FORMAT      = pyaudio.paInt16

class Shaker:
  def __init__(self):
    self.max = 0

    ### SHAKER CONFIG
    ## TODO make config loader

    self.shells  =[{'freq': 5500, 'q': 0.6}]
    self.conf = { 'num beans': 32,
                  'prob': 1 / 16,
                  'system decay': 0.999,
                  'sound decay': 0.96,
                  'shells': self.shells,
                  'zeros': ['both'],
                  'shake time': 30e-3,
                  'filename': 'sekere'}

    ### BANDPASS FILTER VARIABLES
    self.buf = [0, 0]
    self.filters = []
    for filt in self.conf['shells']:
      f  = 2 * np.sin(np.pi * (filt['freq'] / SAMPLE_RATE))
      fb = filt['q'] + (filt['q']/(1-f))
      self.filters.append({'f': f, 'fb': fb})

    ### INIT VARIABLES
    self.shake_energy = 0
    self.sound_level = 0

    ### ONE-ZERO FILTER VARIABLES
    self.at_zero = 0  # 'zero' = y[n] = x[n] - x[n - 1] 
    self.at_both = 0  # 'both' = y[n] = x[n] - x[n - 2] 

    self.value = 0
    self.increment = (np.pi*2) / SAMPLE_RATE / self.conf['shake time']

    # Calculate what shake energy will end at, to normalize output
    self.gain = 0
    while self.value < 2 * np.pi:
      self.value += self.increment
      self.gain += 1 - np.cos(self.value)
    # gain is now the max shake energy will reach,
    # we find the inverse, st we can normalize output
    if DEBUG:
      print(self.gain)
    self.gain =( 2**14.8 ) / self.gain


'''
GLOBAL SHAKER OBJECT
'''
s = Shaker()


'''
CALLBACK FUNCTION FOR SHAKER AUDIO
'''
def callback(in_data, frame_count, time_info, flag):
  # Data buffer used to store samples before sent to output
  data = np.zeros(CHUNK, dtype=np.int16)

  # # Write samples
  for i in range(CHUNK):
    # Add energy to shaker
    if s.value < (np.pi * 2):
      s.value += s.increment
      s.shake_energy += 1 - np.cos(s.value)

    # Exponential system decay
    s.shake_energy *= s.conf['system decay']

    # Bean collision adds energy
    if random.random() <= s.conf['prob']:
      s.sound_level += s.shake_energy

    # Noise generator
    input = s.sound_level * ((random.random() * 2) - 1)

    # Calculate an expontial decay of sound
    s.sound_level *= s.conf['sound decay']

    # Gourd resonance filters
    this_sample = 0
    for filt in s.filters:
      s.buf[0] = s.buf[0] + filt['f'] * (input - s.buf[0] + filt['fb'] * (s.buf[0] - s.buf[1]))
      s.buf[1] = s.buf[1] + filt['f'] * (s.buf[0] - s.buf[1])
      this_sample += s.buf[0] - s.buf[1]

    # Add sample to buffer
    data[i] = this_sample * s.gain
  
  if DEBUG and s.max < np.max(np.abs(data)):
    s.max = np.max(np.abs(data))
    print(s.max)

  return (data, pyaudio.paContinue)


'''
Open pyaudio, runs on audio thread
'''
def open_pyaudio(stream):
  stream.start_stream()
  while stream.is_active():
    time.sleep(0.1)

'''
Main function
'''
if __name__ == '__main__':
  # PyAudio stuff
  p = pyaudio.PyAudio()
  stream = p.open(format=FORMAT,
                  channels=CHANNELS,
                  rate=SAMPLE_RATE,
                  frames_per_buffer=CHUNK,
                  output=True,
                  stream_callback=callback)

  audio_thread = threading.Thread(target=open_pyaudio, args=(stream,))
  audio_thread.start()


  # Register key presses
  tty.setcbreak(sys.stdin)  
  print("press 'a' to shake")
  print("press 'q' to quit")
  while True:
    ## Table of key codes  https://www.asciitable.com/
    key = ord(sys.stdin.read(1))  # key captures the key-code 
    if key == 97:
      s.value = 0
      if DEBUG:
        print(f"s.value: {s.value}")

    if key == 113:
      print("Quitting...")
      stream.stop_stream()
      stream.close()
      p.terminate()
      audio_thread.join()
      sys.exit(0)
