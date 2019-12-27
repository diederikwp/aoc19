import unittest
from pathlib import Path

from days.day13 import BreakoutGame, solve_part_1, solve_part_2


class TestDay13(unittest.TestCase):
    def setUp(self):
        # Just use the official puzzle input as test case. No other test cases are provided, and making custom test
        # cases through mocking an Intcode Program will take a lot of effort.
        self.puzzle_input_1 = Path('days/input/day13.txt').read_text()

    def test_solve_part_1(self):
        self.assertEqual(solve_part_1(self.puzzle_input_1), 260)

    def test_solve_part_2(self):
        self.assertEqual(solve_part_2(self.puzzle_input_1), 12952)


if __name__ == '__main__':
    unittest.main()
