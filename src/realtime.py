import threading, sys, tty
import numpy as np
import pyaudio

### AUDIO VARS
SAMPLE_RATE = 44100
CHUNK       = 256
CHANNELS    = 1

class Shaker:
  def __init__(self):
    ### SHAKER CONFIG
    ## TODO make config loader
    self.shells = [ {'q': 0.96, 'freq': 4200} ]
    self.conf = {'num beans': 32,
                 'prob': 4,
                 'shells' : self.shells,
                 'zeros': 'zero',
                 'system decay': 0.999,
                 'sound decay': 0.95,
                 'shake time': 50,
                 'filename': "perryshaker"}
    
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
    self.gain = np.log(self.conf['num beans']) / np.log(4) * 40 / self.conf['num beans']
    
    ### ONE-ZERO FILTER VARIABLES
    self.at_zero = 0  # 'zero' = y[n] = x[n] - x[n - 1] 
    self.at_both = 0  # 'both' = y[n] = x[n] - x[n - 2] 


s = Shaker()


'''
CALLBACK FUNCTION FOR SHAKER AUDIO
'''
def callback(in_data, frame_count, time_info, flag):
  data = np.zeros( (1, CHUNK) )
  for i in range(CHUNK):
    # Exponential system decay
    s.shake_energy *= s.conf['system decay']

    # Collisions adds energy
    if np.random.randint(s.conf['prob']) == 0:
      s.sound_level += s.gain * s.shake_energy

    input = s.sound_level * np.random.random() * 2 - 1
      
    # Calculate an expontial decay of sound
    s.sound_level *= s.conf['sound decay']

    # Zeros at 0 or both (0 and Nyquist)
    if 'zero' in s.conf['zeros']:
      input -= s.at_zero
    elif 'both' in s.conf['zeros']:
      input -= s.at_both 

    # at_zero is a 1-sample delay, at_both is a 2-sample delay.
    s.at_zero = input
    s.at_both = s.at_zero

    # Gourd resonance filters
    for filt in s.filters:
      s.buf[0] = s.buf[0] + filt['f'] * (input - s.buf[0] + filt['fb'] * (s.buf[0] - s.buf[1]))
      s.buf[1] = s.buf[1] + filt['f'] * (s.buf[0] - s.buf[1])

    this_sample = s.buf[0] - s.buf[1]

    # Add sample to buffer
    data[0, i] = this_sample
  
  # TODO not scaled, find some gain that works
  # for amount of 'energy' measured with IMU

  # IDEA: cap 'energy' to 1:
  # IMU energy * random number (-1 - 1) * max_int_16bit will be of correct size(?) 

  # Map IMU 0 to (reasonably high IMU velocity) -> -1 to 1
  return (data, pyaudio.paContinue)


'''
Opens PyAudio stream
'''
def open_audio(stream):
  # PyAudio
  stream.start_stream()

'''
Main function
'''
if __name__ == '__main__':
  # PyAudio stuff
  p = pyaudio.PyAudio()
  stream = p.open(format=pyaudio.paFloat32,
                  channels=CHANNELS,
                  rate=SAMPLE_RATE,
                  output=True,
                  input=True,
                  stream_callback=callback)

  # Audio thread
  audio_thread = threading.Thread(target=open_audio, args=(stream,))
  audio_thread.start()

  # Register key presses
  tty.setcbreak(sys.stdin)  
  print("press 'a' to shake")
  print("press 'q' to quit")
  while True:
    # Table of key codes  https://www.asciitable.com/
    key = ord(sys.stdin.read(1))  # key captures the key-code 
    if key == 97:
      s.shake_energy += 1
    if key == 113:
      print("Quitting...")
      stream.stop_stream()
      stream.close()
      p.terminate()
      sys.exit(0)
