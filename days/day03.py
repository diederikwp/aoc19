def parse_puzzle_input(puzzle_input):
    lines = puzzle_input.splitlines()
    return Wire(lines[0].split(',')), Wire(lines[1].split(','))


class LineSegment:
    def __init__(self, from_x, from_y, to_x, to_y):
        self.from_x = from_x
        self.to_x = to_x
        self.from_y = from_y
        self.to_y = to_y

        self.min_x = min(from_x, to_x)
        self.max_x = max(from_x, to_x)
        self.min_y = min(from_y, to_y)
        self.max_y = max(from_y, to_y)

        self.length = self.max_x - self.min_x + self.max_y - self.min_y

    def __eq__(self, other):
        return self.from_x == other.from_x and self.to_x == other.to_x and self.from_y == other.from_y

    def __repr__(self):
        return f'LineSegment from ({self.from_x}, {self.from_y}) to ({self.to_x}, {self.to_y})'

    def intersects(self, other):
        if self.min_x >= other.max_x:
            return False
        if self.max_x <= other.min_x:
            return False
        if self.min_y >= other.max_y:
            return False
        if self.max_y <= other.min_y:
            return False

        return True

    def is_horizontal(self):
        return self.from_y == self.to_y


class Wire:
    def __init__(self, path_description):
        self.vertices = [(0, 0)]
        self.segments = []

        x = 0
        y = 0
        total_distance = 0
        for step in path_description:
            direction = step[0]
            distance = int(step[1:])

            if direction == 'U':
                self.segments.append(LineSegment(from_x=x, from_y=y, to_x=x, to_y=y + distance))
                y += distance
            elif direction == 'D':
                self.segments.append(LineSegment(from_x=x, from_y=y, to_x=x, to_y=y - distance))
                y -= distance
            elif direction == 'R':
                self.segments.append(LineSegment(from_x=x, from_y=y, to_x=x + distance, to_y=y))
                x += distance
            elif direction == 'L':
                self.segments.append(LineSegment(from_x=x, from_y=y, to_x=x - distance, to_y=y))
                x -= distance

            self.vertices.append((x, y))
            total_distance += distance

    def __eq__(self, other):
        return self.vertices == other.vertices and self.segments == other.segments

    def distance_to(self, x, y):
        distance = 0
        for seg in self.segments:
            if seg.is_horizontal():
                if y == seg.from_y and seg.min_x <= x <= seg.max_x:
                    return distance + abs(x - seg.from_x)
            else:
                if x == seg.from_x and seg.min_y <= y <= seg.max_y:
                    return distance + abs(y - seg.from_y)

            distance += seg.length

        return None

    def intersections(self, other):
        # This takes O(nm) time, where n is number of self segments and m is number of other segments. Performance can
        # be improved by sorting horizontal segments by 'from_y' and vertical segments by 'from_x'. Sorting will take
        # O(n log(n)). Then a list of other segments that might intersect can be found using bisection search, in
        # O(log (n)).
        crossings = set()
        for ss in self.segments:
            for os in other.segments:
                if ss.intersects(os):
                    if ss.is_horizontal():
                        crossings.add((os.from_x, ss.from_y))
                    else:
                        crossings.add((ss.from_x, os.from_y))

        return crossings


def solve_part_1(puzzle_input):
    wire_1, wire_2 = parse_puzzle_input(puzzle_input)

    intersections = wire_1.intersections(wire_2)
    return min([abs(x) + abs(y) for x, y in intersections])


def solve_part_2(puzzle_input):
    wire_1, wire_2 = parse_puzzle_input(puzzle_input)

    intersections = wire_1.intersections(wire_2)
    return min([wire_1.distance_to(x, y) + wire_2.distance_to(x, y) for x, y in intersections])
