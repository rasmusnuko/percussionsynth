from concept import phism_shaker

if __name__ == '__main__':
  # Maraca
  maraca_conf = { 'num beans': 32,
                  'prob': 32,
                  'system decay': 0.999,
                  'sound decay': 0.95,
                  'zeros': [-1],
                  'filters': [{'freq': 4200, 'q': 0.96}],
                  'shake time': 50,
                  'filename': 'maraca'}
  phism_shaker(maraca_conf)

  # Sekere
  sekere_conf = { 'num beans': 32,
                  'prob': 16,
                  'system decay': 0.999,
                  'sound decay': 0.96,
                  'zeros': [1, -1],
                  'filters': [{'freq': 5500, 'q': 0.6}],
                  'shake time': 30,
                  'filename': 'sekere'}
  phism_shaker(sekere_conf)

  # Cabasa
  cabasa_conf = { 'num beans': 32,
                  'prob': 2,
                  'system decay': 0.997,
                  'sound decay': 0.95,
                  'zeros': [-1],
                  'filters': [{'freq': 3000, 'q': 0.7}],
                  'shake time': 50,
                  'filename': 'cabasa'}
  phism_shaker(cabasa_conf)

  # Guiro
  guiro_conf  = { 'num beans': 32,
                  'prob': 8,
                  'system decay': 0.997,
                  'sound decay': 0.95,
                  'zeros': [1, -1],
                  'filters': [{'freq': 2500, 'q': 0.97},
                              {'freq': 4000, 'q': 0.97}],
                  'shake time': 25,
                  'filename': 'guiro'}
  phism_shaker(guiro_conf)

  # Tambourine
  tambou_conf = { 'num beans': 32,
                  'prob': 32,
                  'system decay': 0.9985,
                  'sound decay': 0.95,
                  'zeros': [1, -1],
                  'filters': [{'freq': 2300, 'q': 0.96},
                             {'freq': 5600, 'q': 0.995},
                              {'freq': 8100, 'q': 0.995}],
                  'shake time': 33,
                  'filename': 'tambourine'}
  phism_shaker(tambou_conf)

  # Sleighbells
  sleigh_conf = { 'num beans': 32,
                  'prob': 32,
                  'system decay': 0.9994,
                  'sound decay': 0.97,
                  'zeros': [1, -1],
                  'filters': [{'freq': 2500, 'q': 0.999},
                              {'freq': 5300, 'q': 0.999},
                              {'freq': 6500, 'q': 0.999},
                              {'freq': 8300, 'q': 0.999},
                              {'freq': 9800, 'q': 0.999}],
                  'shake time': 60,
                  'filename': 'sleighbells'}
  phism_shaker(sleigh_conf)

  # Water drops
  water_conf  = { 'num beans': 16,
                  'prob': 8192,
                  'system decay': 0.999,
                  'sound decay': 0.95,
                  'zeros': [1, -1],
                  'filters': [{'freq': 400, 'q': 0.9985},
                              {'freq': 600, 'q': 0.9985},
                              {'freq': 750, 'q': 0.9985}],
                  'shake time': 5,
                  'filename': 'waterdrops'}
  phism_shaker(water_conf)

  # Bamboo wind chimes
  bamboo_conf = { 'num beans': 6,
                  'prob': 1024,
                  'system decay': 0.95,
                  'sound decay': 0.99995,
                  'zeros': [],
                  'filters': [{'freq': 2200, 'q': 0.995},
                              {'freq': 2800, 'q': 0.995},
                              {'freq': 3400, 'q': 0.995}],
                  'shake time': 1,
                  'filename': 'bamboowindchimes'}
  phism_shaker(bamboo_conf)



