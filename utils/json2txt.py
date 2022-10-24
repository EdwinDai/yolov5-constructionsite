import os
import shutil
import json
import pandas as pd

path = r'E:\file\Code\Python\datasets\cigarette\rawlabels'
errorpath = r'E:\file\Code\Python\datasets\error'
json_floder_path = r'E:\file\Code\Python\datasets\cigarette\rawlabels'
classes = {'xy': 1, 'wcaqm': 2, 'wcgz': 3, 'aqmzc': 4, 'gzzc': 0}

def find_error():
    jsons = os.listdir(path)
    for label in jsons:
        with open(os.path.join(path, label), 'r') as l:
            if l.readline(11) != '{"imagePath':
                l.close()
                shutil.move(os.path.join(os.path.join(path, label)), os.path.join(errorpath, label))


def convert(img_size, box):
    # dw = 1. / (img_size[0])
    # dh = 1. / (img_size[1])
    x = (box[0] + box[2]) / 2.0
    y = (box[1] + box[3]) / 2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    # x = x * dw
    # w = w * dw
    # y = y * dh
    # h = h * dh
    # x1 = box[0]
    # y1 = box[1]
    # x2 = box[2]
    # y2 = box[3]
    return (x, y, w, h)


def decode_json(json_floder_path, json_name, label):
    txt_name = r'E:\file\Code\Python\datasets\cigarette\labels2/' + json_name[0:-5] + '.txt'  # 生成txt文件你想存放的路径
    txt_file = open(txt_name, 'w')
    json_path = os.path.join(json_floder_path, json_name)
    data = json.load(open(json_path, 'r'))

    img_w = data['imageWidth']
    img_h = data['imageHeight']

    for i in data['shapes']:
        if i['shape_type'] == 'rectangle':
            try:
                x1 = float((i['points'][0][0])) / img_w
                y1 = float((i['points'][0][1])) / img_h
                x2 = float((i['points'][1][0])) / img_w
                y2 = float((i['points'][1][1])) / img_h
                if i['label'] == 'xmbhyc' or i['label'] == 'yw_gkxfw' or i['label'] == 'hxq_gjbs' or i[
                    'label'] == 'bj_bpmh' or i['label'] == 'kgg_ybf' or i['label'] == 'kgg_ybh' or i[
                    'label'] == 'bjdsyc':
                    continue
                else:
                    n = classes[i['label']]

                bb = (x1, y1, x2, y2)
                bbox = convert((img_w, img_h), bb)
                txt_file.write(str(n) + " " + " ".join([str(a) for a in bbox]) + '\n')
            except IndexError:
                print(json_name[0:-5] + '的' + i['label'] + "标签坐标缺失")


if __name__ == '__main__':
    json_names = os.listdir(json_floder_path)
    label = classes
    for json_name in json_names:
        if json_name[-4:] == 'json':
            print(json_name)
            label = decode_json(json_floder_path, json_name, label)
