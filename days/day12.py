from math import gcd


class Moon:
    def __init__(self, x, y, z):
        self.pos = [x, y, z]
        self.velocity = [0, 0, 0]

    def apply_gravity(self, other):
        for dim in range(3):
            if self.pos[dim] > other.pos[dim]:
                self.velocity[dim] -= 1
            elif self.pos[dim] < other.pos[dim]:
                self.velocity[dim] += 1

    def move(self):
        for dim in range(3):
            self.pos[dim] += self.velocity[dim]

    @property
    def energy(self):
        return sum([abs(p) for p in self.pos]) * sum([abs(v) for v in self.velocity])

    def __eq__(self, other):
        return self.pos == other.pos and self.velocity == other.velocity

    def __repr__(self):
        return f'pos=<x={self.pos[0]: >3d}, y={self.pos[1]: >3d}, z={self.pos[2]: >3d}>, ' \
               f'vel=<x={self.velocity[0]: >3d}, y={self.velocity[1]: >3d}, z={self.velocity[2]: >3d}>'


class MoonSimulation:
    def __init__(self, moons):
        self.moons = moons
        self.steps = 0

    def apply_gravity(self):
        # Gravity only depends on position, which is unchanged by application of gravity. Hence order of application
        # does not matter
        for m_outer in self.moons:
            for m_inner in self.moons:
                m_outer.apply_gravity(m_inner)

    def apply_velocity(self):
        for m in self.moons:
            m.move()

    def step(self):
        self.apply_gravity()
        self.apply_velocity()
        self.steps += 1

    @property
    def total_energy(self):
        return sum([m.energy for m in self.moons])


def parse_puzzle_input(puzzle_input):
    moons = []
    for line in puzzle_input.splitlines():
        pos = []
        for part in line[1:-1].split(','):
            equals_idx = part.find('=')
            pos.append(int(part[equals_idx + 1:]))
        moons.append(Moon(*pos))

    return moons


def lcm(*args):
    # lowest common multiple
    ret = args[0] * args[1] // gcd(args[0], args[1])
    for i in range(1, len(args)):
        ret = ret * args[i] // gcd(ret, args[i])

    return abs(ret)


def solve_part_1(puzzle_input):
    moons = parse_puzzle_input(puzzle_input)
    moon_sim = MoonSimulation(moons)

    for _ in range(1000):
        moon_sim.step()

    return moon_sim.total_energy


def solve_part_2(puzzle_input):
    # Determine period of x, y and z coordinates separately. The entire (x, y, z) state repeats at the lowest common
    # multiple of those 3 periods, since the x, y and z motions are independent.
    moons = parse_puzzle_input(puzzle_input)
    moon_sim = MoonSimulation(moons)

    history = [set(), set(), set()]  # x, y, z
    periods = [None, None, None]
    periods_known = [False, False, False]

    while not all(periods_known):
        for dim in range(3):
            if periods_known[dim]:
                continue

            state = tuple(((m.pos[dim], m.velocity[dim]) for m in moon_sim.moons))
            if state in history[dim]:
                periods[dim] = moon_sim.steps
                periods_known[dim] = True

            history[dim].add(state)

        moon_sim.step()

    return lcm(periods[0], periods[1], periods[2])
