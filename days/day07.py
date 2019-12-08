from itertools import permutations

from days.intcode_computer import Program


class AmplifierSeries:
    def __init__(self, program, num_stages):
        if type(program) == Program:
            self.program = program
        else:
            self.program = Program(program)

        self.num_stages = num_stages

    def run(self, phase_setting):
        piped_value = 0
        for i in range(self.num_stages):
            self.program.reset()
            piped_value = self.program.run([phase_setting[i], piped_value])[0]

        return piped_value


def solve_part_1(puzzle_input):
    amp = AmplifierSeries(puzzle_input, 5)
    phase_settings = permutations([0, 1, 2, 3, 4], 5)
    max_signal = amp.run(next(phase_settings))

    for phase_setting in phase_settings:
        signal = amp.run(phase_setting)
        if signal > max_signal:
            max_signal = signal

    return max_signal
