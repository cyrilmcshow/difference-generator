import json


def generate_diff(file1_path, file2_path):
    data1 = json.load(open(file1_path))
    data2 = json.load(open(file2_path))
    data1_keys = list(data1.keys())
    data2_keys = list(data2.keys())
    lines = []
    for key in sorted(data1 | data2):

        if key in data1_keys and key in data2_keys:
            if data1[key] == data2[key]:
                line = f'    {key}: {data1[key]}'
            else:
                line = f'  - {key}: {data1[key]}\n  + {key}: {data2[key]}'
        elif key in data1_keys:
            line = f'  - {key}: {data1[key]}'
        elif key in data2_keys:
            line = f'  + {key}: {data2[key]}'

        lines.append(f"\n{line}")

    result = f"{{{''.join(lines)}\n}}"
    print(result)
