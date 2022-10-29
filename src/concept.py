import numpy as np
from scipy.io.wavfile import write

SOUND_DECAY = 0.95
SYSTEM_DECAY = 0.95
SHELL_FREQUENCY = 3200
SHELL_RESO = 0.96
SAMPLE_RATE = 22050
NUM_BEANS = 64
DURATION = 4
GAIN = np.log(NUM_BEANS) / np.log(4) * 40 / NUM_BEANS


def main():
  temp, shake_energy, sound_level = 0, 0, 0

  # Gourd resonance filter
  coeffs = [0, 0]
  coeffs[0] = -SHELL_RESO * 2 * np.cos(SHELL_FREQUENCY * (np.pi * 2) / SAMPLE_RATE)
  coeffs[1] = SHELL_RESO * SHELL_RESO

  # Init output
  output = [0, 0]
  result = []
  for i in range(DURATION * SAMPLE_RATE):
    # Shake for 50ms -> add shake energy
    if temp < (np.pi * 2):
      temp += (np.pi * 2) / SAMPLE_RATE / 0.05
      shake_energy += 1 - np.cos(temp)

    # Shake 4 times per second
    if i % (SAMPLE_RATE / 4) == 0:
      temp = 0

    # Exponential system decay
    shake_energy *= SYSTEM_DECAY

    # Model collision
    if np.random.randint(1024) < NUM_BEANS:
      sound_level += GAIN * shake_energy

    input = sound_level * np.random.random() * 2 - 1
      
    # Expontial decay of sound
    sound_level *= SOUND_DECAY

    # Gourd resonance filter
    input -= output[0]*coeffs[0]
    input -= output[1]*coeffs[1]
    output[1] = output[0]
    output[0] = input

    data = output[0] - output[1]

    result.append(data)

  scaled = np.int16(result / np.max(np.abs(result)) * 32767)
  write("shaker.wav", SAMPLE_RATE, scaled)



if __name__ == '__main__':
  main()
