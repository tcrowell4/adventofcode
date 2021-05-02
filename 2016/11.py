import re
import sys
from collections import namedtuple, defaultdict, deque
from dataclasses import dataclass
from itertools import combinations, chain
from typing import Any, List, Set, Dict, Tuple, Optional
import numpy as np
import time
import pprint


# import graph

"""
--- Day 11: Radioisotope Thermoelectric Generators ---
chips only shielded when powered by corresponding RTG
chip fried if left by other RTG if not powered by it's own RTG
keep chips connected to their corresponding RTG when
    they're in the same room, and away from other RTGs otherwise

elevator:g
capacity: 2 RTGS or microchips in any combination
only functions if it has at least one RTG or chip
always stops on each floor
    items in it subject to items on the floor
    chip or generator powered while elevator recharging
"""


@dataclass
class Node:
    state: any
    floor: int
    distance: int
    # id: str
    prev: any


def pause():
    programPause = input("Press the <ENTER> key to continue...")


def void(*args, **kwargs):
    pass


# used to control whether to debug print or not
dprint = void
# dprint = print

ITEMS = []
ITEMS_ABBR = []
FLOORS = []
SEEN = set()


def entryExit(func):
    def wrapper(*args, **kwargs):
        dprint("Before function call")
        result = func(*args, **kwargs)
        dprint("After function call")
        return result

    return wrapper


# @entryExit
def process_input(lines, part=1):
    floor_dict = defaultdict(list)
    item_dict = defaultdict(int)
    # floor value is the array row value  3 = is the first floor out of 4 floors
    floor = {"first": 3, "second": 2, "third": 1, "fourth": 0}
    # floor = range(4)
    # floor_idx = {3: "F1", 2: "F2", 1: "F3", 0: "F4"}
    for fl, line in enumerate(lines):
        items = re.findall(r"([-\w]* microchip|[-\w]* generator)", line)
        floor_no = floor[line.split()[1]]
        for k in items:
            item_dict[k] = int(fl)
        # item_dict = {k: int(fl) for k in items}
        dprint("item_dict", len(item_dict))
        for i, v in item_dict.items():
            dprint(i, v)
        dprint("=========")

    """
    item_dict contains all the sorted elements and which floor
    they started at:

    cobalt generator 0
    cobalt-compatible microchip 0
    polonium generator 0
    polonium-compatible microchip 1
    promethium generator 0
    promethium-compatible microchip 1
    ruthenium generator 0
    ruthenium-compatible microchip 0
    thulium generator 0
    thulium-compatible microchip 0

    from it we create a list of the items floor positions
    (Pdb) items
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
    |    |= is a generator microchip pair

    they are then joined as Tuple pairs
    (Pdb) pairs
    ((0, 0), (0, 1), (0, 1), (0, 0), (0, 0))
      |  |
      G  M

    """

    dprint("===ALL*======")
    for k in sorted(item_dict.keys()):
        dprint(k, item_dict[k])

    items = [item_dict[k] for k in sorted(item_dict.keys())]
    print("items", items)

    pairs = tuple((items[i], items[i + 1]) for i in range(0, len(items), 2))
    print("pairs", pairs)

    # =========================================
    # dump the state
    floors = [[], [], [], []]
    for element, (x, y) in enumerate(pairs):
        floors[x].append((element, 0))  # (element_index, type)
        floors[y].append((element, 1))

    dprint("=== floors ===")
    for f in floors:
        dprint(f)

    dprint("=== floors 2 ===")
    dprint(floors)
    # =========================================

    starting_floor = 0  # set starting elevator floor
    initial_state = tuple(sorted(pairs))

    init_node = Node(initial_state, starting_floor, 0, "start")
    dprint(init_node)
    print(init_node.state)

    return init_node


def validate_state(floors: List[List[Tuple[int, int]]]) -> bool:
    """

    determine if any microchip is unprotected with another generator present
    must validate protected chip
    if unprotected chip and there is at least one Generator then it is invalid
    - ergo: if unprotected the generator is not its mate

    # state check:
    # if the item type is 1 (microchip) and the
    # corresponding generator (type 0)  is not
    # on the same floor (same element_index ) and there are any other generators
    # then the chip is fried and this is not a valid state

    # this is what the floors variable represents extracted rows
    floors = [[], [], [], []]
    # dump the state
    for element, (x, y) in enumerate(state):
        floors[x].append((element, 0))  # (element_index, type)
        floors[y].append((element, 1))

    """

    for row in floors:
        mc = [e for e, x in row if x == 1]
        gen = [e for e, x in row if x == 0]
        unprotected = [mc for i in mc if i not in gen]
        # print(f"Gen = {g} Microchip {m}")
        # for any items not protected and if any generators
        # then the microchip is fried
        if unprotected and gen:
            dprint(row)
            return False
    return True


