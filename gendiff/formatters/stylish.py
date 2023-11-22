

def convert(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value


def convert_dictionary_to_string(data, depth=0, space_count=4):
    if not isinstance(data, dict):
        return data
    result = ['{']
    space_for_changed_file = ' ' * depth * space_count
    depth += 1
    for key, value in data.items():
        result.append(
            f"{space_for_changed_file}    {key}: {convert_dictionary_to_string(value, depth)}" # noqa E501
        )
    result.append(f'{space_for_changed_file}{"}"}')
    return '\n'.join(result)


def load_stylish_view(diff, depth=0, space_count=4):  # noqa C901
    lines = []
    space_for_changed_file = ' ' * depth * space_count
    depth += 1
    for upper_key, upper_value in diff.items():
        element_type = upper_value.get('type')
        value = convert(upper_value.get('value'))
        value_from = convert(upper_value.get('from'))
        value_to = convert(upper_value.get('to'))
        if element_type == 'nested':
            lines.append(
                f"{space_for_changed_file}    {upper_key}: "
                f"{load_stylish_view(value, depth)}")
        elif element_type == 'added':
            lines.append(
                f"{space_for_changed_file}  + {upper_key}: "
                f"{convert_dictionary_to_string(value, depth)}")
        elif element_type == 'removed':
            lines.append(
                f"{space_for_changed_file}  - {upper_key}: "
                f"{convert_dictionary_to_string(value, depth)}")
        elif element_type == 'changed':
            lines.append(
                f"{space_for_changed_file}  - {upper_key}: "
                f"{convert_dictionary_to_string(value_from, depth)}")
            lines.append(
                f"{space_for_changed_file}  + {upper_key}: "
                f"{convert_dictionary_to_string(value_to, depth)}")
        elif element_type == 'unchanged':
            lines.append(
                f"{space_for_changed_file}    {upper_key}: "
                f"{convert_dictionary_to_string(value, depth)}")
        else:
            raise ValueError
        result = ['{']
        result.extend(lines)
        result.append(space_for_changed_file + '}')
    return '\n'.join(result)
