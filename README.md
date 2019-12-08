# Advent of Code 2019
My solutions to Advent of Code 2019, in Python.

This code is not equipped to
handle invalid input gracefully, since it is just for solving synthetic
puzzles.

## Project structure
```
├── aoc19.py                          -- CLI tool for running solutions
├── days
│   ├── day01.py                      -- Module for solving day 1
│   ├── day02.py                      -- Module for solving day 2
│   ├── ...
│   └── input
│       ├── day01.txt                 -- Official puzzle input for day 1
│       ├── day02.txt                 -- Official puzzle input for day 1
│       └── ...
├── README.md
└── tests
    ├── input
    │   ├── test_input_day01_01.txt   -- First test input for day 1
    │   ├── test_input_day01_02.txt   -- Second test input for day 2
    │   ├── test_input_day02_01.txt   -- First test input for day 1
    │   └── ...
    ├── test_day01.py                 -- Test cases for day 1
    ├── test_day02.py                 -- Test cases for day 2
    └── ...
```
## CLI tool
Puzzles can be solved by executing aoc19.py. Type `./aoc19.py -h` for help.

## Tests
Run all tests by typing `python -m unittest` in the project root.
