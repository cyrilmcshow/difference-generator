def prepare_data(data):
    if isinstance(data, int):
        return int(data)
    if isinstance(data, dict):
        return '[complex value]'
    elif data not in ('true', 'false', 'null'):
        return f"'{data}'"
    return data


def formatting_plain_view(diff, incoming_key=None): # noqa
    lines = []
    for key, value in diff.items():
        path = f"{incoming_key + '.' if incoming_key else ''}{key}"
        element_type = value.get('type')
        element_value = value.get('value')
        old_value = value.get('from')
        new_value = value.get('to')
        if element_type == 'nested':
            lines.append(formatting_plain_view(element_value, path))
        elif element_type == 'added':
            line = (f"Property '{path}' was {element_type} "
                    f"with value: {prepare_data(element_value)}")
            lines.append(line)
        elif element_type == 'removed':
            line = f"Property '{path}' was {element_type}"
            lines.append(line)
        elif element_type == 'changed':
            line = (f"Property '{path}' was updated. "
                    f"From {prepare_data(old_value)} "
                    f"to {prepare_data(new_value)}")
            lines.append(line)
        elif element_type == 'unchanged':
            continue
        else:
            raise ValueError
    return '\n'.join(lines)
