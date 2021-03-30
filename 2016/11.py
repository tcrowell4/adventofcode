import re
import sys
from collections import namedtuple, defaultdict, deque
from dataclasses import dataclass
from typing import Any
import numpy as np

"""
--- Day 11: Radioisotope Thermoelectric Generators ---
chips only shielded when powered by corresponding RTG
chip fried if left by other RTG if not powered by it's own RTG
keep chips connected to their corresponding RTG when
    they're in the same room, and away from other RTGs otherwise

elevator:
capacity: 2 RTGS or microchips in any combination
only functions if it has at least one RTG or chip
always stops on each floor
    items in it subject to items on the floor
    chip or generator powered while elevator recharging
"""


@dataclass
class Node:
    state: any
    id: any


def pause():
    programPause = input("Press the <ENTER> key to continue...")


def void(*args, **kwargs):
    pass


# used to control whether to debug print or not
dprint = void
dprint = print

ITEMS = []
ITEMS_ABBR = []
FLOORS = []

INITIAL_STATE = ""


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
    for line in lines:
        items = re.findall(r"([-\w]* microchip|[-\w]* generator)", line)
        floor_no = floor[line.split()[1]]
        FLOORS.append(line.split()[1])
        ITEMS.extend(items)
        items_abbr = [
            (i.split()[0][0:2] + "_" + i.split()[1][0]).upper() for i in items
        ]
        ITEMS_ABBR.extend(items_abbr)
        dprint(floor_no, items)
        floor_dict[floor_no] = items_abbr
        dprint(floor_no, items_abbr)

    # dprint(ITEMS)
    dprint("=========")
    dprint("floor_dict", len(floor_dict))
    for i, v in floor_dict.items():
        print(i, v)
    dprint("=========")
    # dprint(sorted(ITEMS_ABBR))
    for i, v in enumerate(sorted(ITEMS_ABBR)):
        item_dict[v] = i + 1
    dprint("=========")
    dprint("item_dict", len(item_dict))
    for i, v in item_dict.items():
        print(i, v)
    dprint("=========")
    # dprint(FLOORS)
    # s = {x[:2] for x in ITEMS_ABBR}
    # x = []
    # for i, v in enumerate(s):
    #     x.append(str(i + 1) + "G")
    #     x.append(str(i + 1) + "M")
    # dprint(sorted(x))

    initial_state = np.zeros((len(floor_dict), len(item_dict) + 1), dtype=np.int8)

    for i, v in floor_dict.items():
        for j in v:
            initial_state[i, item_dict[j]] = 1
    initial_state[3, 0] = 1  # set starting elevator floor
    print(initial_state)

    init_node = Node(initial_state, "initial state")
    print(init_node)
    print(init_node.state)

    z = np.copy(init_node.state)
    z[0, 2] = 9
    print(init_node.state)
    print(z)


"""
State-space search algorithm
;; problem describes the start state, operators, goal test, and operator costs
;; queueing-function is a comparator function that ranks two states
;; general-search returns either a goal node or failure
"""

#  function general-search (problem, QUEUEING-FUNCTION)
def bfs(startnode):
    # Track the visited and unvisited nodes using queue
    # nodes = MAKE-QUEUE(MAKE-NODE(problem.INITIAL-STATE))
    seen, queue = set([startnode]), collections.deque([startnode])

    # if EMPTY(nodes) then return "failure"
    while queue:
        # node = REMOVE-FRONT(nodes)
        vertex = queue.popleft()
        marked(vertex)
        # • GOAL-TEST
        # 	– Test if state satisfies all goal conditions
        if node.state == INITIAL_STATE:
            return node
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)


def marked(n):
    print(n)


def main():

    with open("11s.in") as fp:
        lines = [line.strip() for line in fp]
    # print("=========", lines)
    process_input(lines)
    # process_input(lines, part2, "part 2")

    return


if __name__ == "__main__":
    main()
