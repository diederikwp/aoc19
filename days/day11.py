from collections import defaultdict

from days.intcode_computer import Program


class HullPaintingBot:
    def __init__(self, robot_program, starting_colour=0):
        if not isinstance(robot_program, Program):
            robot_program = Program(robot_program)
        self.program = robot_program
        self.hull = defaultdict(int)
        self.hull[(0, 0)] = starting_colour
        self.painted = set()

        self.x = 0
        self.y = 0
        self.direction = [0, 1]

    def move_forward(self):
        self.x += self.direction[0]
        self.y += self.direction[1]

    def paint(self):
        pos = (self.x, self.y)

        self.program.inputs.append(self.hull[pos])
        self.program.run()
        self.hull[pos] = self.program.outputs.popleft()
        self.painted.add(pos)

        if self.program.outputs.popleft() == 0:
            self.turn_left()
        else:
            self.turn_right()

        self.move_forward()

    def render_painting(self):
        min_x = min([pos[0] for pos in self.hull])
        max_x = max([pos[0] for pos in self.hull])
        min_y = min([pos[1] for pos in self.hull])
        max_y = max([pos[1] for pos in self.hull])

        rendered = ''
        for y in range(max_y, min_y - 1, -1):
            for x in range(min_x, max_x + 1):
                rendered += ' ' if self.hull[(x, y)] == 0 else '#'
            rendered += '\n'

        return rendered

    def run(self):
        while not self.program.halted:
            self.paint()

    def turn_left(self):
        tmp = self.direction[0]
        self.direction[0] = -self.direction[1]
        self.direction[1] = tmp

    def turn_right(self):
        tmp = self.direction[0]
        self.direction[0] = self.direction[1]
        self.direction[1] = -tmp


def solve_part_1(puzzle_input):
    bot = HullPaintingBot(puzzle_input)
    bot.run()

    return len(bot.painted)


def solve_part_2(puzzle_input):
    bot = HullPaintingBot(puzzle_input, 1)
    bot.run()

    return bot.render_painting()
