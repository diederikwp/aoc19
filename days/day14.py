from collections import defaultdict, namedtuple

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


def ore_required(reactions):
    required = {"FUEL": 1}
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


def solve_part_1(puzzle_input):
    reactions = parse_puzzle_input(puzzle_input)
    return ore_required(reactions)
