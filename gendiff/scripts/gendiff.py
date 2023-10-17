#!/usr/bin/env python3
import argparse
from gendiff.app import generate_diff


def add_arg():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        type=str,
        default='FORMAT',
        help='set format of output'
    )
    args = parser.parse_args()
    return args


def main():
    print(add_arg())


if __name__ == '__main__':
    main()
