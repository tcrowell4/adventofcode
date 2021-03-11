from collections import defaultdict
import numpy as np


def void(*args):
    pass


# used to control whether to debug print or not
# dprint = print
dprint = void


def execute_move(instr, row, col):
    """
    For arrays moving left and right are associated with columns
    up and down are rows
    """
    action = instr
    amount = 1

    dprint("Action: {} Location: {}:{}".format(action, row, col))

    if (action in ">R") and (col < 2):
        col += amount
    elif (action in "<L") and (col > 0):
        col -= amount
    elif (action in "^U") and (row > 0):
        row -= amount
    elif (action in "vD") and (row < 2):
        row += amount

    dprint("After: Action: {}  Location: {}:{}".format(action, row, col))

    return row, col


def process_directions(nav):
    arr = np.arange(1, 10).reshape(3, 3)
    dprint(arr)
    door_code = []
    row = 1  # East-West location
    col = 1  # North-South location

    for instruction in nav:
        for direction in instruction:
            dprint(direction)
            row, col = execute_move(direction, row, col)
        door_code.append(str(arr[row, col]))
        print("door_code {}".format("".join(door_code), "=== ", arr[row, col]))


def main():
    with open("2_input.txt") as fp:
        lines = fp.readlines()
    # strip each line and break into individual characters
    nav_list = list(map(lambda x: x.strip(), lines))
    # print("=========", nav_list)
    process_directions(nav_list)

    return


if __name__ == "__main__":
    main()
