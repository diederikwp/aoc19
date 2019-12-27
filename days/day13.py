import curses
import time

from days.intcode_computer import Program


class BreakoutGame:
    tile_chars = {0: ' ', 1: '@', 2: '#', 3: '_', 4: 'O'}

    def __init__(self, program):
        self.program = program
        self.tiles = dict()
        self.score = 0
        self.window = None
        self.fps = None
        self.prev_frame_time = None

        self.ball_x = None
        self.ball_y = None
        self.paddle_x = None

    def calc_paddle_move(self):
        if self.paddle_x < self.ball_x:
            return 1
        if self.paddle_x > self.ball_x:
            return -1
        return 0

    def get_joystick_pos(self):
        key = self.window.getch()
        while self.window.getch() != -1:  # Disregard all other key presses that have been saved up
            pass

        if key == curses.KEY_LEFT:
            return -1
        if key == curses.KEY_RIGHT:
            return 1

        return 0

    def play(self, rendered=True, interactive=True, fps=1):
        try:
            if rendered:
                self.window = curses.initscr()
                self.fps = fps
                curses.cbreak()
                curses.noecho()
                curses.curs_set(0)
                self.window.nodelay(True)
                self.window.keypad(True)
                self.prev_frame_time = time.time() - 1 / self.fps

            while True:
                self.program.run()
                self.process_prog_outputs()
                if rendered:
                    self.print_frame()

                if self.program.halted:
                    break

                if interactive:
                    joystick_pos = self.get_joystick_pos()
                else:
                    joystick_pos = self.calc_paddle_move()
                self.program.inputs.append(joystick_pos)

        finally:  # Don't leave the terminal in altered state
            if rendered:
                self.window.keypad(False)
                self.window.nodelay(False)
                curses.curs_set(2)
                curses.echo()
                curses.nocbreak()
                curses.endwin()

    def print_frame(self):
        max_y, max_x = self.window.getmaxyx()
        for (x, y), tile_id in self.tiles.items():
            if y >= max_y or x >= max_x:
                raise ValueError("Game does not fit inside terminal window")

            self.window.addch(y, x, self.tile_chars[tile_id])

        # Try to keep constant time between frames. This is noticeably not working at low fps, probably because some
        # buffering is going on in the terminal itself, leading to a variable delay between a call to
        # self.window.refresh and the output appearing on screen. It does not matter that much for solving the puzzle.
        time.sleep(max(1 / self.fps - (time.time() - self.prev_frame_time), 0))
        self.window.refresh()
        self.prev_frame_time = time.time()

    def process_prog_outputs(self):
        while self.program.outputs:
            tile_id = self.program.outputs.pop()
            y = self.program.outputs.pop()
            x = self.program.outputs.pop()

            if x == -1 and y == 0:
                self.score = tile_id
            else:
                self.tiles[(x, y)] = tile_id
                if tile_id == 3:
                    self.paddle_x = x
                elif tile_id == 4:
                    self.ball_x = x
                    self.ball_y = y

    @property
    def num_remaining_block_tiles(self):
        return len([tile_id for tile_id in self.tiles.values() if tile_id == 2])


def solve_part_1(puzzle_input):
    prog = Program(puzzle_input)
    game = BreakoutGame(prog)
    game.play(rendered=False, interactive=False)

    return game.num_remaining_block_tiles


def solve_part_2(puzzle_input):
    prog = Program(puzzle_input)
    prog.memory[0] = 2
    game = BreakoutGame(prog)
    game.play(rendered=False, interactive=False)

    return game.score
