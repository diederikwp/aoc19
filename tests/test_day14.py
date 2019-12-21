import unittest
from pathlib import Path

from days.day14 import parse_puzzle_input, Material, solve_part_1


class TestDay14(unittest.TestCase):
    def setUp(self):
        self.puzzle_input_1 = Path('tests/input/test_input_day14_01.txt').read_text()
        self.puzzle_input_2 = Path('tests/input/test_input_day14_02.txt').read_text()
        self.puzzle_input_3 = Path('tests/input/test_input_day14_03.txt').read_text()
        self.puzzle_input_4 = Path('tests/input/test_input_day14_04.txt').read_text()
        self.puzzle_input_5 = Path('tests/input/test_input_day14_05.txt').read_text()
        self.puzzle_input_6 = Path('tests/input/test_input_day14_06.txt').read_text()

    def test_parse_input(self):
        parsed = parse_puzzle_input(self.puzzle_input_1)
        self.assertEqual(parsed, {'A': (Material('A', 10), [Material('ORE', 10)]),
                                  'B': (Material('B', 1), [Material('ORE', 1)]),
                                  'C': (Material('C', 1), [Material('A', 7), Material('B', 1)]),
                                  'D': (Material('D', 1), [Material('A', 7), Material('C', 1)]),
                                  'E': (Material('E', 1), [Material('A', 7), Material('D', 1)]),
                                  'FUEL': (Material('FUEL', 1), [Material('A', 7), Material('E', 1)])})

    def test_solve_part_1(self):
        self.assertEqual(solve_part_1(self.puzzle_input_1), 31)
        self.assertEqual(solve_part_1(self.puzzle_input_2), 165)
        self.assertEqual(solve_part_1(self.puzzle_input_3), 13312)
        self.assertEqual(solve_part_1(self.puzzle_input_4), 180697)
        self.assertEqual(solve_part_1(self.puzzle_input_5), 2210736)
        self.assertEqual(solve_part_1(self.puzzle_input_6), 2)
