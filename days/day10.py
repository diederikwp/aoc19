import math

from collections import namedtuple


Direction = namedtuple('Direction', ['dx', 'dy'])


def parse_puzzle_input(puzzle_input):
    asteroids = list()
    for y, line in enumerate(puzzle_input.splitlines()):
        pos = line.find('#', 0)
        while pos != -1:
            asteroids.append((pos, y))
            pos = line.find('#', pos + 1)

    return asteroids


def count_num_visible(asteroids, view_point_idx):
    x_self, y_self = asteroids[view_point_idx]
    directions = set()

    for idx, (x_other, y_other) in enumerate(asteroids):
        if idx == view_point_idx:
            continue

        dx = x_self - x_other
        dy = y_self - y_other
        if dx == 0:
            dy = dy // abs(dy)
        elif dy == 0:
            dx = dx // abs(dx)
        else:
            div = math.gcd(dx, dy)
            dx //= div
            dy //= div

        directions.add(Direction(dx, dy))

    return len(directions)


def solve_part_1(puzzle_input):
    asteroids = parse_puzzle_input(puzzle_input)
    max_visible = 0
    for idx in range(len(asteroids)):
        max_visible = max(count_num_visible(asteroids, idx), max_visible)

    return max_visible
