from realtime import Shaker
from configs import confs
import matplotlib.pyplot as plt
import numpy as np
import random

temp = 0
shake_energy = 0
sound_lvl = 0
sound_lvls = []
vals = []
audio = 0
audios = []
maraca_audio = []
sleighbells_audio = []

maraca = Shaker(confs[0])
sleighbells = Shaker(confs[4])

for i in range(int(0.2 * 44100)):
    # Increment during shake time
    if temp < 2*np.pi:
        temp += ((2 * np.pi) / 44100 / 0.05)
    shake_energy += (1 - np.cos(temp))

    # Collision
    if random.randint(0, 1024) < 32:
        sound_lvl += shake_energy

    audio = sound_lvl * (2*random.random()-1)

    # Append values
    vals.append(shake_energy)
    sound_lvls.append(sound_lvl)
    audios.append(audio)

    # Filter audio
    this_sample_maraca = 0
    for filt in maraca.filters:
      maraca.buf[0] = maraca.buf[0] + filt['f'] * (audio - maraca.buf[0] + filt['fb'] * (maraca.buf[0] - maraca.buf[1]))
      maraca.buf[1] = maraca.buf[1] + filt['f'] * (maraca.buf[0] - maraca.buf[1])
      this_sample_maraca += maraca.buf[0] - maraca.buf[1]

    maraca_audio.append(this_sample_maraca)

    this_sample_sleigh = 0
    for filt in sleighbells.filters:
      sleighbells.buf[0] = sleighbells.buf[0] + filt['f'] * (audio - sleighbells.buf[0] + filt['fb'] * (sleighbells.buf[0] - sleighbells.buf[1]))
      sleighbells.buf[1] = sleighbells.buf[1] + filt['f'] * (sleighbells.buf[0] - sleighbells.buf[1])
      this_sample_sleigh += sleighbells.buf[0] - sleighbells.buf[1]

    sleighbells_audio.append(this_sample_sleigh)


    # Exponential decay
    shake_energy *= 0.999
    sound_lvl *= 0.95

        
# Plot shaker energy
plt.plot(vals)
plt.xlabel('samples')
plt.ylabel('Value of shakeEnergy')
plt.show()

# Plot sound level
plt.plot(sound_lvls)
plt.xlabel('samples')
plt.ylabel('Value of sndLevel')
plt.show()

# Plot audio
plt.plot(audios)
plt.xlabel('samples')
plt.ylabel('Amplitude of audio signal')
plt.show()

# Plot audio
plt.plot(maraca_audio)
plt.xlabel('samples')
plt.ylabel('Amplitude of maraca audio signal')
plt.show()

# Plot audio
plt.plot(sleighbells_audio)
plt.xlabel('samples')
plt.ylabel('Amplitude of maraca audio signal')
plt.show()
