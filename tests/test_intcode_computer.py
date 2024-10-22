import unittest
from collections import deque

from days.intcode_computer import InfiniteList, Program


class TestProgram(unittest.TestCase):
    def test_prog_1(self):
        # addition
        program = Program([1, 0, 0, 0, 99])
        program.run()
        self.assertEqual(program.memory, [2, 0, 0, 0, 99])

    def test_prog_2(self):
        # multiplication
        program = Program([2, 3, 0, 3, 99])
        program.run()
        self.assertEqual(program.memory, [2, 3, 0, 6, 99])

    def test_prog_3(self):
        # multiplication, input as string
        program = Program('2,4,4,5,99,0')
        program.run()
        self.assertEqual(program.memory, [2, 4, 4, 5, 99, 9801])

    def test_prog_4(self):
        # multiplication and addition
        program = Program([1, 1, 1, 4, 99, 5, 6, 0, 99])
        program.run()
        self.assertEqual(program.memory, [30, 1, 1, 4, 2, 5, 6, 0, 99])

    def test_prog_5(self):
        # immediate mode
        program = Program('1002,4,3,4,33')
        program.run()
        self.assertEqual(program.memory, [1002, 4, 3, 4, 99])

    def test_prog_6(self):
        # immediate mode
        program = Program('102,3,4,4,33')
        program.run()
        self.assertEqual(program.memory, [102, 3, 4, 4, 99])

    def test_prog_7(self):
        # input
        program = Program([3, 2, 0, 4, 0])
        program.inputs.extend([3, 99])
        program.run()
        self.assertEqual(program.outputs, deque())
        self.assertEqual(program.memory, [3, 2, 3, 4, 99])

    def test_prog_8(self):
        # output
        program = Program([101, -93, 0, 5, 4, -1, 4, 0, 99])
        program.run()
        self.assertEqual(list(program.outputs), [99, 101])
        self.assertEqual(program.memory, [101, -93, 0, 5, 4, 8, 4, 0, 99])

    def test_prog_9(self):
        # input and output
        program = Program('3,0,4,0,99')
        program.inputs.append(1337)
        program.run()
        self.assertEqual(list(program.outputs), [1337])

    def test_prog_10(self):
        # equals, position mode. Program tests whether input equals 8.
        program = Program('3,9,8,9,10,9,4,9,99,-1,8')

        program.inputs.append(8)
        program.run()
        self.assertEqual(list(program.outputs), [1])

        program.reset()
        program.inputs.append(-8)
        program.run()
        self.assertEqual(list(program.outputs), [0])

        program.reset()
        program.inputs.append(4)
        program.run()
        self.assertEqual(list(program.outputs), [0])

        program.reset()
        program.inputs.append(40)
        program.run()
        self.assertEqual(list(program.outputs), [0])

    def test_prog_11(self):
        # equals, immediate mode. Program tests whether input equals 8.
        program = Program('3,3,1108,-1,8,3,4,3,99')

        program.inputs.append(8)
        program.run()
        self.assertEqual(list(program.outputs), [1])

        program.reset()
        program.inputs.append(-8)
        program.run()
        self.assertEqual(list(program.outputs), [0])

        program.reset()
        program.inputs.append(4)
        program.run()
        self.assertEqual(list(program.outputs), [0])

        program.reset()
        program.inputs.append(40)
        program.run()
        self.assertEqual(list(program.outputs), [0])

    def test_prog_12(self):
        # less than, position mode. Program tests whether input is less than 8.
        program = Program('3,9,7,9,10,9,4,9,99,-1,8')

        program.inputs.append(7)
        program.run()
        self.assertEqual(list(program.outputs), [1])

        program.reset()
        program.inputs.append(6)
        program.run()
        self.assertEqual(list(program.outputs), [1])

        program.reset()
        program.inputs.append(-11)
        program.run()
        self.assertEqual(list(program.outputs), [1])

        program.reset()
        program.inputs.append(8)
        program.run()
        self.assertEqual(list(program.outputs), [0])

        program.reset()
        program.inputs.append(60)
        program.run()
        self.assertEqual(list(program.outputs), [0])

    def test_prog_13(self):
        # less than, immediate mode. Program tests whether input is less than 8.
        program = Program('3,3,1107,-1,8,3,4,3,99')

        program.inputs.append(7)
        program.run()
        self.assertEqual(list(program.outputs), [1])

        program.reset()
        program.inputs.append(6)
        program.run()
        self.assertEqual(list(program.outputs), [1])

        program.reset()
        program.inputs.append(-11)
        program.run()
        self.assertEqual(list(program.outputs), [1])

        program.reset()
        program.inputs.append(8)
        program.run()
        self.assertEqual(list(program.outputs), [0])

        program.reset()
        program.inputs.append(60)
        program.run()
        self.assertEqual(list(program.outputs), [0])

    def test_prog_14(self):
        # jumps, position mode. Program tests whether input is nonzero
        program = Program('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9')

        program.inputs.append(0)
        program.run()
        self.assertEqual(list(program.outputs), [0])

        program.reset()
        program.inputs.append(1)
        program.run()
        self.assertEqual(list(program.outputs), [1])

        program.reset()
        program.inputs.append(-1)
        program.run()
        self.assertEqual(list(program.outputs), [1])

    def test_prog_15(self):
        # jumps, immediate mode. Program tests whether input is nonzero
        program = Program('3,3,1105,-1,9,1101,0,0,12,4,12,99,1')

        program.inputs.append(0)
        program.run()
        self.assertEqual(list(program.outputs), [0])

        program.reset()
        program.inputs.append(1)
        program.run()
        self.assertEqual(list(program.outputs), [1])

        program.reset()
        program.inputs.append(-1)
        program.run()
        self.assertEqual(list(program.outputs), [1])

    def test_prog_16(self):
        # slightly larger test of opcodes 1--8, 99. Program outputs 999 if input is below 8, 1000 if input equals 8 and
        # 1001 if input is greater than 8.
        program = Program('3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,'
                          '1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,'
                          '999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99')

        program.inputs.append(0)
        program.run()
        self.assertEqual(list(program.outputs), [999])

        program.reset()
        program.inputs.append(7)
        program.run()
        self.assertEqual(list(program.outputs), [999])

        program.reset()
        program.inputs.append(8)
        program.run()
        self.assertEqual(list(program.outputs), [1000])

        program.reset()
        program.inputs.append(9)
        program.run()
        self.assertEqual(list(program.outputs), [1001])

        program.reset()
        program.inputs.append(70)
        program.run()
        self.assertEqual(list(program.outputs), [1001])

    def test_prog_17(self):
        # multiple inputs, not all at once
        program = Program([3, 5, 3, 6, 1102, -1, -1, 9, 104, -1, 3, 11, 1, 11, 0, 17, 4, -1, 99])

        program.inputs.extend([2, 10])
        program.run()
        self.assertEqual(list(program.outputs), [20])
        self.assertFalse(program.halted)
        self.assertEqual(program.inputs, deque())

        program.inputs.append(5)
        program.run()
        self.assertEqual(list(program.outputs), [20, 104])
        self.assertTrue(program.halted)
        self.assertEqual(program.inputs, deque())

    def test_prog_18(self):
        # relative mode and expanding memory beyond initial size
        program = Program('109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99')
        program.run()
        self.assertEqual(list(program.outputs),
                         [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0,  99])

    def test_prog_19(self):
        # Big ints
        program = Program('1102,34915192,34915192,7,4,7,99,0')
        program.run()
        self.assertEqual(len(program.outputs), 1)
        self.assertEqual(len(str(program.outputs[0])), 16)  # day 9 "should output a 16-digit number"

    def test_prog_20(self):
        # Big ints
        program = Program('104,1125899906842624,99')
        program.run()
        self.assertEqual(len(program.outputs), 1)
        self.assertEqual(program.outputs[0], 1125899906842624)

    def test_reset(self):
        ints = [109, -3, 2002, 6, 9, 7, 99, 0]
        program = Program(ints)
        program.run()
        self.assertNotEqual(program.ip, 0)
        self.assertNotEqual(program.memory, ints)
        program.reset()
        self.assertEqual(program.memory, ints)
        self.assertEqual(program.ip, 0)
        program.run()
        self.assertNotEqual(program.ip, 0)
        self.assertEqual(program.memory, [109, -3, 2002, 6, 9, 7, 99, 9801])


