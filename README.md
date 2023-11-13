### Hexlet tests and linter status:
[![Actions Status](https://github.com/cyrilmcshow/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/cyrilmcshow/python-project-50/actions)
[![Python CI](https://github.com/cyrilmcshow/python-project-50/actions/workflows/tests-and-linter.yml/badge.svg)](https://github.com/cyrilmcshow/python-project-50/actions/workflows/tests-and-linter.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/759630111352b20f742c/maintainability)](https://codeclimate.com/github/cyrilmcshow/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/759630111352b20f742c/test_coverage)](https://codeclimate.com/github/cyrilmcshow/python-project-50/test_coverage)

## Difference generator
> A command line tool to calculate the difference between two data structures. Runs from the command line, compares two configuration files and shows a difference. Working with JSON and YAML. Provides output in stylish, plain and json format.
### Usage:
#### Help: 
```sh
$ gendiff -h
```
#### Running:
```sh
$ gendiff <file_path1> <file_path2> --format <format>
```
##### format - optional parameter, default value is 'stylish'. Possible values: 'stylish', 'plain', 'json'.
### Setup 
#### Using Makefile:
```sh
$ make install
```
```sh
$ make build
```
```sh
$ make package-install
```
### Asciinemas
[![asciicast](https://asciinema.org/a/gPfnazt23V9L6a3BEp5Hfgn9m.svg)](https://asciinema.org/a/gPfnazt23V9L6a3BEp5Hfgn9m)
