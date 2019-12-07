import unittest

from days.day02 import run_program
from days.intcode_computer import Program


class TestDay02(unittest.TestCase):
    def test_run_program(self):
        program = Program([1, 0, 0, 4, 99, 5, 6, 0, 99])
        self.assertEqual(run_program(program, 1, 1), 30)


if __name__ == '__main__':
    unittest.main()
