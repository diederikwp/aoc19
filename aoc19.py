#!/usr/bin/env python3

import argparse
import sys

from importlib import import_module
from pathlib import Path


def main():
    # Parse args
    parser = argparse.ArgumentParser(description='Run any of the Advent of Code puzzle solvers on any input')

    parser.add_argument('day', type=int, help='Number between 1 and 25 indicating the day of the puzzle.')
    parser.add_argument('part', choices=['1', '2'], nargs='?',
                        help='Indicates the first or second part of the puzzle. If omitted '
                        'solve both parts and separate their solutions by a newline.')

    input_group = parser.add_mutually_exclusive_group()
    input_group.add_argument('--stdin', action='store_true', help='Take input from stdin.')
    input_group.add_argument('-i', dest='input_file',
                             help='Path to input file. If -i and --stdin are omitted, use the official puzzle input'
                             'instead.')

    args = parser.parse_args()

    # Load correct module
    module_path = Path(f'days/day{args.day:02d}.py')
    day_module = import_module(f'days.day{args.day:02d}')

    # Read puzzle input
    # Todo: Handle file existence and permission exceptions
    if args.stdin:
        puzzle_input = sys.stdin.read()
    else:
        in_path = Path(args.input_file) if args.input_file is not None else Path(f'days/input/day{args.day:02}.txt')
        puzzle_input = in_path.read_text()

    # Solve and print solution
    if args.part == '1' or args.part is None:
        if 'solve_part_1' not in dir(day_module):
            raise ValueError(f'There is no solution for part 1 of day {args.day}')

        print(day_module.solve_part_1(puzzle_input))

    if args.part == '2' or args.part is None:
        if 'solve_part_2' not in dir(day_module):
            raise ValueError(f'There is no solution for part 2 of day {args.day}')

        print(day_module.solve_part_2(puzzle_input))


if __name__ == '__main__':
    main()

