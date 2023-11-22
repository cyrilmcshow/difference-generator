from gendiff.parser import get_parse_file, get_file_and_extension
from gendiff.diff_calc import diff_calc
from gendiff.formatters.stylish import load_stylish_view
from gendiff.formatters.plain import load_plain_view
from gendiff.formatters.json import load_json_view


def generate_diff(file1_path, file2_path, format='stylish'):
    first_data_string, first_data_extension = get_file_and_extension(file1_path)
    second_data_string, second_data_extension = get_file_and_extension(file2_path) # noqa
    data1 = get_parse_file(first_data_string, first_data_extension)
    data2 = get_parse_file(second_data_string, second_data_extension)
    diff = diff_calc(data1, data2)
    if format == 'stylish':
        result = load_stylish_view(diff)
    elif format == 'plain':
        result = load_plain_view(diff)
    elif format == 'json':
        result = load_json_view(diff)
    else:
        raise ValueError
    return result
