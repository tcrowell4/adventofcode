#!/usr/bin/python

# aoc_day1_part1.py

import sys
import re
import hashlib

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

def go(l):
    floor = 0
    for secret_key in l:
        gen = infinite_sequence()
        while True:
            str2hash = "{}{}".format(secret_key, next(gen))
            x = hashlib.md5(str2hash.encode())
            md5hash = x.hexdigest()
            # print(".", end="")
            if md5hash.startswith("000000"):
                print("\n",str2hash,md5hash)
                break

def parse(file):
    with open(file) as fp:
        lines = [line.strip() for line in fp]

    go(lines)

    return


def main():
    file = "day4_input.txt"
    parse(file)
    sys.exit(1)

    return


if __name__ == "__main__":
    main()
