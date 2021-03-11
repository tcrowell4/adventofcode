#!/usr/bin/python

# aoc_day1_part1.py
"""

"""

import sys
import re

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    f = open("day1_input.txt", "rU")
    lines = f.readlines()
    # linelist = lines.split()
    print("***", lines[0])
    # print(lines)
    for i, year in enumerate(lines):
        y1 = int(year.strip())
        for x, year2 in enumerate(lines[i + 1 :]):
            y2 = int(year2.strip())
            print(y1, y2)
            if y1 + y2 == 2020:
                print("{} {} {}".format(y1, y2, y1 * y2))
                sys.exit()
    sys.exit(1)


if __name__ == "__main__":
    main()
