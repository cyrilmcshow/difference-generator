def prepare_data(data):
    if isinstance(data, dict):
        return '[complex value]'
    elif data not in ('true', 'false', 'null'):
        return f"'{data}'"
    if data == '0':
        return 0
    return data


def plain_view(diff, incoming_key=None):
    lines = []
    for key, value in diff.items():
        path = f"{incoming_key + '.' if incoming_key else ''}{key}"

        type_ = value.get('type')
        value_ = value.get('value')
        old_value = value.get('from')
        new_value = value.get('to')
        if type_ == 'nested':
            lines.append(plain_view(value_, path))
        elif type_ == 'added':
            line = (f"Property '{path}' was {type_} "
                    f"with value: {prepare_data(value_)}")
            lines.append(line)
        elif type_ == 'removed':
            line = f"Property '{path}' was {type_}"
            lines.append(line)
        elif type_ == 'changed':
            line = (f"Property '{path}' was updated."
                    f" From {prepare_data(old_value)} "
                    f"to {prepare_data(new_value)}")
            lines.append(line)

    return '\n'.join(lines)
