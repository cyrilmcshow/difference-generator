from gendiff.parser import parser
from gendiff.diff_calc import diff_calc
from gendiff.formatters.stylish import view_stylish


def generate_diff(file1_path, file2_path, format='stylish'):
    data1, data2 = parser(file1_path, file2_path)
    diff = diff_calc(data1, data2)
    result = view_stylish(diff)
    print(result)
    return result
