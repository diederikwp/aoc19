import unittest
from pathlib import Path

from days.day01 import get_required_fuel
from days.day01 import solve_part_1
from days.day01 import solve_part_2


class TestDay01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_input_01 = Path('tests/input/test_input_day01_01.txt').read_text()
        cls.test_input_02 = Path('tests/input/test_input_day01_02.txt').read_text()

    # This is a bit convoluted, but apparently you are supposed to put just 1 test case in each function
    def test_required_fuel_12(self):
        self.assertEqual(get_required_fuel(12), 2)

    def test_required_fuel_14(self):
        self.assertEqual(get_required_fuel(14), 2)

    def test_required_fuel_1969(self):
        self.assertEqual(get_required_fuel(1969), 654)

    def test_required_fuel_100756(self):
        self.assertEqual(get_required_fuel(100756), 33583)

    def test_required_fuel_recursive_14(self):
        self.assertEqual(get_required_fuel(14, recursive=True), 2)

    def test_required_fuel_recursive_34(self):
        self.assertEqual(get_required_fuel(34, recursive=True), 10)

    def test_required_fuel_recursive_1969(self):
        self.assertEqual(get_required_fuel(1969, recursive=True), 966)

    def test_required_fuel_recursive_100756(self):
        self.assertEqual(get_required_fuel(100756, recursive=True), 50346)

    def test_solve_part_1(self):
        self.assertEqual(solve_part_1(self.test_input_01), 34241)

    def test_solve_part_2(self):
        self.assertEqual(solve_part_2(self.test_input_02), 51314)


if __name__ == '__main__':
    unittest.main()
