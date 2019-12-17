from days.intcode_computer import Program


def solve_part_1(puzzle_input):
    prog = Program(puzzle_input)
    screen = dict()

    prog.run()
    for _ in range(len(prog.outputs) // 3):
        tile_id = prog.outputs.pop()
        y = prog.outputs.pop()
        x = prog.outputs.pop()

        screen[(x, y)] = tile_id

    num_blocks = 0
    for tile_id in screen.values():
        if tile_id == 2:
            num_blocks += 1

    return num_blocks
