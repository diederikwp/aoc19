import math

from collections import namedtuple, defaultdict
from itertools import cycle


Direction = namedtuple('Direction', ['dx', 'dy'])


def count_num_visible(asteroids, view_point_idx):
    asteroids_by_direction = group_asteroids_by_direction(asteroids, view_point_idx)
    return len(set(asteroids_by_direction.keys()))


def find_best_asteroid(asteroids):
    max_visible = -1
    idx_max_visible = 0
    for idx in range(len(asteroids)):
        num_visible = count_num_visible(asteroids, idx)
        if num_visible > max_visible:
            max_visible = num_visible
            idx_max_visible = idx

    return max_visible, idx_max_visible


def group_asteroids_by_direction(asteroids, view_point_idx):
    x_self, y_self = asteroids[view_point_idx]
    asteroids_by_direction = defaultdict(list)

    for idx, (x_other, y_other) in enumerate(asteroids):
        if idx == view_point_idx:
            continue

        dx = x_other - x_self
        dy = y_other - y_self
        if dx == 0:
            dy = dy // abs(dy)
        elif dy == 0:
            dx = dx // abs(dx)
        else:
            div = math.gcd(dx, dy)
            dx //= div
            dy //= div

        asteroids_by_direction[Direction(dx, dy)].append(asteroids[idx])

    return asteroids_by_direction


def parse_puzzle_input(puzzle_input):
    asteroids = list()
    for y, line in enumerate(puzzle_input.splitlines()):
        pos = line.find('#', 0)
        while pos != -1:
            asteroids.append((pos, y))
            pos = line.find('#', pos + 1)

    return asteroids


def sorted_directions(directions):
    # Sort directions "clockwise" without using expensive inverse trigonometric functions. We sort primarily by
    # negativity of dx, secondarily by +/- scaled dy. The function sorted is stable, so we simply sort by the secondary
    # criterion followed by another sort on the primary criterion.
    secondary = sorted(directions, key=lambda d: d.dy / (abs(d.dx) + abs(d.dy)) * math.copysign(1, d.dx))
    return sorted(secondary, key=lambda d: d.dx < 0)


def vaporize_until_n(asteroids_by_direction, n):
    directions = sorted_directions(asteroids_by_direction.keys())

    # Iterate over remaining asteroids in clockwise order until n vaporized
    asteroids_vaporized = 0
    for i, direction in enumerate(cycle(directions)):
        revolution = i // len(directions)
        if len(asteroids_by_direction[direction]) > revolution:
            asteroids_vaporized += 1  # Only count if there are still remaining asteroids in this direction

        if asteroids_vaporized == n:
            return direction, revolution


def solve_part_1(puzzle_input):
    asteroids = parse_puzzle_input(puzzle_input)
    max_visible, _ = find_best_asteroid(asteroids)
    return max_visible


def solve_part_2(puzzle_input):
    # Find position of laser
    asteroids = parse_puzzle_input(puzzle_input)
    _, idx_laser = find_best_asteroid(asteroids)

    # Find direction of 200th vaporized asteroid, and after how many revolutions it was vaporized
    asteroids_by_direction = group_asteroids_by_direction(asteroids, idx_laser)
    direction, revolution = vaporize_until_n(asteroids_by_direction, 200)

    # Sort asteroids in direction of 200th asteroid by distance to find answer
    x_laser, y_laser = asteroids[idx_laser]
    asteroids_by_direction[direction].sort(key=lambda ast: (ast[0] - x_laser) ** 2 + (ast[1] - y_laser) ** 2)
    asteroid_answer = asteroids_by_direction[direction][revolution]
    return 100 * asteroid_answer[0] + asteroid_answer[1]

