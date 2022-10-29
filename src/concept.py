import numpy as np
from scipy.io.wavfile import write

SAMPLE_RATE = 44100

def phism_shaker(num_beans, shell_freq, shell_reso, sound_decay, system_decay, shake_time, shakes_pr_sec = 4, duration = 4, filename = "shaker"):
  temp, shake_energy, sound_level = 0, 0, 0
  
  gain = np.log(num_beans) / np.log(4) * 40 / num_beans

  # Gourd resonance filter
  coeffs = [0, 0]
  coeffs[0] = -shell_reso * 2 * np.cos(shell_freq * (np.pi * 2) / SAMPLE_RATE)
  coeffs[1] = shell_reso * shell_reso

  # Init output
  output = [0, 0]
  result = []
  for i in range(duration * SAMPLE_RATE):
    # Shake for X ms -> add shake energy
    if temp < (np.pi * 2):
      temp += (np.pi * 2) / SAMPLE_RATE / (shake_time / 1000)
      shake_energy += 1 - np.cos(temp)

    # Shake X times per second
    if i % (SAMPLE_RATE / shakes_pr_sec) == 0:
      temp = 0

    # Exponential system decay
    shake_energy *= system_decay

    # Model collision
    if np.random.randint(1024) < num_beans:
      sound_level += gain * shake_energy

    input = sound_level * np.random.random() * 2 - 1
      
    # Expontial decay of sound
    sound_level *= sound_decay

    # Gourd resonance filter
    input -= output[0]*coeffs[0]
    input -= output[1]*coeffs[1]
    output[1] = output[0]
    output[0] = input

    data = output[0] - output[1]

    result.append(data)

  scaled = np.int16(result / np.max(np.abs(result)) * 32767)
  write(f"{filename}.wav", SAMPLE_RATE, scaled)



if __name__ == '__main__':
  # Perry's shaker
  phism_shaker(64,      # number of beans
               3400,    # shell frequency (Hz)
               0.95,    # shell resonance (0 - 1)
               0.95,    # sound decay   (0 - 1)
               0.96,    # system decay  (0 - 1)
               50,      # shake time (millis)
               4,       # shakes per second
               4,       # duration of audio clip (seconds)
               "perryshaker")


  # High shaker  
  phism_shaker(80,      # number of beans
               6200,    # shell frequency (Hz)
               0.95,    # shell resonance (0 - 1)
               0.95,    # sound decay   (0 - 1)
               0.92,    # system decay  (0 - 1)
               25,      # shake time (millis)
               6,       # shakes per second
               4,       # duration of audio clip (seconds)
               "highshaker")
