import json


def formatting_json_view(data):
    return json.dumps(data, indent=4)
