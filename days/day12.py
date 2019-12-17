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


def solve_part_1(puzzle_input):
    moons = parse_puzzle_input(puzzle_input)
    moon_sim = MoonSimulation(moons)

    for _ in range(1000):
        moon_sim.step()

    return moon_sim.total_energy
