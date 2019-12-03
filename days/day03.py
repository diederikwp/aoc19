from collections import namedtuple


LineSegment = namedtuple('LineSegment', ['from_x', 'from_y', 'to_x', 'to_y'])


def parse_puzzle_input(puzzle_input):
    lines = puzzle_input.splitlines()
    return lines[0].split(','), lines[1].split(',')


def trace_line_segments(line_path):
    hor_segments = []
    vert_segments = []
    x = 0
    y = 0

    for step in line_path:
        direction = step[0]
        distance = int(step[1:])

        if direction == 'U':
            segment = LineSegment(from_x=x, from_y=y, to_x=x, to_y=y + distance)
            vert_segments.append(segment)
            y += distance
        elif direction == 'D':
            # Direction does not matter. Always having "from <= to" makes things easier.
            segment = LineSegment(from_x=x, from_y=y - distance, to_x=x, to_y=y)
            vert_segments.append(segment)
            y -= distance
        elif direction == 'R':
            segment = LineSegment(from_x=x, from_y=y, to_x=x + distance, to_y=y)
            hor_segments.append(segment)
            x += distance
        elif direction == 'L':
            # Direction does not matter. Always having "from <= to" makes things easier.
            segment = LineSegment(from_x=x - distance, from_y=y, to_x=x, to_y=y)
            hor_segments.append(segment)
            x -= distance

    return hor_segments, vert_segments


def find_intersections(hor_segments, vert_segments):
    # Possible performance improvement:
    #   - sort the horizontal segments by 'from_y' and the vertical segments by 'from_x'
    #   - for cur_segment in the shorter list:
    #       - find the first element in the other list just left / just below cur_segment using bisection search
    #       - start looping over the other list from here until you are just right / just above cur_segment
    #       - check for intersections in each iteration

    intersections = []
    for hor_segment in hor_segments:
        for vert_segment in vert_segments:
            if hor_segment.from_x < vert_segment.from_x < hor_segment.to_x and \
                    vert_segment.from_y < hor_segment.from_y < vert_segment.to_y:
                intersections.append((vert_segment.from_x, hor_segment.from_y))

    return intersections


def manhattan(coords):
    return [abs(c[0]) + abs(c[1]) for c in coords]


def solve_part_1(puzzle_input):
    line_paths = parse_puzzle_input(puzzle_input)
    hor_segm_1, vert_segm_1 = trace_line_segments(line_paths[0])
    hor_segm_2, vert_segm_2 = trace_line_segments(line_paths[1])

    intersections = find_intersections(hor_segm_1, vert_segm_2) + find_intersections(hor_segm_2, vert_segm_1)
    return sorted(manhattan(intersections))[0]