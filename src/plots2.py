from realtime import Shaker
from configs import confs
import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.io.wavfile import write
plt.rcParams["figure.figsize"] = (12,3)

for conf in confs:
    temp = 0
    shake_energy = 0
    sound_lvl = 0
    sound_lvls = []
    vals = []
    audio = 0
    audios = []
    shaker = Shaker(conf)
    for i in range(int(5 * 44100)):
        # Increment during shake time
        if temp < 2*np.pi:
            temp += ((2 * np.pi) / 44100 / shaker.conf['shake time'])
        shake_energy += (1 - np.cos(temp))

        # Collision
        if random.random() <= 1 / shaker.conf['prob']:
            sound_lvl += shake_energy

        shake_energy *= shaker.conf['system decay']
    
        audio = sound_lvl * (2*random.random()-1)

        sound_lvl *= shaker.conf['sound decay']
    
        # Append values
        vals.append(shake_energy)
        sound_lvls.append(sound_lvl)
    
        # Filter audio
        this_sample = 0
        for filt in shaker.filters:
          shaker.buf[0] = shaker.buf[0] + filt['f'] * (audio - shaker.buf[0] + filt['fb'] * (shaker.buf[0] - shaker.buf[1]))
          shaker.buf[1] = shaker.buf[1] + filt['f'] * (shaker.buf[0] - shaker.buf[1])
          this_sample += shaker.buf[0] - shaker.buf[1]
    
        audios.append(this_sample)
    
        # Exponential decay
    

    # Output generated audio as wav file
    # data = np.max(np.abs(audios)) * np.array(audios) * 2**15   # For waterdrops config
    data = shaker.gain * np.array(audios)
    write(f"example_{shaker.conf['name']}.wav", 44100, data.astype(np.int16))

    ## PLOTTING
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    fig.suptitle(f'{shaker.conf["name"].upper()}')
    # Plot shaker energy
    ax1.plot(vals)
    # Plot sound level
    ax2.plot(sound_lvls)
    # Plot audio
    ax3.plot(data)

    plt.savefig(f'example_{shaker.conf["name"]}.png', dpi=100)

    plt.show()
