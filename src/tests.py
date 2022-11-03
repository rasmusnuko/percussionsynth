from concept import phism_shaker

if __name__ == '__main__':
  # Maraca
  maraca_conf = { 'prob': 4,
                  'system decay': 0.999,
                  'sound decay': 0.95,
                  'shells': [{'freq': 3000, 'reso': 0.96}],
                  'shake time': 50,
                  'filename': 'maraca'}

  # Sekere
  sekere_conf = { 'prob': 16,
                  'system decay': 0.999,
                  'sound decay': 0.96,
                  'shells': [{'freq': 5500, 'reso': 0.6}],
                  'shake time': 50,
                  'filename': 'sekere'}

  # Cabasa
  cabasa_conf = { 'prob': 2,
                  'system decay': 0.997,
                  'sound decay': 0.95,
                  'shells': [{'freq': 3000, 'reso': 0.7}],
                  'shake time': 50,
                  'filename': 'cabasa'}

  # Guiro
  guiro_conf  = { 'prob': 8,
                  'system decay': 0.997,
                  'sound decay': 0.95,
                  'shells': [{'freq': 2500, 'reso': 0.97},
                             {'freq': 4000, 'reso': 0.97}],
                  'shake time': 50,
                  'filename': 'guiro'}

  # Tambourine
  tambou_conf = { 'prob': 32,
                  'system decay': 0.9985,
                  'sound decay': 0.95,
                  'shells': [{'freq': 2300, 'reso': 0.97},
                             {'freq': 5600, 'reso': 0.995},
                             {'freq': 8100, 'reso': 0.995}],
                  'shake time': 50,
                  'filename': 'tambourine'}

  # Sleigh bell
  sleigh_conf = { 'prob': 32,
                  'system decay': 0.9994,
                  'sound decay': 0.97,
                  'shells': [{'freq': 2500, 'reso': 0.999},
                             {'freq': 5300, 'reso': 0.999},
                             {'freq': 6500, 'reso': 0.999},
                             {'freq': 8300, 'reso': 0.999},
                             {'freq': 9800, 'reso': 0.999}],
                  'shake time': 50,
                  'filename': 'sleighbells'}

  # Water drops
  water_conf  = { 'prob': 8192,
                  'system decay': 0.999,
                  'sound decay': 0.95,
                  'shells': [{'freq': 400, 'reso': 0.9985},
                             {'freq': 600, 'reso': 0.9985},
                             {'freq': 750, 'reso': 0.9985}],
                  'shake time': 50,
                  'filename': 'waterdrops'}

  # Water drops
  bamboo_conf = { 'prob': 1024,
                  'system decay': 0.95,
                  'sound decay': 0.99995,
                  'shells': [{'freq': 2200, 'reso': 0.995},
                             {'freq': 2800, 'reso': 0.995},
                             {'freq': 3400, 'reso': 0.995}],
                  'shake time': 50,
                  'filename': 'bamboowindchimes'}

