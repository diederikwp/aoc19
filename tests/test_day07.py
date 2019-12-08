import unittest

from days.day07 import AmplifierSeries, solve_part_1
from days.intcode_computer import Program


class TestAmplifierSeries(unittest.TestCase):
    def setUp(self):
        self.input_program_1 = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
        self.input_program_2 = '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'
        self.input_program_3 = '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,' \
                               '31,4,31,99,0,0,0'

    def test_prog_1(self):
        program = Program(self.input_program_1)
        amp = AmplifierSeries(program, 5)
        self.assertEqual(amp.run([4, 3, 2, 1, 0]), 43210)

    def test_prog_2(self):
        program = Program(self.input_program_2)
        amp = AmplifierSeries(program, 5)
        self.assertEqual(amp.run([0, 1, 2, 3, 4]), 54321)

    def test_prog_3(self):
        program = Program(self.input_program_3)
        amp = AmplifierSeries(program, 5)
        self.assertEqual(amp.run([1, 0, 4, 3, 2]), 65210)


class TestDay07(unittest.TestCase):
    def setUp(self):
        self.input_program_1 = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
        self.input_program_2 = '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'
        self.input_program_3 = '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,' \
                               '31,4,31,99,0,0,0'

    def test_solve_part_1(self):
        self.assertEqual(solve_part_1(self.input_program_1), 43210)
        self.assertEqual(solve_part_1(self.input_program_2), 54321)
        self.assertEqual(solve_part_1(self.input_program_3), 65210)

