from gendiff import generate_diff
import pytest


def get_answer(type_formatter, path):
    if type_formatter == 'stylish':
        with open(path, 'r') as file:
            answer = file.read()
    elif type_formatter == 'plain':
        with open(path, 'r') as file:
            answer = file.read()
    return answer


@pytest.mark.parametrize('path1,path2,type_formatter, answer_path', [
    ('./tests/fixtures/file1.json', './tests/fixtures/file2.json', 'stylish', './tests/fixtures/answer.txt'),
    ('./tests/fixtures/file1.yml', './tests/fixtures/file2.yml', 'stylish', './tests/fixtures/answer.txt'),
    ('./tests/fixtures/file1.json', './tests/fixtures/file2.json', 'plain', './tests/fixtures/answer_plain'),
    ('./tests/fixtures/file1.yml', './tests/fixtures/file2.yml', 'plain', './tests/fixtures/answer_plain')
])
def test_generate_diff(path1, path2, type_formatter, answer_path):
    answer = get_answer(type_formatter, answer_path)
    assert generate_diff(path1, path2, type_formatter) == answer
