import unittest

from days.day06 import parse_input, solve_part_1, solve_part_2
from pathlib import Path


class TestDay06(unittest.TestCase):
    def setUp(self):
        self.test_input_1 = Path('tests/input/test_input_day06_01.txt').read_text()
        self.test_input_2 = Path('tests/input/test_input_day06_02.txt').read_text()
        self.test_input_3 = Path('tests/input/test_input_day06_03.txt').read_text()

    def test_parse_input(self):
        nodes, edges, edges_reversed = parse_input(self.test_input_1)

        self.assertEqual(nodes, {'COM', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'})

        self.assertEqual(edges, {'COM': {'B'},
                                 'B': {'C', 'G'},
                                 'C': {'D'},
                                 'D': {'E', 'I'},
                                 'E': {'F', 'J'},
                                 'G': {'H'},
                                 'J': {'K'},
                                 'K': {'L'}})

        self.assertEqual(edges_reversed, {'B': 'COM',
                                          'C': 'B',
                                          'D': 'C',
                                          'E': 'D',
                                          'F': 'E',
                                          'G': 'B',
                                          'H': 'G',
                                          'I': 'D',
                                          'J': 'E',
                                          'K':  'J',
                                          'L': 'K'})

    def test_solve_part_1(self):
        self.assertEqual(solve_part_1(self.test_input_1), 42)

    def test_solve_part_2(self):
        self.assertEqual(solve_part_2(self.test_input_2), 4)
        self.assertEqual(solve_part_2(self.test_input_3), 5)


if __name__ == '__main__':
    unittest.main()