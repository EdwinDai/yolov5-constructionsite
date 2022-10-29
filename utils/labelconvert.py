import os
import shutil
import json
import pandas as pd

path = r'E:\file\Code\Python\datasets\cigarette\train\labels\\'
dest = r'E:\file\Code\Python\datasets\converted\\'
file = r'000183.txt'

txts = os.listdir(path)
for txt in txts:
    txt_name = dest + txt  # 生成txt文件你想存放的路径
    txt_file = open(txt_name, 'w')

    with open(os.path.join(path, txt), 'r') as f:
        a = f.readlines()
        for i in a:
            content = i
            if i[0] == str(0):
                txt_file.write(content)
    f.close()
