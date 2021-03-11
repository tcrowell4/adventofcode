#!/usr/bin/python


"""
--- Day 7: Handy Haversacks ---
primary_list 1 count = 17 more = 1
primary_list 2 count = 72 more = 1
primary_list 3 count = 128 more = 1
primary_list 4 count = 152 more = 1
primary_list 5 count = 159 more = 1
primary_list 6 count = 162 more = 1
primary_list 7 count = 162 more = 0
Total number of bags = 161  <=== because shiny gold is the seeded it has to be removed
"""

import sys
import re


def build_items(line, pattern):

    match = re.findall(pattern, line)
    if match:
        pass
    # print(match)
    return match


def process_items(lines, list):
    more = 0
    pat_all_bags = "\w* \w* bag"

    for i, xline in enumerate(lines):
        # print(i, xline)
        # build the list of bags on the current line
        bag_list = build_items(xline, pat_all_bags)
        for item in list:
            idx = bag_list.index(item) if item in bag_list else -1
            # print("idx {} pattern {}".format(idx, item))
            if idx > 0:
                # print("adding {} {}".format(idx, bag_list[0], bag_list[idx]))
                if bag_list[0] not in list:
                    list.append(bag_list[0])
                    more = 1
    return more


def main():
    pat_all_bags = "\w* \w* bag"
    pat_shiny = "shiny gold bag"

    count_questions = 0
    with open("day7_input.txt") as f:
        lines = f.readlines()
    # print(lines)

    bags_dict = {}
    primary_list = ["shiny gold bag"]

    num_groups = 0

    more = 1
    loops = 0
    while more:
        loops += 1
        more = process_items(lines, primary_list)
        print(
            "primary_list {} count = {} more = {}".format(
                loops, len(primary_list), more
            )
        )

        # print(primary_list)

    # process_items(lines, primary_list)
    # print("primary_list second time")
    # print(primary_list)
    primary_list.pop(0)
    print("Total number of bags = {}".format(len(primary_list)))

    sys.exit(1)


if __name__ == "__main__":
    main()
