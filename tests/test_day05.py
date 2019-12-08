import unittest

from days.day05 import solve_part_1, solve_part_2


class TestDay05(unittest.TestCase):
    def test_solve_part_1(self):
        self.assertEqual(solve_part_1('3,0,4,0,104,1337,99'), 1337)

    def test_solve_part_2(self):
        self.assertEqual(solve_part_2('3,0,4,0,99'), 5)


if __name__ == '__main__':
    unittest.main()
