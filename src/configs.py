from concept import phism_shaker
'''
Configs from article
'''
# Maraca
maraca_conf = { 'num beans': 32,
                'prob': 32,
                'system decay': 0.999,
                'sound decay': 0.95,
                'zeros': ['zero'],
                'shells': [{'freq': 4200, 'q': 0.96}],
                'shake time': 50e-3,
                'name': 'maraca'}

# Sekere
sekere_conf = { 'num beans': 32,
                'prob': 16,
                'system decay': 0.999,
                'sound decay': 0.96,
                'zeros': ['both'],
                'shells': [{'freq': 5500, 'q': 0.6}],
                'shake time': 30e-3,
                'name': 'sekere'}

# Cabasa
cabasa_conf = { 'num beans': 32,
                'prob': 2,
                'system decay': 0.997,
                'sound decay': 0.95,
                'zeros': ['zero'],
                'shells': [{'freq': 3000, 'q': 0.7}],
                'shake time': 50e-3,
                'name': 'cabasa'}

# Guiro
guiro_conf  = { 'num beans': 32,
                'prob': 8,
                'system decay': 0.997,
                'sound decay': 0.95,
                'zeros': ['both'],
                'shells': [{'freq': 2500, 'q': 0.97},
                            {'freq': 4000, 'q': 0.97}],
                'shake time': 25e-3,
                'name': 'guiro'}

### ### # Tambourine
### ### tambou_conf = { 'num beans': 32,
### ###                 'prob': 32,
### ###                 'system decay': 0.9985,
### ###                 'sound decay': 0.95,
### ###                 'zeros': ['both'],
### ###                 'shells': [{'freq': 2300, 'q': 0.96},
### ###                            {'freq': 5600, 'q': 0.995},
### ###                             {'freq': 8100, 'q': 0.995}],
### ###                 'shake time': 33e-3,
### ###                 'name': 'tambourine'}

# Sleighbells
sleigh_conf = { 'num beans': 32,
                'prob': 32,
                'system decay': 0.9994,
                'sound decay': 0.97,
                'zeros': ['both'],
                'shells': [{'freq': 2500, 'q': 0.999},
                            {'freq': 5300, 'q': 0.999},
                            {'freq': 6500, 'q': 0.999},
                            {'freq': 8300, 'q': 0.999},
                            {'freq': 9800, 'q': 0.999}],
                'shake time': 60e-3,
                'name': 'sleighbells'}

# Water drops
water_conf  = { 'num beans': 16,
                'prob': 8192,
                'system decay': 0.999,
                'sound decay': 0.95,
                'zeros': ['both'],
                'shells': [{'freq': 2500, 'q': 0.99},
                            {'freq': 4000, 'q': 0.98}],
                # 'shells': [{'freq': 400, 'q': 0.9985},
                #             {'freq': 600, 'q': 0.9985},
                #             {'freq': 750, 'q': 0.9985}],
                'shake time': 5e-3,
                'name': 'waterdrops'}

# Bamboo wind chimes
bamboo_conf = { 'num beans': 6,
                'prob': 1024,
                'system decay': 0.95,
                'sound decay': 0.99995,
                'zeros': [],
                'shells': [{'freq': 2200, 'q': 0.995},
                            {'freq': 2800, 'q': 0.995},
                            {'freq': 3400, 'q': 0.995}],
                'shake time': 1e-3,
                'name': 'bamboowindchimes'}

confs = [maraca_conf, sekere_conf, cabasa_conf, guiro_conf,
         sleigh_conf, water_conf, bamboo_conf]

def choose_config():

    for i, conf in enumerate(confs):
        print(f"{i+1}: {conf['name']}")

    choice = -1
    while not (0 < choice <= len(confs)):
        try:
          choice = int(input("Choose: "))
        except:
          print("give int u eediot")

    return confs[choice - 1]


if __name__ == '__main__':
  phism_shaker(maraca_conf)
  phism_shaker(sekere_conf)
  phism_shaker(cabasa_conf)
  phism_shaker(guiro_conf)
  phism_shaker(tambou_conf)
  phism_shaker(sleigh_conf)
  phism_shaker(water_conf)
  phism_shaker(bamboo_conf)
