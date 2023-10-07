#!/usr/bin/env python3
import argparse

def add_arg():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()

def main():
    print(add_arg())

if __name__ == '__main__':
    main()