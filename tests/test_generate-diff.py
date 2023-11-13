from gendiff import generate_diff
import pytest


@pytest.fixture
def stylish_answer():
    with open('./tests/fixtures/answer.txt', 'r') as file:
        answer = file.read()
    return answer


@pytest.fixture
def stylish_plain():
    with open('./tests/fixtures/answer_plain', 'r') as file:
        answer = file.read()
    return answer


def test_generate_diff_json(stylish_answer):
    answer = stylish_answer
    assert generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json') == answer


def test_generate_diff_yaml(stylish_answer):
    answer = stylish_answer
    assert generate_diff('./tests/fixtures/file1.yml', './tests/fixtures/file2.yml') == answer


def test_generate_diff_json_plain(stylish_plain):
    answer = stylish_plain
    assert generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json', 'plain') == answer


def test_generate_diff_yaml_plain(stylish_plain):
    answer = stylish_plain
    assert generate_diff('./tests/fixtures/file1.yml', './tests/fixtures/file2.yml', 'plain') == answer
