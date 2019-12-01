import unittest
from days.day01 import solve_part_1


class TestDay01(unittest.TestCase):
    def test_me(self):
        self.assertEqual(1, 1)

    def test_me_some_more(self):
        solve_part_1('my_input')
        self.assertTrue(1 == 1)


if __name__ == '__main__':
    unittest.main()
