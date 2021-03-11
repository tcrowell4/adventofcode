from collections import defaultdict
import numpy as np


def void(*args):
    pass


# used to control whether to debug print or not
# dprint = print
dprint = void


def process_input(lines):
    print("========Part1==========")
    possible_list = []
    possible, not_possible = 0, 0
    for line in lines:
        dprint("=================")
        dprint(line)
        a, b, c = sorted(line)
        if (a + b) > c:
            dprint(a, b, c, "possible")
            possible += 1
            possible_list.append(line)
        else:
            not_possible += 1
    print("Possible: {}  Not Possible: {}".format(possible, not_possible))


def main():
    with open("3_input.txt") as fp:
        lines = [[int(x) for x in line.strip().split()] for line in fp]
    # print("=========", lines)
    process_input(lines)

    return


if __name__ == "__main__":
    main()
