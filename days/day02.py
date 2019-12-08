from days.intcode_computer import Program


def run_program(program, input1, input2):
    # In day 2 we don't yet make use of the intcode computer's native I/O system, but we input 2 numbers at
    # memory locations 1 and 2 instead, and read the output from location 0

    program.memory[1] = input1
    program.memory[2] = input2
    program.exec_all()
    return program.memory[0]


def solve_part_1(puzzle_input):
    program = Program(puzzle_input)

    return run_program(program, 12, 2)


def solve_part_2(puzzle_input):
    program = Program(puzzle_input)

    for noun in range(100):
        for verb in range(100):
            program.reset()
            if run_program(program, noun, verb) == 19690720:
                return 100 * noun + verb

