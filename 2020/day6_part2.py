#!/usr/bin/python


"""
--- Day 4: Passport Processing ---
Part 1
210 valid passports
Part 2
131 valid passports
"""

import sys
import re


def build_items(dict, line):
    for x in line:
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1


def process_items(dict, num):
    x = 0
    # print(num, dict)
    for key in dict:
        if dict[key] == num:
            x += 1
    return x


def main():
    count_questions = 0
    with open("day6_input.txt") as f:
        lines = f.readlines()
    # print(lines)

    group_dict = {}
    num_groups = 0
    for i, xline in enumerate(lines):
        # print(i, xline)
        line = xline.strip()
        if len(line) == 0:
            group_cnt = process_items(group_dict, num_groups)
            count_questions += group_cnt
            num_groups = 0
            group_dict = {}
        else:
            build_items(group_dict, line)
            num_groups += 1

    group_cnt = process_items(group_dict, num_groups)
    count_questions += group_cnt

    print("Total questions: {}".format(count_questions))

    sys.exit(1)


if __name__ == "__main__":
    main()
