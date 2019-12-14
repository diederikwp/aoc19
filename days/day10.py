import math

from collections import namedtuple, defaultdict


Direction = namedtuple('Direction', ['dx', 'dy'])


def parse_puzzle_input(puzzle_input):
    asteroids = list()
    for y, line in enumerate(puzzle_input.splitlines()):
        pos = line.find('#', 0)
        while pos != -1:
            asteroids.append((pos, y))
            pos = line.find('#', pos + 1)

    return asteroids


def map_asteroids_to_direction(asteroids, view_point_idx):
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


def find_best_asteroid(asteroids):
    max_visible = -1
    idx_max_visible = 0
    for idx in range(len(asteroids)):
        num_visible = count_num_visible(asteroids, idx)
        if num_visible > max_visible:
            max_visible = num_visible
            idx_max_visible = idx

    return max_visible, idx_max_visible


def count_num_visible(asteroids, view_point_idx):
    asteroids_by_direction = map_asteroids_to_direction(asteroids, view_point_idx)
    return len(set(asteroids_by_direction.keys()))


def solve_part_1(puzzle_input):
    asteroids = parse_puzzle_input(puzzle_input)
    max_visible, _ = find_best_asteroid(asteroids)
    return max_visible


def solve_part_2(puzzle_input):
    asteroids = parse_puzzle_input(puzzle_input)
    _, idx_laser = find_best_asteroid(asteroids)
    asteroids_by_direction = map_asteroids_to_direction(asteroids, idx_laser)

    # Sort directions "clockwise" without using expensive inverse trigonometric functions. We sort primarily by
    # negativity of dx, secondarily by +/- scaled dy. The function sorted is stable, so we simply sort by the secondary
    # criterion followed by another sort on the primary criterion.
    sorted_directions = sorted(asteroids_by_direction,
                               key=lambda d: d.dy / (abs(d.dx) + abs(d.dy)) * math.copysign(1, d.dx))
    sorted_directions = sorted(sorted_directions, key=lambda d: d.dx < 0)

    # Iterate over remaining asteroids in clockwise order until 200 vaporized
    i = -1
    revolution = 0
    asteroids_vaporized = 0
    direction = None
    while asteroids_vaporized < 200:
        i = (i + 1) % len(sorted_directions)
        revolution = i // len(sorted_directions)
        direction = sorted_directions[i]

        if len(asteroids_by_direction[direction]) > revolution:
            asteroids_vaporized += 1  # Only count if there are still remaining asteroids in this direction

    # Direction of 200th asteroid is now known; sort asteroids in that direction by distance to find answer
    x_laser, y_laser = asteroids[idx_laser]
    asteroids_by_direction[direction].sort(key=lambda ast: (ast[0] - x_laser) ** 2 + (ast[1] - y_laser) ** 2)
    asteroid_answer = asteroids_by_direction[direction][revolution]
    return 100 * asteroid_answer[0] + asteroid_answer[1]