def create_floors(state):
    # extract elevator row
    floors = [[], [], [], []]
    # dump the state
    for element, (x, y) in enumerate(state):
        floors[x].append((element, 0))  # (element_index, type)
        floors[y].append((element, 1))
    return floors


"""
State-space search algorithm
;; problem describes the start state, operators, goal test, and operator costs
;; queueing-function is a comparator function that ranks two states
;; general-search returns either a goal node or failure
"""

#  function general-search (problem, QUEUEING-FUNCTION)
def bfs(startnode):
    final_state = tuple((3, 3) for j, _ in startnode.state)
    # Track the visited and unvisited nodes using queue
    # nodes = MAKE-QUEUE(MAKE-NODE(problem.INITIAL-STATE))
    # seen, queue = startnode, deque(startnode)
    # seen = set(startnode)
    # SEEN.add(startnode.id)
    queue = deque([startnode])
    graph = defaultdict(list)

    # if EMPTY(nodes) then return "failure"
    while queue:
        # node = REMOVE-FRONT(nodes)
        node = queue.popleft()
        dprint("================", node.state, node.floor, node.prev)

        # extract elevator row
        floors = [[], [], [], []]
        # dump the state
        for element, (x, y) in enumerate(node.state):
            floors[x].append((element, 0))  # (element_index, type)
            floors[y].append((element, 1))

        if not validate_state(floors):
            dprint("INVALID", node.state)
            continue

        if (node.distance, node.state, node.floor) in SEEN:
            continue
        # print("================")

        marked(node)
        graph[node.state].append(node.prev)

        # • GOAL-TEST
        # 	– Test if state satisfies all goal conditions
        # if np.array_equal(node.state, final_state):
        # print(node.state, final_state)
        if node.state == final_state:
            return node, graph

        # nodes = QUEUEING-FUNCTION(nodes, EXPAND(node,
        #         problem.OPERATORS))
        x = expand(node, floors)
        successor_nodes = queue.extend(x)

        SEEN.add((node.distance, node.state, node.floor))

    print("FAILURE")


# @entryExit
def expand(node, floors: List[List[Tuple[int, int]]]):
    new_nodes = []
    floor = node.floor
    pairs = node.state
    dprint(">>> Node:", node)
    # clever algorithm
    # calculates whether adjusting the floors up(+1) or down (-1)
    # find the threshold of the floor
    #   floor = 3
    #   {min(floor + 1, 3), max(floor - 1, 0)}
    #       {2, 3}
    # since the floor current_floor is 3 then 3 will be removed
    # by the ....     - set([floor])
    # that way only options for up direction will be created

    # candidates = chain(floors[floor], combinations(floors[floor], 2))

    for floorx in {min(floor + 1, 3), max(floor - 1, 0)} - set([floor]):
        dprint(">>> Floors:", floorx, floors[floor])
        # pprint.pprint(floors)
        dprint(pairs)
        for i, things in enumerate(
            chain(map(lambda x: [x], floors[floor]), combinations(floors[floor], 2))
        ):
            dprint("Things", i, things, type(things))
            # convert pairs to list of lists
            x = [[g, m] for g, m in pairs]
            for thing in things:
                dprint(i, thing)
                i, e = thing
                x[i][e] = floorx
            # convert new pairs to tuple
            new_pairs = tuple(tuple(z) for z in x)
            new_nodes.append(
                Node(tuple(sorted(new_pairs)), floorx, node.distance + 1, node.state)
            )
            dprint("new_pairs", new_pairs)
            # pprint.pprint(new_nodes)

    return new_nodes


def marked(n):
    # print(n)
    pass


def main():
    start = time.time()
    print("Start Timer")
    with open("11_2.in") as fp:
        lines = [line.strip() for line in fp]
    # print("=========", lines)
    initial_node = process_input(lines)
    n, g = bfs(initial_node)
    # process_input(lines, part2, "part 2")
    # print(SEEN)
    # for i, v in g.items():
    #     print(i, v)

    print(f"Distance: {n.distance}")
    end = time.time()
    print(end - start)

    return

    def p_id(id):
        print(f"Floor {id[0]}")
        for i in range(4):
            print(id[(i * 4) + 1 : (i * 4) + 5])

    s = n.id
    cnt = 0
    while s != "start":
        p_id(s)
        next = g[s]
        next = next[0]
        print(cnt, next)
        s = next
        cnt += 1

    return


if __name__ == "__main__":
    main()
