import os
import shutil
import json
import pandas as pd
import xml.etree.ElementTree as ET
import pickle

path = r'E:\file\Code\Python\datasets\helmet\aqm_gz\rawlabel'
errorpath = r'E:\file\Code\Python\datasets\error'
xml_floder_path = r'E:\file\Code\Python\datasets\helmet\aqm_gz\rawlabel'
classes = {'xy': 1, 'wcaqm': 2, 'wcgz': 3, 'aqmzc': 4, 'gzzc': 0}
exclude_cls = ['xmbhyc', 'yw_gkxfw', 'hxq_gjbs', 'bj_bpmh', 'kgg_ybf', 'kgg_ybh', 'bjdsyc']


def find_error():
    jsons = os.listdir(path)
    for label in jsons:
        with open(os.path.join(path, label), 'r') as l:
            if l.readline(11) != '{"imagePath':
                l.close()
                shutil.move(os.path.join(os.path.join(path, label)), os.path.join(errorpath, label))


def convert(img_size, box):
    dw = 1. / (img_size[0])
    dh = 1. / (img_size[1])
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    # x1 = box[0]
    # y1 = box[1]
    # x2 = box[2]
    # y2 = box[3]
    return (x, y, w, h)


def decode_json(xml_floder_path, json_name, label):
    txt_name = r'E:\file\Code\Python\datasets\helmet\aqm_gz\labels/' + json_name[0:-4] + '.txt'  # 生成txt文件你想存放的路径
    txt_file = open(txt_name, 'w')

    xml_path = os.path.join(xml_floder_path, json_name)
    root = ET.parse(xml_path).getroot()

    img_w = root.find('size').find('width').text
    img_h = root.find('size').find('height').text

    for obj in root.iter('object'):
        cls = obj.find('name').text
        # if cls in exclude_cls:
        #     continue
        cls_id = classes[str(cls)]

        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text),
             float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))

        bbox = convert((float(img_w), float(img_h)), b)
        txt_file.write(str(cls_id) + " " + " ".join([str(a) for a in bbox]) + '\n')


if __name__ == '__main__':
    json_names = os.listdir(xml_floder_path)
    label = classes
    for json_name in json_names:
        if json_name[-4:] == '.xml':
            print(json_name)
            label = decode_json(xml_floder_path, json_name, label)
