import json
import yaml


def parser(file1_path, file2_path):
    if '.json' in file1_path:
        data1 = json.load(open(file1_path))
    if '.json' in file2_path:
        data2 = json.load(open(file2_path))
    if '.yaml' or '.yml' in file1_path:
        data1 = yaml.load(open(file1_path), Loader=yaml.FullLoader)
    if '.yaml' or '.yml' in file1_path:
        data2 = yaml.load(open(file2_path), Loader=yaml.FullLoader)
    return data1, data2
