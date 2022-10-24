import os
import shutil
import json
import pandas as pd
import xml.etree.ElementTree as ET
import pickle

path = r'E:\file\Code\Python\datasets\merged\val\labels'
classes = {'xy': 1, 'wcaqm': 2, 'wcgz': 3, 'aqmzc': 4, 'gzzc': 0}
calc_cls = {1: 0, 2: 0, 3: 0, 4: 0, 0: 0}

txts = os.listdir(path)

for txt in txts:
    with open(os.path.join(path, txt)) as f:
        for i in f:
            calc_cls[int(i[0])] += 1
print(calc_cls)
