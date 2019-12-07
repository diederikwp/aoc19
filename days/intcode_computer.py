class Program:
    def __init__(self, initial_mem):
        if type(initial_mem) == str:
            initial_mem = [int(i) for i in initial_mem.split(',')]

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
