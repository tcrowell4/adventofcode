#!/usr/bin/python


import sys
import re
import numpy as np
from collections import defaultdict
import itertools


def pause():
    programPause = input("Press the <ENTER> key to continue...")


def calc_happy(t, dict):
    h = 0
    # print("Calc happy")
    for i in range(0, len(t) - 1):
        # print(t[i], t[i + 1])
        x = dict.get((t[i], t[i + 1]))
        y = dict.get((t[i + 1], t[i]))
        # print(x, y)
        h = h + x + y
    x = dict.get((t[0], t[-1]))
    y = dict.get((t[-1], t[0]))
    # print(x, y)
    h = h + x + y

    return h


def go(lines):
    people = set()

    pairs = defaultdict(int)

    for line in lines:
        c1, _, gain_loss, units, _, _, _, _, _, _, c2 = line.split()
        units = int(units)
        if gain_loss == "lose":
            units = units * -1
        # c1 = c1[:-1]
        c2 = c2[:-1]
        people.add(c1)
        people.add(c2)
        pairs[(c1, c2)] = units
        # pairs[(c2, c1)] = units
        # print(line)

    # Part 2
    for p in people:
        pairs[(p, "self")] = 0
        pairs[("self", p)] = 0

    people.add("self")
    # end part 2

    per = itertools.permutations(people)
    perm_list = []

    for val in per:
        happy = calc_happy(val, pairs)
        perm_list.append([val, happy])
        # print(*val, happy)
        # print(type(val))

    # print(perm_list)
    s_dist = 9999
    s_path = ""
    l_dist = 0
    l_path = ""
    for i in perm_list:
        # print(i)
        if i[1] < s_dist:
            s_dist = i[1]
            s_path = i[0]
        if i[1] > l_dist:
            l_dist = i[1]
            l_path = i[0]

    print("shortest {} {}".format(s_path, s_dist))
    print("Longest  {} {}".format(l_path, l_dist))


def main():
    file = "day13_input.txt"
    with open(file) as fp:
        lines = [line.strip() for line in fp]
    go(lines)
    sys.exit(1)

    return


if __name__ == "__main__":
    main()
