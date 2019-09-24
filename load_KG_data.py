import json, os
import numpy as np



NAMESPACES = ['datasets', 'methods', 'activities',
              'agecategories', 'modalities', 'formats',
              'parcellationatlases', 'parcellationregions',
              'persons', 'preparations', 'protocols',
              'sex', 'species', 'experimentalpreparations',
              'projects']
KEYS = ['identifier', 'name', 'description', '@id']

def load_dbs():
    
    uniminds_data, minds_data = {}, {}
    
    for entry in NAMESPACES:

        uniminds_data[entry], minds_data[entry] = {}, {}
        for key in KEYS:
            minds_data[entry][key] = []
            uniminds_data[entry][key] = []

        filename = 'KGdb/minds-%s.json' % entry
        if os.path.isfile(filename):
            with open(filename) as f:
                dataJ = json.load(f)
            minds_dataJ = dataJ['results']

            for key in KEYS:
                if key in minds_dataJ[0]:
                    for i in range(len(minds_dataJ)):
                        minds_data[entry][key].append(minds_dataJ[i][key])

        filename = 'KGdb/uniminds-%s.json' % entry
        if os.path.isfile(filename):
            with open(filename) as f:
                dataJ = json.load(f)
            uniminds_dataJ = dataJ['results']

            for key in KEYS:
                if key in uniminds_dataJ[0]:
                    for i in range(len(uniminds_dataJ)):
                        uniminds_data[entry][key].append(uniminds_dataJ[i][key])


    for entry in NAMESPACES:
        print("uniminds %s: %i" % (entry, len(uniminds_data[entry]['name'])))
        print("minds %s: %i" % (entry, len(minds_data[entry]['name'])))
        
    return uniminds_data, minds_data
