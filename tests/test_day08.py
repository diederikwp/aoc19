import unittest

from days.day08 import combine_layers, render_image, solve_part_1, solve_part_2, split_layers
from pathlib import Path


class TestDay08(unittest.TestCase):
    def test_combine_layers(self):
        layers = ['0222', '1122', '2212', '0000']
        self.assertEqual(combine_layers(layers, 2, 2), '0110')

    def test_render_image(self):
        flat_image = '1    1    1111 1  1 1111 '
        rendered_image = '#    \n' \
                         + '#    \n' \
                         + '#### \n' \
                         + '#  # \n' \
                         + '#### \n'

        self.assertEqual(render_image(flat_image, 5, 5), rendered_image)

    def test_split_layers(self):
        layers = split_layers('123456789012', 2, 3)
        self.assertEqual(layers, ['123456', '789012'])

        layers = split_layers('000123456007111202777309', 6, 4)
        self.assertEqual(layers, ['000123456007111202777309'])

        layers = split_layers('000123456007111202777309', 4, 3)
        self.assertEqual(layers, ['000123456007', '111202777309'])

    def test_solve_part_1(self):
        puzzle_input = Path('tests/input/test_input_day08_01.txt').read_text()
        self.assertEqual(solve_part_1(puzzle_input), 438)

    def test_solve_part_2(self):
        puzzle_input = Path('tests/input/test_input_day08_02.txt').read_text()
        rendered = '# # # # # # # # # # # # #\n' \
                   + '#########################\n' \
                   + '#                       #\n' \
                   + '#                       #\n' \
                   + '#                       #\n' \
                   + '#           #           #\n'

        self.assertEqual(solve_part_2(puzzle_input), rendered)
