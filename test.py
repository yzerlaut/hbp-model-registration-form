import json, os
import numpy as np


uniminds_data, minds_data = {}, {}

from load_KG_data import *
uniminds_data, minds_data = load_dbs()                    

for entry in NAMESPACES:
    print('-------------------------------')
    print("uniminds %s: %i" % (entry, len(uniminds_data[entry]['name'])))
    print("minds %s: %i" % (entry, len(minds_data[entry]['name'])))
    for key in ['name', 'identifier']:
        try:
            print('   ---> %i overlapping entries (based on %s)' %\
                  (len(np.intersect1d(np.array(uniminds_data[entry][key], dtype=str), np.array(minds_data[entry][key], dtype=str))) ,key))
        except ValueError:
            pass


