class Program:
    # Todo: explain public interface in docstring

    num_params_by_op_code = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 99: 0}
    write_params_by_op_code = {1: 2, 2: 2, 3: 0, 7: 2, 8: 2}  # e.g. param 2 (0-based) of op_code 1 is a write-address
    jump_ops = {5, 6}  # operations that mutate the instruction pointer

    def __init__(self, initial_mem):
        if type(initial_mem) == str:
            initial_mem = [int(i) for i in initial_mem.split(',')]
        self.initial_memory = initial_mem.copy()
        self.memory = initial_mem.copy()

        self.inputs = []
        self.outputs = []

        self.ip = 0  # instruction pointer
        self.halted = False

    def exec_all(self):
        while not self.halted:
            self.exec_next_op()

    def exec_next_op(self):
        op_code, params, param_modes = self.parse_next_instruction()
        vals = self.get_param_values(params, param_modes)

        if op_code == 99:
            self.halted = True
            return

        if op_code == 1:
            self.exec_op_add(*vals)
        elif op_code == 2:
            self.exec_op_mult(*vals)
        elif op_code == 3:
            self.exec_op_input(*vals)
        elif op_code == 4:
            self.exec_op_output(*vals)
        elif op_code == 5:
            self.exec_op_jump_true(*vals)
        elif op_code == 6:
            self.exec_op_jump_false(*vals)
        elif op_code == 7:
            self.exec_op_less_than(*vals)
        elif op_code == 8:
            self.exec_op_equals(*vals)

        if op_code not in self.jump_ops:
            self.ip += len(vals) + 1

    def exec_op_add(self, val1, val2, result_address):
        self.memory[result_address] = val1 + val2

    def exec_op_equals(self, val1, val2, result_address):
        self.memory[result_address] = int(val1 == val2)

    def exec_op_jump_false(self, val1, jump_address):
        if val1 == 0:
            self.ip = jump_address
        else:
            self.ip += 3

    def exec_op_jump_true(self, val1, jump_address):
        if val1 != 0:
            self.ip = jump_address
        else:
            self.ip += 3

    def exec_op_less_than(self, val1, val2, result_address):
        self.memory[result_address] = int(val1 < val2)

    def exec_op_input(self, result_address):
        self.memory[result_address] = self.inputs.pop()

    def exec_op_mult(self, val1, val2, result_address):
        self.memory[result_address] = val1 * val2

    def exec_op_output(self, val1):
        self.outputs.append(val1)

    def get_param_values(self, params, param_modes):
        vals = []
        for param, mode in zip(params, param_modes):
            if mode == 0:
                vals.append(self.memory[param])
            elif mode == 1:
                vals.append(param)

        return vals

    def parse_next_instruction(self):
        instruction = str(self.memory[self.ip]).zfill(2)  # instruction is the first val of the full instruction
        op_code = int(instruction[-2:])
        num_params = self.num_params_by_op_code[op_code]
        if num_params > 0:
            params = self.memory[self.ip + 1:self.ip + 1 + num_params]
        else:
            params = []

        instruction = str(self.memory[self.ip]).zfill(num_params + 2)
        param_modes = []
        for mode in reversed(instruction[:-2]):
            param_modes.append(int(mode))

        if op_code in self.write_params_by_op_code:
            # Param is a write address which, confusingly, is always in position mode but should actually be
            # handled in immediate mode (the param is the address itself, not the address of the memory location
            # containing the address).
            param_modes[self.write_params_by_op_code[op_code]] = 1

        return op_code, params, param_modes

    def reset(self):
        self.memory = self.initial_memory.copy()

        self.inputs = []
        self.outputs = []

        self.ip = 0
        self.halted = False

    def run(self, inputs=None):
        if inputs is None:
            inputs = []
        self.inputs = list(reversed(inputs))  # Reversed because this allows "pop"'ing the inputs
        self.exec_all()
        return self.outputs
