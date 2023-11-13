from itertools import chain


def get_child(data, depth=0, space_count=4):
    if not isinstance(data, dict):
        return data
    result = []
    space_for_changed_file = ' ' * depth * space_count
    depth += 1
    for key, value in data.items():
        result.append(
            f"{space_for_changed_file}    {key}: {get_child(value, depth)}"
        )
    return '{\n' + '\n'.join(result) + '\n' + space_for_changed_file + '}'


def stylish_view(diff, depth=0, space_count=4):  # noqa C901
    lines = []
    space_for_changed_file = ' ' * depth * space_count
    depth += 1
    for upper_key, upper_value in diff.items():
        type_ = upper_value.get('type')
        value = upper_value.get('value')
        value_from = upper_value.get('from')
        value_to = upper_value.get('to')
        if type_ == 'nested':
            lines.append(
                f"{space_for_changed_file}    {upper_key}: "
                f"{stylish_view(value, depth)}")
        elif type_ == 'added':
            value = upper_value.get('value')
            lines.append(
                f"{space_for_changed_file}  + {upper_key}: "
                f"{get_child(value, depth)}")
        elif type_ == 'removed':
            lines.append(
                f"{space_for_changed_file}  - {upper_key}: "
                f"{get_child(value, depth)}")
        elif type_ == 'changed':
            lines.append(
                f"{space_for_changed_file}  - {upper_key}: "
                f"{get_child(value_from, depth)}")
            lines.append(
                f"{space_for_changed_file}  + {upper_key}: "
                f"{get_child(value_to, depth)}")
        elif type_ == 'unchanged':
            lines.append(
                f"{space_for_changed_file}    {upper_key}: "
                f"{get_child(value, depth)}")
        result = list(chain('{', lines, [space_for_changed_file + '}']))

    return '\n'.join(result)
