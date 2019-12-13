from collections import UserList, deque


class Program:
    # Todo: explain public interface in docstring

    num_params_by_op_code = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1, 99: 0}
    write_params_by_op_code = {1: 2, 2: 2, 3: 0, 7: 2, 8: 2}  # e.g. param 2 (0-based) of op_code 1 is a write-address
    jump_ops = {5, 6}  # operations that mutate the instruction pointer

    def __init__(self, initial_mem):
        if isinstance(initial_mem, str):
            initial_mem = [int(i) for i in initial_mem.split(',')]

        initial_mem = InfiniteList(initial_mem)
        self.initial_memory = initial_mem.copy()
        self.memory = initial_mem.copy()

        self.inputs = deque()
        self.outputs = deque()

        self.ip = 0  # instruction pointer
        self.relative_base = 0
        self.halted = False

    def exec_all(self):
        while not self.halted:
            self.exec_next_op()

    def exec_next_op(self):
        op_code, params, param_modes, dereference = self.parse_next_instruction()
        vals = self.get_param_values(params, param_modes, dereference)

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
        elif op_code == 9:
            self.exec_op_adjust_relative_base(*vals)

        if op_code not in self.jump_ops:
            self.ip += len(vals) + 1

    def exec_op_add(self, val1, val2, result_address):
        self.memory[result_address] = val1 + val2

    def exec_op_adjust_relative_base(self, delta):
        self.relative_base += delta

    def exec_op_equals(self, val1, val2, result_address):
        self.memory[result_address] = int(val1 == val2)

    def exec_op_input(self, result_address):
        if not self.inputs:
            raise InputRequiredError

        self.memory[result_address] = self.inputs.popleft()

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

    def exec_op_mult(self, val1, val2, result_address):
        self.memory[result_address] = val1 * val2

    def exec_op_output(self, val1):
        self.outputs.append(val1)

    def get_param_values(self, params, param_modes, dereference):
        vals = []
        for param, mode, deref in zip(params, param_modes, dereference):
            if mode == 0:
                vals.append(self.memory[param]) if deref else vals.append(param)
            elif mode == 1:
                vals.append(param)
            elif mode == 2:
                vals.append(self.memory[self.relative_base + param]) if deref \
                    else vals.append(self.relative_base + param)

        return vals

    def parse_next_instruction(self):
        instruction = str(self.memory[self.ip]).zfill(2)  # instruction is the first int of the full instruction
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

        dereference = [True] * len(param_modes)
        if op_code in self.write_params_by_op_code:
            # Params representing write addresses are special cases. They are never in immediate mode, and when they
            # are in relative or position mode, they should not be dereferenced but interpreted as an address. For
            # example, the parameter 5 in position mode (mode 0), normally means "the value at address 5", but when
            # the parameter is a write address, it means "the address 5".
            dereference[self.write_params_by_op_code[op_code]] = False

        return op_code, params, param_modes, dereference

    def reset(self):
        self.memory = self.initial_memory.copy()

        self.inputs = deque()
        self.outputs = deque()

        self.ip = 0
        self.relative_base = 0
        self.halted = False

    def run(self):
        try:
            self.exec_all()
        except InputRequiredError:
            pass  # We simply return in non-halted state. Continue by calling run again after supplying more inputs

        return


class InfiniteList(UserList):
    """List that expands itself with zeros whenever an item beyond the end of the list is accessed"""
    def __iter__(self):
        return self.data.__iter__()  # Prevents infinite iterator

    def __getitem__(self, key):
        self._check_key(key)
        self._expand(key)
        return self.data.__getitem__(key)

    def __setitem__(self, key, value):
        self._check_key(key)
        self._expand(key)
        return self.data.__setitem__(key, value)

    @staticmethod
    def _check_key(key):
        if isinstance(key, slice):
            if key.start >= 0 and key.stop >= 0:
                return
        elif key >= 0:
            return

        # Negative indices make no sense since an InfiniteList has no end. Allowing this would be confusing.
        raise IndexError("Negative indices are not allowed in an InfiniteList")

    def _expand(self, key):
        if isinstance(key, slice):
            limit = key.stop - 1
        else:
            limit = key

        if limit >= len(self.data):
            self.data += [0] * (limit - len(self.data) + 1)

    def insert(self, i, item):
        self._check_key(i)

        if i > len(self.data):
            self.__setitem__(i, item)
        else:
            self.data.insert(i, item)


class InputRequiredError(Exception):
    pass
