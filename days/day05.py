from days.intcode_computer import Program


def solve_part_1(puzzle_input):
    program = Program(puzzle_input)
    program.inputs.append(1)
    program.run()
    return program.outputs.pop()


def solve_part_2(puzzle_input):
    program = Program(puzzle_input)
    program.inputs.append(5)
    program.run()
    return program.outputs.pop()
