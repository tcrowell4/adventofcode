from collections import defaultdict
import numpy as np


def void(*args):
    pass


# used to control whether to debug print or not
# dprint = print
dprint = void


def process_input(lines):
    print("========Part1==========")
    possible, not_possible = 0, 0
    for line in lines:
        dprint("=================")
        dprint(line)
        a, b, c = sorted(line)
        if (a + b) > c:
            dprint(a, b, c, "possible")
            possible += 1
        else:
            not_possible += 1
    print("Possible: {}  Not Possible: {}".format(possible, not_possible))


def process_input2(lines):
    print("========Part2==========")
    possible, not_possible = 0, 0
    arr = np.array(lines)
    dprint(arr)
    arrT = arr.T.reshape(-1, 3)
    dprint(arrT)
    for x in arr.T.reshape(-1, 3):
        dprint("=================")
        dprint(x)
        a, b, c = sorted(x)
        if (a + b) > c:
            dprint(a, b, c, "possible")
            possible += 1
        else:
            not_possible += 1
    print("Possible: {}  Not Possible: {}".format(possible, not_possible))


def main():
    with open("3_input.txt") as fp:
        lines = [[int(x) for x in line.strip().split()] for line in fp]
    # print("=========", lines)
    process_input(lines)
    process_input2(lines)

    return


if __name__ == "__main__":
    main()
