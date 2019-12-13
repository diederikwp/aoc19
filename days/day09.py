from days.intcode_computer import Program


def solve_part(puzzle_input, input_val):
    program = Program(puzzle_input)
    program.inputs.append(input_val)
    program.run()
    return program.outputs.pop()


def solve_part_1(puzzle_input):
    return solve_part(puzzle_input, 1)


def solve_part_2(puzzle_input):
    return solve_part(puzzle_input, 2)
