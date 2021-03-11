from collections import defaultdict
import numpy as np


def void(*args):
    pass


# used to control whether to debug print or not
# dprint = print
dprint = void


def execute_move(instr, row, col, arr):
    """
    For arrays moving left and right are associated with columns
    up and down are rows
    """
    action = instr
    amount = 1

    dprint("Action: {} Location: {}:{} {}".format(action, row, col, arr[row][col]))

    if (action in ">R") and (col < 4):
        if arr[row][col + 1] != " ":
            col += amount
    elif (action in "<L") and (col > 0):
        if arr[row][col - 1] != " ":
            col -= amount
    elif (action in "^U") and (row > 0):
        if arr[row - 1][col] != " ":
            row -= amount
    elif (action in "vD") and (row < 4):
        dprint(arr[row + 1][col])
        if arr[row + 1][col] != " ":
            row += amount

    dprint(
        "After: Action: {}  Location: {}:{} {}".format(action, row, col, arr[row][col])
    )

    return row, col


def process_directions(nav):
    # arr = np.arange(1, 10).reshape(3, 3)
    # arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]   #part 1
    arr = [
        [" ", " ", "1", " ", " "],
        [" ", "2", "3", "4", " "],
        ["5", "6", "7", "8", "9"],
        [" ", "A", "B", "C", " "],
        [" ", " ", "D", " ", " "],
    ]

    dprint(arr)
    door_code = []
    row = 2  # East-West location
    col = 0  # North-South location

    for instruction in nav:
        dprint("=================")
        for direction in instruction:
            dprint(direction)
            row, col = execute_move(direction, row, col, arr)
        door_code.append(arr[row][col])
        print("door_code {}".format("".join(door_code), "=== ", arr[row][col]))


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
