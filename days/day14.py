from collections import defaultdict, namedtuple
from functools import partial

Material = namedtuple('Material', ['name', 'amount'])


def parse_puzzle_input(puzzle_input):
    reactions = dict()

    for line in puzzle_input.splitlines():
        lhs, rhs = line.split('=>')
        product_amount, product_name = rhs.split()
        product = Material(product_name, int(product_amount))
        ingredients = [Material(term.split()[1], int(term.split()[0])) for term in lhs.split(',')]

        reactions[product.name] = (product, ingredients)

    return reactions


def ore_required(reactions, fuel_to_produce=1):
    required = {"FUEL": fuel_to_produce}
    remaining = defaultdict(int)

    ore_amount = 0
    while required:
        prev_required = required
        required = dict()
        for req_name, req_amount in prev_required.items():
            if req_name == 'ORE':
                ore_amount += req_amount
                continue

            product, ingredients = reactions[req_name]
            to_create = max(req_amount - remaining[req_name], 0)
            num_reactions = (to_create + (product.amount - 1)) // product.amount
            remaining[req_name] = num_reactions * product.amount - (req_amount - remaining[req_name])

            for ingredient in ingredients:
                amount = ingredient.amount * num_reactions
                if ingredient.name in required:
                    required[ingredient.name] += amount
                else:
                    required[ingredient.name] = amount

    return ore_amount


def find_upper_lim_arg(fun, start, limit_val):
    # Fun should increase monotonically
    lim = start
    while fun(lim) < limit_val:
        lim *= 2

    return lim


def bin_search_glb(fun, lower_lim, upper_lim, target):
    """
    Return the greatest lower bound (glb) of the set of argument values between lower_lim and upper_lim (inclusive) for
    which fun(arg) < target, using binary search.

    :param fun: Monotonically increasing function of a single int; does not have to be strictly monotonic
    :param lower_lim: Any integer s.t. fun(lower_lim) < target and lower_lim < upper_lim
    :param upper_lim: Any integer s.t. fun(upper_lim) > target and lower_lim < upper_lim
    :param target: The search target
    :return: Integer glb
    """

    while upper_lim - lower_lim > 1:
        mid = lower_lim + (upper_lim - lower_lim) // 2
        if fun(mid) <= target:
            lower_lim = mid
        else:
            upper_lim = mid

    return lower_lim


def solve_part_1(puzzle_input):
    reactions = parse_puzzle_input(puzzle_input)
    return ore_required(reactions)


def solve_part_2(puzzle_input):
    reactions = parse_puzzle_input(puzzle_input)
    search_fun = partial(ore_required, reactions)
    lower_lim = 0
    upper_lim = find_upper_lim_arg(search_fun, 1, int(1e12))
    return bin_search_glb(search_fun, lower_lim, upper_lim, int(1e12) + 1)
