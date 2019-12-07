import unittest

from days.intcode_computer import Program


class TestProgram(unittest.TestCase):
    def test_exec_till_halt_1(self):
        program = Program([1, 0, 0, 0, 99])
        program.execute_till_halted()
        self.assertEqual(program.memory, [2, 0, 0, 0, 99])

    def test_exec_till_halt_2(self):
        program = Program([2, 3, 0, 3, 99])
        program.execute_till_halted()
        self.assertEqual(program.memory, [2, 3, 0, 6, 99])

    def test_exec_till_halt_3(self):
        program = Program([2, 4, 4, 5, 99, 0])
        program.execute_till_halted()
        self.assertEqual(program.memory, [2, 4, 4, 5, 99, 9801])

    def test_exec_till_halt_4(self):
        program = Program([1, 1, 1, 4, 99, 5, 6, 0, 99])
        program.execute_till_halted()
        self.assertEqual(program.memory, [30, 1, 1, 4, 2, 5, 6, 0, 99])

    def test_reset(self):
        ints = [2, 4, 4, 5, 99, 0]
        program = Program(ints.copy())
        program.execute_next_op()
        self.assertNotEqual(program.ip, 0)
        self.assertNotEqual(program.memory, ints)
        program.reset()
        self.assertEqual(program.memory, ints)
        self.assertEqual(program.ip, 0)


if __name__ == '__main__':
    unittest.main()
