import json
import yaml


def get_file_and_extension(path):
    with open(path) as file:
        result = file.read()
        extension = '.json' if '.json' in file else '.yaml'
    return result, extension


def get_parse_file(data, file_extension):
    if file_extension == 'json':
        return json.load(data)
    elif file_extension == '.yaml' or '.yml':
        return yaml.load(data, Loader=yaml.FullLoader)
