import json, os
import numpy as np


uniminds_data, minds_data = {}, {}

from load_KG_data import *
uniminds_data, minds_data = load_dbs()                    

for entry in NAMESPACES:
    print("uniminds %s: %i" % (entry, len(uniminds_data[entry]['name'])))
    print("minds %s: %i" % (entry, len(minds_data[entry]['name'])))
    for key in KEYS:
        try:
            print(key, '---> %i overlapping entries ' % len(np.intersect1d(uniminds_data[entry][key], minds_data[entry][key])))
        except TypeError:
            pass
