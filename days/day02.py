class Program:
    def __init__(self, initial_mem):
        self.initial_memory = initial_mem.copy()
        self.memory = initial_mem
        self.ip = 0  # instruction pointer
        self.halted = False

    def execute_next_op(self):
        instruction = self.memory[self.ip]
        if instruction == 99:
            self.halted = True
        else:
            pos1 = self.memory[self.ip + 1]
            pos2 = self.memory[self.ip + 2]
            dest = self.memory[self.ip + 3]

            if instruction == 1:
                self.memory[dest] = self.memory[pos1] + self.memory[pos2]
                self.ip += 4
            elif instruction == 2:
                self.memory[dest] = self.memory[pos1] * self.memory[pos2]
                self.ip += 4

    def execute_till_halted(self):
        while not self.halted:
            self.execute_next_op()

    def reset(self):
        self.memory = self.initial_memory.copy()
        self.ip = 0
        self.halted = False

    def run(self, *inputs):
        """
        Place the inputs in addresses 1 and up, execute the program till it halts, and return the memory at address 0.
        """
        self.reset()
        self.memory[1:1 + len(inputs)] = inputs
        self.execute_till_halted()
        return self.memory[0]


def parse_puzzle_input(puzzle_input):
    return [int(i) for i in puzzle_input.split(',')]


def solve_part_1(puzzle_input):
    ints = parse_puzzle_input(puzzle_input)
    program = Program(ints)

    return program.run(12, 2)


def solve_part_2(puzzle_input):
    ints = parse_puzzle_input(puzzle_input)
    program = Program(ints)

    for noun in range(100):
        for verb in range(100):
            if program.run(noun, verb) == 19690720:
                return 100 * noun + verb

