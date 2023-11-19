from gendiff.parser import parsing_file, get_file_and_extension
from gendiff.diff_calc import diff_calc
from gendiff.formatters.stylish import formatting_stylish_view
from gendiff.formatters.plain import formatting_plain_view
from gendiff.formatters.json import formatting_json_view


def generate_diff(file1_path, file2_path, format='stylish'):
    first_data_string, first_data_extension = get_file_and_extension(file1_path)
    second_data_string, second_data_extension = get_file_and_extension(file2_path) # noqa
    data1 = parsing_file(first_data_string, first_data_extension)
    data2 = parsing_file(second_data_string, second_data_extension)
    diff = diff_calc(data1, data2)
    if format == 'stylish':
        result = formatting_stylish_view(diff)
    elif format == 'plain':
        result = formatting_plain_view(diff)
    elif format == 'json':
        result = formatting_json_view(diff)
    return result
