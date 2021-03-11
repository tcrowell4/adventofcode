#!/usr/local/bin/python

import re
from collections import defaultdict


def go(sues, things, stats):
    for sue, value in sues.items():
        item1, v1, item2, v2, item3, v3 = value
        x = 0
        thing = things.get(item1)
        if thing == v1:
            x += 1
        thing = things.get(item2)
        if thing == v2:
            x += 1
        thing = things.get(item3)
        if thing == v3:
            x += 1
        stats[sue] = x

    for k, v in stats.items():
        if v == 3:
            print(k, v)


if __name__ == "__main__":
    file = "day16_input.txt"
    sues = defaultdict(int)
    # dict stat is for counting the number of matches between sender and sues
    stats = defaultdict(int)

    with open(file) as fp:
        lines = [line.strip() for line in fp]

    with open("day16_input2.txt") as f:
        things = {k[:-1]: int(v) for x in f for (k, v) in [x.strip().split()]}
        # lines = [x.strip() for x in f]
    # print(lines)

    for line in lines:
        m = re.search(r"(.*): (\w*): (\d*), (\w*): (\d*), (\w*): (\d*)", line)
        sue, b, bb, c, cc, d, dd = m.groups()
        bb = int(bb)
        cc = int(cc)
        dd = int(dd)

        sues[sue] = [b, bb, c, cc, d, dd]
        stats[sue] = 0

    for k, v in sues.items():
        print(k, v)
    for k, v in things.items():
        print(k, v)

    go(sues, things, stats)
