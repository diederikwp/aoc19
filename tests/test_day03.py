import unittest
from pathlib import Path

from days.day03 import LineSegment, parse_puzzle_input, trace_line_segments, find_intersections, solve_part_1


class TestDay03(unittest.TestCase):
    def test_parse_puzzle_input(self):
        puzzle_input = 'R75,D30,R83,U83,L12,D49,R71,U7,L72\n' \
                       + 'U62,R66,U55,R34,D71,R55,D58,R83'

        parsed1, parsed2 = parse_puzzle_input(puzzle_input)
        self.assertEqual(parsed1, ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'])
        self.assertEqual(parsed2, ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83'])

    def test_trace_line_segments(self):
        segments_hor, segments_vert = trace_line_segments(['U62', 'R66', 'U55', 'R34', 'D71', 'L55', 'D58', 'R83'])

        self.assertEqual(segments_vert, [LineSegment(0, 0, 0, 62),
                                         LineSegment(66, 62, 66, 117),
                                         LineSegment(100, 46, 100, 117),
                                         LineSegment(45, -12, 45, 46)])

        self.assertEqual(segments_hor, [LineSegment(0, 62, 66, 62),
                                        LineSegment(66, 117, 100, 117),
                                        LineSegment(45, 46, 100, 46),
                                        LineSegment(45, -12, 128, -12)])

    def test_find_intersections(self):
        hor_segments = [LineSegment(0, 0, 8, 0), LineSegment(3, 5, 8, 5)]
        vert_segments = [LineSegment(0, 0, 0, 7), LineSegment(6, 3, 6, 7)]

        self.assertEqual(find_intersections(hor_segments, vert_segments), [(6, 5)])

    def test_solve_part_1_1(self):
        test_input_1 = Path('tests/input/test_input_day03_01.txt').read_text()
        self.assertEqual(solve_part_1(test_input_1), 6)

    def test_solve_part_1_2(self):
        test_input_1 = Path('tests/input/test_input_day03_02.txt').read_text()
        self.assertEqual(solve_part_1(test_input_1), 159)

    def test_solve_part_1_3(self):
        test_input_1 = Path('tests/input/test_input_day03_03.txt').read_text()
        self.assertEqual(solve_part_1(test_input_1), 135)


if __name__ == '__main__':
    unittest.main()