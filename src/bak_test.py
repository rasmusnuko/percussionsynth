import threading, sys, tty
import numpy as np
import pyaudio

### AUDIO VARS
SAMPLE_RATE = 44100
CHUNK       = 256
CHANNELS    = 1

output_sound = False

'''
CALLBACK FUNCTION FOR SHAKER AUDIO
'''
def callback(in_data, frame_count, time_info, flag):
  if output_sound:
    data = np.random.rand(1,CHUNK)
  else:
    data = np.zeros((1, CHUNK))
  
  return (data, pyaudio.paContinue)

def open_audio(stream):
  # PyAudio
  stream.start_stream()

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
  print("press 'a' to toggle noise")
  while True:
    # Table of key codes  https://www.asciitable.com/
    key = ord(sys.stdin.read(1))  # key captures the key-code 
    if key == 97:
      output_sound = not output_sound 
    else:
      print("Quitting...")
      stream.stop_stream()
      stream.close()
      p.terminate()
      sys.exit(0)
