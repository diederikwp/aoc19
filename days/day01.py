def get_required_fuel(mass, recursive=False):
    total_fuel = max(mass // 3 - 2, 0)

    if recursive:
        fuel = total_fuel
        while fuel > 0:
            fuel = max(fuel // 3 - 2, 0)
            total_fuel += fuel

    return total_fuel


def parse_puzzle_input(puzzle_input):
    return [int(m) for m in puzzle_input.split()]


def solve_part_1(puzzle_input):
    masses = parse_puzzle_input(puzzle_input)
    return sum([get_required_fuel(m) for m in masses])


def solve_part_2(puzzle_input):
    masses = parse_puzzle_input(puzzle_input)
    return sum([get_required_fuel(m, recursive=True) for m in masses])
