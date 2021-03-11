#!/usr/bin/python


"""
--- Day 6: Custom Customs ---
Total questions: 6430
"""

import sys
import re


def build_items(dict, line):
    for x in line:
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1


def process_items(dict):
    print(len(dict), dict)
    return len(dict)


def main():
    count_questions = 0
    with open("day6_input.txt") as f:
        lines = f.readlines()
    # print(lines)

    group_dict = {}
    for i, xline in enumerate(lines):
        # print(i, xline)
        line = xline.strip()
        if len(line) == 0:
            group_cnt = process_items(group_dict)
            count_questions += group_cnt
            group_dict = {}
        else:
            build_items(group_dict, line)

    group_cnt = process_items(group_dict)
    count_questions += group_cnt

    print("Total questions: {}".format(count_questions))

    sys.exit(1)


if __name__ == "__main__":
    main()
