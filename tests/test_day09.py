import unittest

from pathlib import Path
from days.day09 import solve_part_1, solve_part_2


class TestDay09(unittest.TestCase):
    def test_solve_part_1(self):
        puzzle_input = Path('tests/input/test_input_day09_01.txt').read_text()
        self.assertEqual(solve_part_1(puzzle_input), 2453265701)

    def test_solve_part_2(self):
        puzzle_input = '3,0,4,0,99'
        self.assertEqual(solve_part_2(puzzle_input), 2)
