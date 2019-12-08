from copy import deepcopy
from itertools import permutations

from days.intcode_computer import Program


class AmplifierSeries:
    def __init__(self, program, num_stages, feedback_loop=False):
        if type(program) != Program:
            program = Program(program)

        self.num_stages = num_stages
        self.feedback_loop = feedback_loop

        self.programs = []
        for _ in range(num_stages):
            self.programs.append(deepcopy(program))

    def reset(self):
        for program in self.programs:
            program.reset()

    def run(self, phase_setting):
        self.reset()
        for program, phase in zip(self.programs, phase_setting):
            program.inputs.append(phase)
        self.programs[0].inputs.append(0)

        i = 0
        while self.feedback_loop or i < self.num_stages:
            if self.programs[i].halted:
                break

            self.programs[i].inputs.extend(self.programs[i - 1].outputs)
            self.programs[i - 1].outputs.clear()
            self.programs[i].run()

            i = (i + 1) % self.num_stages

        return self.programs[-1].outputs.pop()


def find_max_setting(amplifier_series, phase_settings):
    max_signal = amplifier_series.run(next(phase_settings))

    for phase_setting in phase_settings:
        signal = amplifier_series.run(phase_setting)
        if signal > max_signal:
            max_signal = signal

    return max_signal


def solve_part_1(puzzle_input):
    amp = AmplifierSeries(puzzle_input, 5)
    phase_settings = permutations([0, 1, 2, 3, 4], 5)

    return find_max_setting(amp, phase_settings)


def solve_part_2(puzzle_input):
    amp = AmplifierSeries(puzzle_input, 5, feedback_loop=True)
    phase_settings = permutations([5, 6, 7, 8, 9], 5)

    return find_max_setting(amp, phase_settings)
