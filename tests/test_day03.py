import unittest
from pathlib import Path

from days.day03 import LineSegment, Wire, parse_puzzle_input, solve_part_1, solve_part_2


class TestLineSegment(unittest.TestCase):
    def setUp(self):
        self.ls1 = LineSegment(2, 1, -2, 1)
        self.ls2 = LineSegment(2, -3, 2, 1)
        self.ls3 = LineSegment(3, -2, -1, -2)

    def test_init(self):
        self.assertEqual(self.ls1.min_x, -2)
        self.assertEqual(self.ls1.max_x, 2)
        self.assertEqual(self.ls1.min_y, 1)
        self.assertEqual(self.ls1.max_y, 1)
        self.assertEqual(self.ls1.length, 4)

    def test_intersects(self):
        self.assertFalse(self.ls1.intersects(self.ls2))
        self.assertFalse(self.ls2.intersects(self.ls1))

        self.assertFalse(self.ls1.intersects(self.ls3))
        self.assertFalse(self.ls3.intersects(self.ls1))

        self.assertTrue(self.ls2.intersects(self.ls3))
        self.assertTrue(self.ls3.intersects(self.ls2))

    def test_is_horizontal(self):
        self.assertTrue(self.ls1.is_horizontal())
        self.assertFalse(self.ls2.is_horizontal())
        self.assertTrue(self.ls3.is_horizontal())


class TestWire(unittest.TestCase):
    def setUp(self):
        self.wire1 = Wire(['R8', 'U5', 'L5', 'D3'])
        self.wire2 = Wire(['U7', 'R6', 'D4', 'L4'])
        self.wire3 = Wire(['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'])
        self.wire4 = Wire(['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83'])

    def test_line_segments(self):
        self.assertEqual(self.wire3.segments, [LineSegment(0, 0, 75, 0),
                                               LineSegment(75, 0, 75, -30),
                                               LineSegment(75, -30, 158, -30),
                                               LineSegment(158, -30, 158, 53),
                                               LineSegment(158, 53, 146, 53),
                                               LineSegment(146, 53, 146, 4),
                                               LineSegment(146, 4, 217, 4),
                                               LineSegment(217, 4, 217, 11),
                                               LineSegment(217, 11, 145, 11)])

    def test_vertices(self):
        self.assertEqual(self.wire3.vertices, [(0, 0), (75, 0), (75, -30), (158, -30), (158, 53), (146, 53), (146, 4),
                                               (217, 4), (217, 11), (145, 11)])

    def test_distance_to(self):
        self.assertEqual(self.wire3.distance_to(146, 18), 318)

    def test_intersections(self):
        intersections = {(6, 5), (3, 3)}

        self.assertEqual(self.wire1.intersections(self.wire2), intersections)
        self.assertEqual(self.wire2.intersections(self.wire1), intersections)


class TestDay03(unittest.TestCase):
    def setUp(self):
        self.test_input_1 = Path('tests/input/test_input_day03_01.txt').read_text()
        self.test_input_2 = Path('tests/input/test_input_day03_02.txt').read_text()
        self.test_input_3 = Path('tests/input/test_input_day03_03.txt').read_text()

    def test_parse_puzzle_input(self):
        puzzle_input = 'R75,D30,R83,U83,L12,D49,R71,U7,L72\n' \
                       + 'U62,R66,U55,R34,D71,R55,D58,R83'

        wire1, wire2 = parse_puzzle_input(puzzle_input)
        self.assertEqual(wire1, Wire(['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']))
        self.assertEqual(wire2, Wire(['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']))

    def test_solve_part_1_1(self):
        self.assertEqual(solve_part_1(self.test_input_1), 6)

    def test_solve_part_1_2(self):
        self.assertEqual(solve_part_1(self.test_input_2), 159)

    def test_solve_part_1_3(self):
        self.assertEqual(solve_part_1(self.test_input_3), 135)

    def test_solve_part_2_1(self):
        self.assertEqual(solve_part_2(self.test_input_1), 30)

    def test_solve_part_2_2(self):
        self.assertEqual(solve_part_2(self.test_input_2), 610)

    def test_solve_part_2_3(self):
        self.assertEqual(solve_part_2(self.test_input_3), 410)


if __name__ == '__main__':
    unittest.main()