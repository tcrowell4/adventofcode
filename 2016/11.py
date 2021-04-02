import re
import sys
from collections import namedtuple, defaultdict, deque
from dataclasses import dataclass
from itertools import combinations
from typing import Any
import numpy as np

# import graph

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
    floor_idx = {3: "F1", 2: "F2", 1: "F3", 0: "F4"}
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
        dprint(i, v)
    dprint("=========")
    # dprint(sorted(ITEMS_ABBR))
    for i, v in enumerate(sorted(ITEMS_ABBR)):
        item_dict[v] = i + 1
    dprint("=========")
    dprint("item_dict", len(item_dict))
    for i, v in item_dict.items():
        dprint(i, v)
    dprint("=========")
    # dprint(FLOORS)
    # s = {x[:2] for x in ITEMS_ABBR}
    # x = []
    # for i, v in enumerate(s):
    #     x.append(str(i + 1) + "G")
    #     x.append(str(i + 1) + "M")
    # dprint(sorted(x))

    initial_state = np.zeros((len(floor_dict), len(item_dict) + 1), dtype=np.int8)

    # build the state
    # column 0 is the elevator  1=current floor
    # column 1,3,5... = Generator
    # column 2,4,6 = matching microchip
    for i, v in floor_dict.items():
        for j in v:
            initial_state[i, item_dict[j]] = 1
    initial_state[3, 0] = 1  # set starting elevator floor
    dprint(initial_state)
    key = initial_state.flatten().tolist()
    id = "".join([str(aa) for aa in key])
    init_node = Node(initial_state, id, "start")
    dprint(init_node)
    print(init_node.state)

    # z = np.copy(init_node.state)
    # print(init_node.state, validate_state(init_node.state))
    # z[1, 2] = 1
    # print(z, validate_state(z))

    return init_node


def validate_state(state):
    """
    determine if any microchip is unprotected with another generator present
    must validate protected chip
    if unprotected chip and there is at least one Generator then it is invalid
    - ergo: if unprotected the generator is not its mate
    """
    for row in state:
        gen = row[1::2]
        # print(gen)
        g = np.sum(gen)  # finds the number of generators
        mc = row[2::2]
        # print(mc)
        m = np.sum(mc)
        # print(f"Gen = {g} Microchip {m}")
        for i in range(len(mc)):
            if mc[i] > gen[i] and g > 0:
                # print("unprotected")
                # print("fried chip")
                return False
    return True


"""
State-space search algorithm
;; problem describes the start state, operators, goal test, and operator costs
;; queueing-function is a comparator function that ranks two states
;; general-search returns either a goal node or failure
"""

#  function general-search (problem, QUEUEING-FUNCTION)
def bfs(startnode):
    r, c = startnode.state.shape
    final_state = np.zeros((r, c), dtype=np.int8)
    final_state[0] = 1  # set top floor to all ones
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
        dprint(">>>>>>>>>>>>>", node.id)
        if node.id in SEEN:
            continue
        dprint("================", node.id, node.prev)
        # print(node.id)
        # print("================")
        marked(node)
        graph[node.id].append(node.prev)
        # • GOAL-TEST
        # 	– Test if state satisfies all goal conditions
        if np.array_equal(node.state, final_state):
            return node, graph
        # nodes = QUEUEING-FUNCTION(nodes, EXPAND(node,
        #         problem.OPERATORS))
        successor_nodes = queue.extend(expand(node))
        SEEN.add(node.id)


def expand(node):
    # get row that elevator is stopped on
    # elevator is column 0
    e_col = node.state[:, 0]
    idx = [i for i, v in enumerate(e_col) if v > 0]

    # extract elevator row
    current_floor = node.state[idx]

    # find the indexes for columns with devices
    xx = [i + 1 for i, v in enumerate(current_floor[0, 1:]) if v > 0]
    move_one_device = [(0, v) for i, v in enumerate(xx) if v > 0]
    move_two_devices = [x for x in (combinations(xx, 2))]
    move_devices = move_one_device + move_two_devices
    return create_new_states(node, idx[0], move_devices)


def create_new_states(old_node, cf, opts):
    # cf = current_floor
    # opts is the number of options in a list
    #  [(0, 2), (0, 4), (2, 4)]
    new_nodes = []
    r, c = old_node.state.shape
    # if not at the top row create an up state
    for i in opts:
        ns = np.copy(old_node.state)
        dprint(f"items moving {i} current_floor:{cf}  r:{r}")
        dprint(f"opts {opts}")
        item1, item2 = i
        if cf + 1 != r:  # form dn state
            ns_dn = np.copy(old_node.state)
            if item1 != 0:
                ns_dn[cf, item1], ns_dn[cf + 1, item1] = (
                    ns_dn[cf + 1, item1],
                    ns_dn[cf, item1],
                )
            if item2 != 0:
                ns_dn[cf, item2], ns_dn[cf + 1, item2] = (
                    ns_dn[cf + 1, item2],
                    ns_dn[cf, item2],
                )
            ns_dn[cf, 0], ns_dn[cf + 1, 0] = (
                ns_dn[cf + 1, 0],
                ns_dn[cf, 0],
            )  # swap floor
            if validate_state(ns_dn):
                dprint(f"down {i}\n {ns_dn}")
                key = ns_dn.flatten().tolist()
                id = "".join([str(aa) for aa in key])
                n_node = Node(ns_dn, id, old_node.id)
                new_nodes.append(n_node)

        if cf != 0:
            ns_up = np.copy(old_node.state)
            if item1 != 0:
                ns_up[cf, item1], ns_up[cf - 1, item1] = (
                    ns_up[cf - 1, item1],
                    ns_up[cf, item1],
                )
            if item2 != 0:
                ns_up[cf, item2], ns_up[cf - 1, item2] = (
                    ns_up[cf - 1, item2],
                    ns_up[cf, item2],
                )
            ns_up[cf, 0], ns_up[cf - 1, 0] = (
                ns_up[cf - 1, 0],
                ns_up[cf, 0],
            )  # swap floor
            if validate_state(ns_up):
                dprint(f"up {i}\n {ns_up}")
                key = ns_up.flatten().tolist()
                id = "".join([str(aa) for aa in key])
                n_node = Node(ns_up, id, old_node.id)
                new_nodes.append(n_node)

        dprint("creating new nodes", new_nodes)

    return new_nodes

    # if r != 0:


def marked(n):
    # print(n)
    pass


def main():

    with open("11.in") as fp:
        lines = [line.strip() for line in fp]
    # print("=========", lines)
    initial_node = process_input(lines)
    n, g = bfs(initial_node)
    # process_input(lines, part2, "part 2")
    # print(SEEN)
    # for i, v in g.items():
    #     print(i, v)

    s = n.id
    cnt = 0
    while s != "start":
        next = g[s]
        next = next[0]
        print(cnt, next)
        s = next
        cnt += 1
    return


if __name__ == "__main__":
    main()
