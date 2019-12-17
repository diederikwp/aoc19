import unittest

from days.day12 import Moon, MoonSimulation, lcm, parse_puzzle_input, solve_part_1, solve_part_2


class TestMoon(unittest.TestCase):
    def test_move(self):
        m = Moon(1, 2, -3)
        m.velocity = [20, -3, 1]

        m.move()
        self.assertEqual(m.pos, [21, -1, -2])
        self.assertEqual(m.velocity, [20, -3, 1])

        m.move()
        self.assertEqual(m.pos, [41, -4, -1])
        self.assertEqual(m.velocity, [20, -3, 1])

    def test_gravity(self):
        m1 = Moon(1, 2, -3)
        m2 = Moon(3, 1, -2)
        m2.velocity = [5, -5, 10]

        m1.apply_gravity(m2)
        self.assertEqual(m1.pos, [1, 2, -3])
        self.assertEqual(m1.velocity, [1, -1, 1])
        self.assertEqual(m2.pos, [3, 1, -2])
        self.assertEqual(m2.velocity, [5, -5, 10])

        m2.apply_gravity(m1)
        self.assertEqual(m1.pos, [1, 2, -3])
        self.assertEqual(m1.velocity, [1, -1, 1])
        self.assertEqual(m2.pos, [3, 1, -2])
        self.assertEqual(m2.velocity, [4, -4, 9])

    def test_energy(self):
        m = Moon(1, 2, -3)
        m.velocity = [20, -3, 1]

        self.assertEqual(m.energy, 144)


class TestMoonSimulation(unittest.TestCase):
    def test_example_1(self):
        moons = [Moon(-1, 0, 2), Moon(2, -10, -7), Moon(4, -8, 8), Moon(3, 5, -1)]
        moon_sim = MoonSimulation(moons)
        for _ in range(10):
            moon_sim.step()

        self.assertEqual(moon_sim.steps, 10)
        self.assertEqual(moon_sim.total_energy, 179)

    def test_example_2(self):
        moons = [Moon(-8, -10, 0), Moon(5, 5, 10), Moon(2, -7, 3), Moon(9, -8, -3)]
        moon_sim = MoonSimulation(moons)
        for _ in range(100):
            moon_sim.step()

        self.assertEqual(moon_sim.steps, 100)
        self.assertEqual(moon_sim.total_energy, 1940)


class TestDay12(unittest.TestCase):
    def setUp(self):
        self.puzzle_input_1 = ('<x=0, y=6, z=1>\n'
                               '<x=4, y=4, z=19>\n'
                               'x=-11, y=1, z=8>\n'
                               'x=2, y=19, z=15>\n')
        self.puzzle_input_2 = ('<x=-1, y=0, z=2>\n'
                               '<x=2, y=-10, z=-7>\n'
                               'x=4, y=-8, z=8>\n'
                               'x=3, y=5, z=-1>\n')
        self.puzzle_input_3 = ('<x=-8, y=-10, z=0>\n'
                               '<x=5, y=5, z=10>\n'
                               '<x=2, y=-7, z=3>\n'
                               '<x=9, y=-8, z=-3>\n')

    def test_parse_puzzle_input(self):
        self.assertEqual(parse_puzzle_input(self.puzzle_input_1), [Moon(0, 6, 1),
                                                                   Moon(4, 4, 19),
                                                                   Moon(-11, 1, 8),
                                                                   Moon(2, 19, 15)])

    def test_lcm(self):
        self.assertEqual(lcm(90, 56), 2520)
        self.assertEqual(lcm(90, 56, 25), 12600)
        self.assertEqual(lcm(11, 1), 11)
        self.assertEqual(lcm(11, -1), 11)
        self.assertEqual(lcm(90, 56, 25, -252), 12600)

    def test_solve_part1(self):
        # Just use the official puzzle as test
        self.assertEqual(solve_part_1(self.puzzle_input_1), 14809)

    def test_solve_part_2(self):
        self.assertEqual(solve_part_2(self.puzzle_input_2), 2772)
        self.assertEqual(solve_part_2(self.puzzle_input_3), 4686774924)


if __name__ == '__main__':
    unittest.main()
