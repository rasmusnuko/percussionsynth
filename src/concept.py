import numpy as np
from scipy.io.wavfile import write

SAMPLE_RATE = 44100

# https://www.musicdsp.org/en/latest/Filters/29-resonant-filter.html
def get_filters(input_filters):
  filters = []

  for filt in input_filters:
    f  = 2 * np.sin(np.pi * (filt['freq'] / SAMPLE_RATE))
    fb = filt['q'] + (filt['q']/(1-f))

    filters.append({'f': f, 'fb': fb})

  print(filters)

  return filters


def phism_shaker(conf):
  # Init
  temp, shake_energy, sound_level = 0, 0, 0
  gain = np.log(conf['num beans']) / np.log(4) * 40 / conf['num beans']

  print(f"Rendering {conf['filename']}.wav")

  # Gourd qnance filter
  filters = get_filters(conf['filters'])

  # Init buf
  buf = [0, 0]
  result = []
  prev_input = 0
  for i in range(4 * SAMPLE_RATE):          # 4 second audio clip
    # Shake for X ms -> add shake energy
    if temp < (np.pi * 2):
      temp += (np.pi * 2) / SAMPLE_RATE / (conf['shake time'] / 1000)
      shake_energy += 1 - np.cos(temp)

    # Shake 4 times per second
    if i % (SAMPLE_RATE / 4) == 0:
      temp = 0

    # Exponential system decay
    shake_energy *= conf['system decay']

    # Collisions adds energy
    if np.random.randint(conf['prob']) == 0:
      sound_level += gain * shake_energy

    input = sound_level * np.random.random() * 2 - 1
      
    # Calculate an expontial decay of sound
    sound_level *= conf['sound decay']

    # Gourd qnance filter
    for filt in filters:
      buf[0] = buf[0] + filt['f'] * ( input - buf[0] + filt['fb'] * (buf[0] - buf[1]) )
      buf[1] = buf[1] + filt['f'] * (buf[0] - buf[1])

    data = buf[0] - buf[1]

    # Zeros at either 0Hz or 1/2 SAMPLE_RATE Hz 
    for zero in conf['zeros']:
      data += zero * prev_input

    prev_input = input

    result.append(data)

  scaled = np.int16(result / np.max(np.abs(result)) * 32767)
  write(f"{conf['filename']}.wav", SAMPLE_RATE, scaled)


if __name__ == '__main__':
  # Perry's shaker
  perry_shells = [ {'q': 0.96, 'freq': 4200} ]

  perry_config = {'num beans': 32,
                  'prob': 4,
                  'shells' : perry_shells,
                  'system decay': 0.999,
                  'sound decay': 0.95,
                  'shake time': 50,
                  'filename': "perryshaker"}

  phism_shaker(perry_config)
