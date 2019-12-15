import unittest
from unittest.mock import Mock, PropertyMock
from collections import deque

from days.day11 import HullPaintingBot
from days.intcode_computer import Program


class TestDay11(unittest.TestCase):
    def test_hull_painting_bot(self):
        # Mock the example program from the puzzle description
        program = Mock(spec=Program('0,1,2,3'))
        program.outputs = deque([1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0])
        program.inputs = deque()
        halted_values = [False] * 7 + [True]
        type(program).halted = PropertyMock(side_effect=halted_values)

        bot = HullPaintingBot(program)
        bot.run()

        self.assertEqual(program.inputs, deque([0, 0, 0, 0, 1, 0, 0]))
        self.assertEqual(bot.hull, {(0, 0): 0,
                                    (-1, 0): 0,
                                    (-1, -1): 1,
                                    (0, -1): 1,
                                    (1, 0): 1,
                                    (1, 1): 1})
        self.assertEqual(bot.painted, {(0, 0), (-1, 0), (-1, -1), (0, -1), (1, 0), (1, 1)})
