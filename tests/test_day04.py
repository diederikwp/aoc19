import unittest

from days.day04 import contains_two_adjacent, contains_exactly_two_adjacent, non_decreasing_digits, num_to_digits,\
                       solve_part_1, solve_part_2


class TestDay04(unittest.TestCase):
    def test_contains_2_adjacent(self):
        self.assertTrue(contains_two_adjacent([1, 1, 1, 1, 1, 1]))
        self.assertTrue(contains_two_adjacent([2, 2, 3, 4, 5, 0]))
        self.assertFalse(contains_two_adjacent([1, 2, 3, 7, 8, 9]))

    def test_contains_exactly_2_adjacent(self):
        self.assertTrue(contains_exactly_two_adjacent([1, 1, 2, 2, 3, 3]))
        self.assertFalse(contains_exactly_two_adjacent([1, 2, 3, 4, 4, 4]))
        self.assertTrue(contains_exactly_two_adjacent([1, 1, 1, 1, 2, 2]))
        self.assertFalse(contains_exactly_two_adjacent([1, 2, 3, 4, 5, 2]))

    def test_non_decreasing_digits(self):
        digit_range = non_decreasing_digits(234548, 234568)
        self.assertEqual(list(digit_range), [[2, 3, 4, 5, 5, 8],
                                             [2, 3, 4, 5, 5, 9],
                                             [2, 3, 4, 5, 6, 6],
                                             [2, 3, 4, 5, 6, 7],
                                             [2, 3, 4, 5, 6, 8]])

    def test_num_to_digits(self):
        self.assertEqual(num_to_digits(111111), [1, 1, 1, 1, 1, 1])
        self.assertEqual(num_to_digits(223450), [2, 2, 3, 4, 5, 0])
        self.assertEqual(num_to_digits(123789), [1, 2, 3, 7, 8, 9])

    def test_solve_part_1(self):
        self.assertEqual(solve_part_1('234545-234568'), 6)
        # valid: 234555, 234556, 234557, 234558, 234559, 234566

    def test_solve_part_2(self):
        self.assertEqual(solve_part_2('234545-234568'), 5)
        # valid: 234556, 234557, 234558, 234559, 234566


if __name__ == '__main___':
    unittest.main()
