def get_required_fuel(mass, recursive=False):
    fuel = mass // 3 - 2
    fuel = 0 if fuel < 0 else fuel

    if fuel == 0 or not recursive:
        return fuel

    return fuel + get_required_fuel(fuel, recursive)


def parse_puzzle_input(puzzle_input):
    return [int(m) for m in puzzle_input.split()]


def solve_part_1(puzzle_input):
    masses = parse_puzzle_input(puzzle_input)
    return sum([get_required_fuel(m) for m in masses])


def solve_part_2(puzzle_input):
    masses = parse_puzzle_input(puzzle_input)
    return sum([get_required_fuel(m, recursive=True) for m in masses])