class TestInfiniteList(unittest.TestCase):
    def test_getitem(self):
        il = InfiniteList([1, 2, 3])

        # Before expanding
        self.assertEqual(il[0], 1)
        self.assertEqual(il[1], 2)
        self.assertEqual(il[2], 3)

        # Expand with integer key
        self.assertEqual(il[5], 0)
        self.assertEqual(il[8], 0)
        self.assertEqual(il, [1, 2, 3, 0, 0, 0, 0, 0, 0])

        # Expand with slice key
        self.assertEqual(il[2:10], [3, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(il[5:8], [0, 0, 0])
        self.assertEqual(il, [1, 2, 3, 0, 0, 0, 0, 0, 0, 0])

    def test_setitem(self):
        il = InfiniteList([1, 2, 3])

        il[1] = 4
        self.assertEqual(il, [1, 4, 3])

        il[5] = -1
        self.assertEqual(il, [1, 4, 3, 0, 0, -1])

        il[4:7] = [10, 11, 12]
        self.assertEqual(il, [1, 4, 3, 0, 10, 11, 12])

    def test_insert(self):
        il = InfiniteList([1, 2, 3])

        il.insert(0, 9)
        il.insert(2, 9)
        il.insert(5, 9)
        self.assertEqual(il, [9, 1, 9, 2, 3, 9])

        il.insert(7, 7)
        self.assertEqual(il, [9, 1, 9, 2, 3, 9, 0, 7])

    def test_iter(self):
        il = InfiniteList([1, 2, 3])
        self.assertEqual([i for i in il], [1, 2, 3])

        il[5] = 5
        self.assertEqual([i for i in il], [1, 2, 3, 0, 0, 5])

    def test_negative_key(self):
        il = InfiniteList([1, 2, 3])

        with self.assertRaises(IndexError):
            il[-1]
        with self.assertRaises(IndexError):
            il[0:-1]
        with self.assertRaises(IndexError):
            il[-3:-1]
        with self.assertRaises(IndexError):
            il[-3:0]
        with self.assertRaises(IndexError):
            il[-2] = 0
        with self.assertRaises(IndexError):
            il[0:-1] = [10, 11]
        with self.assertRaises(IndexError):
            il.insert(-2, 0)


if __name__ == '__main__':
    unittest.main()
