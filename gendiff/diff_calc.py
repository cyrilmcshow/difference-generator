def diff_calc(data1, data2):  # noqa C901
    keys = data1.keys() | data2.keys()
    diff = {}
    for key in sorted(keys):
        if key not in data1:
            diff[key] = {'type': 'added',
                         'value': data2[key]}
        elif key not in data2:
            diff[key] = {'type': 'removed',
                         'value': data1[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = {'type': 'nested',
                         'value': diff_calc(data1[key], data2[key])}

        elif key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff[key] = {'type': 'unchanged',
                             'value': data1[key]}
            else:
                diff[key] = {'type': 'changed',
                             'from': data1[key],
                             'to': data2[key]}

    return diff
