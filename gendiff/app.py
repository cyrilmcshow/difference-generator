from gendiff.parser import parser
from gendiff.diff_calc import diff_calc
from gendiff.formatters.stylish import stylish_view
from gendiff.formatters.plain import plain_view
from gendiff.formatters.json import json_view


def generate_diff(file1_path, file2_path, format='stylish'):
    data1, data2 = parser(file1_path, file2_path)
    diff = diff_calc(data1, data2)
    if format == 'stylish':
        result = stylish_view(diff)
    elif format == 'plain':
        result = plain_view(diff)
    elif format == 'json':
        result = json_view(diff)
    print(result)
    return result
