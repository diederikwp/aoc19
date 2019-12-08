from collections import defaultdict


def parse_input(puzzle_input):
    nodes = set()
    edges = defaultdict(set)  # key: "from"-node, value: set of "to"-nodes.
    edges_reversed = dict()  # key: "to"-node, value: "from"-node (never more than 1).

    for line in puzzle_input.splitlines():
        node1, node2 = line.split(')')
        nodes.add(node1)
        nodes.add(node2)
        edges[node1].add(node2)
        edges_reversed[node2] = node1

    return nodes, edges, edges_reversed


def solve_part_1(puzzle_input):
    nodes, edges, _ = parse_input(puzzle_input)
    visited = {'COM'}  # 'COM' is the root node, and there is only 1 connected component, so we start from 'COM'.
    num_orbits = 0
    steps = 1

    while visited:
        prev_visited = visited
        visited = set()

        for node in prev_visited:
            reachable = edges[node]
            visited.update(reachable)
            num_orbits += steps * len(reachable)

        steps += 1

    return num_orbits


def solve_part_2(puzzle_input):
    # Breadth-first search

    nodes, edges, edges_reversed = parse_input(puzzle_input)
    start = edges_reversed['YOU']
    end = edges_reversed['SAN']
    steps = 0
    visited = {start}
    reachable = {start}

    while end not in visited:
        prev_reachable = reachable
        reachable = set()
        for node in prev_reachable:
            reachable.update(edges[node])
            if node in edges_reversed:
                reachable.add(edges_reversed[node])

        reachable.difference_update(visited)  # Do not revisit already visited nodes
        visited.update(reachable)
        steps += 1

    return steps
