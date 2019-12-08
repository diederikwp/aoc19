from days.intcode_computer import Program


def solve_part_1(puzzle_input):
    program = Program(puzzle_input)
    out = program.run([1])
    return out[-1]


def solve_part_2(puzzle_input):
    program = Program(puzzle_input)
    out = program.run([5])
    return out[0]
