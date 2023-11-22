import json


def load_json_view(data):
    return json.dumps(data, indent=4)
