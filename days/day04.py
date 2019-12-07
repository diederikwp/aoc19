from collections import Counter


def parse_puzzle_input(puzzle_input):
    lower, upper = puzzle_input.split('-')
    return int(lower), int(upper)


def num_to_digits(num):
    return [int(i) for i in str(num)]  # No need to consider leading zero's in this puzzle


def non_decreasing_digits(start, end):
    """Efficiently generate lists of non-decreasing digits, between integers start and end (inclusive)"""
    n = start
    while True:
        digits = num_to_digits(n)

        for idx in range(1, len(digits)):
            diff = digits[idx - 1] - digits[idx]
            if diff > 0:
                n += diff * 10 ** (len(digits) - idx - 1)
                digits[idx] = digits[idx - 1]

        if n > end:
            break

        yield digits
        n += 1


def contains_two_adjacent(digits):
    for idx in range(1, len(digits)):
        if digits[idx] == digits[idx - 1]:
            return True

    return False


def contains_exactly_two_adjacent(digits):
    return contains_two_adjacent(digits) and 2 in Counter(digits).values()


def solve_puzzle_part(puzzle_input, validation_fun):
    lower_limit, upper_limit = parse_puzzle_input(puzzle_input)

    # From the description it is not clear whether the limits should be inclusive or exclusive. I assume inclusive.
    digits_range = non_decreasing_digits(lower_limit, upper_limit)

    num_valid = 0
    for digits in digits_range:
        if validation_fun(digits):
            num_valid += 1

    return num_valid


def solve_part_1(puzzle_input):
    return solve_puzzle_part(puzzle_input, contains_two_adjacent)


def solve_part_2(puzzle_input):
    return solve_puzzle_part(puzzle_input, contains_exactly_two_adjacent)
