#!/usr/bin/python

# aoc_day1_part1.py

import sys
import re

def go(l):
    floor = 0
    for x in l:
        if x == "(":
            floor += 1
        else:
            floor -= 1
    print("Final floor {} {}".format(floor, l))

def parse(file):
    # with open(file) as fp:
    #     lines = [line.strip() for line in fp]

    with open(file) as fp:
        line = fp.read().strip()
    # for line in lines:
        go(line)

    return


def main():
    file = "day1_input.txt"
    parse(file)
    sys.exit(1)

    return


if __name__ == "__main__":
    main()
