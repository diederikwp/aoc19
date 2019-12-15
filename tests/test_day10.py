import unittest

from pathlib import Path
from days.day10 import parse_puzzle_input, count_num_visible, group_asteroids_by_direction, solve_part_1, solve_part_2


class TestDay10(unittest.TestCase):
    def setUp(self):
        self.test_input_1 = Path('tests/input/test_input_day10_01.txt').read_text()
        self.test_input_2 = Path('tests/input/test_input_day10_02.txt').read_text()
        self.test_input_3 = Path('tests/input/test_input_day10_03.txt').read_text()
        self.test_input_4 = Path('tests/input/test_input_day10_04.txt').read_text()
        self.test_input_5 = Path('tests/input/test_input_day10_05.txt').read_text()

    def test_parse_puzzle_input(self):
        self.assertEqual(parse_puzzle_input(self.test_input_2),
                         [(6, 0), (8, 0),
                          (0, 1), (3, 1), (5, 1),
                          (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2),
                          (1, 3), (3, 3), (5, 3), (6, 3), (7, 3),
                          (1, 4), (4, 4),
                          (2, 5), (7, 5), (9, 5),
                          (0, 6), (3, 6), (8, 6),
                          (1, 7), (2, 7), (4, 7), (7, 7), (8, 7), (9, 7),
                          (0, 8), (1, 8), (5, 8), (8, 8),
                          (1, 9), (6, 9), (7, 9), (8, 9), (9, 9)])

    def test_count_num_visible(self):
        asteroids = [(0, 1), (0, 4),
                     (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
                     (3, 4),
                     (4, 3), (4, 4)]

        self.assertEqual(count_num_visible(asteroids, 0), 7)
        self.assertEqual(count_num_visible(asteroids, 1), 7)
        self.assertEqual(count_num_visible(asteroids, 2), 6)
        self.assertEqual(count_num_visible(asteroids, 3), 7)
        self.assertEqual(count_num_visible(asteroids, 4), 7)
        self.assertEqual(count_num_visible(asteroids, 5), 7)
        self.assertEqual(count_num_visible(asteroids, 6), 5)
        self.assertEqual(count_num_visible(asteroids, 7), 7)
        self.assertEqual(count_num_visible(asteroids, 8), 8)
        self.assertEqual(count_num_visible(asteroids, 9), 7)

    def test_solve_part_1(self):
        self.assertEqual(solve_part_1(self.test_input_1), 8)
        self.assertEqual(solve_part_1(self.test_input_2), 33)
        self.assertEqual(solve_part_1(self.test_input_3), 35)
        self.assertEqual(solve_part_1(self.test_input_4), 41)
        self.assertEqual(solve_part_1(self.test_input_5), 210)

    def test_solve_part_2(self):
        self.assertEqual(solve_part_2(self.test_input_5), 802)
