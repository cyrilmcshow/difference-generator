import json


def json_view(data):
    result = [json.dumps(data, indent=4)]
    return ''.join(result)
