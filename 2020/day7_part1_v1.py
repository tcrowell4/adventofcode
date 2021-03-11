#!/usr/bin/python


"""
--- Day 6: Custom Customs ---
Total questions: 3125
"""

import sys
import re


def build_items(dict, line, pattern):

    match = re.findall(pattern, line)
    if match:
        pass
    # print(match)
    return match


def process_items(dict, num):
    x = 0
    # print(num, dict)
    for key in dict:
        if dict[key] == num:
            x += 1
    return x


def main():
    pat_all_bags = "\w* \w* bag"
    pat_shiny = "shiny gold bag"

    count_questions = 0
    with open("day7_input.txt") as f:
        lines = f.readlines()
    # print(lines)

    bags_dict = {}
    primary_list = []

    num_groups = 0
    for i, xline in enumerate(lines):
        # print(i, xline)
        # build_items(bags_dict, xline, pat_shiny)
        bag_list = build_items(bags_dict, xline, pat_all_bags)
        # idx = thing_list.index(elem) if elem in thing_list else -1
        idx = bag_list.index(pat_shiny) if pat_shiny in bag_list else -1
        # print("idx {} pattern {}".format(idx, pat_shiny))
        if idx > 0:
            # print("adding {} {}".format(idx, bag_list[0], bag_list[idx]))
            primary_list.append(bag_list[0])
    print("primary_list")
    print(primary_list)

    secondary_list = []
    for i, xline in enumerate(lines):
        # print(i, xline)
        # build_items(bags_dict, xline, pat_shiny)
        bag_list = build_items(bags_dict, xline, pat_all_bags)
        # idx = thing_list.index(elem) if elem in thing_list else -1
        for primary in primary_list:
            idx = bag_list.index(primary) if primary in bag_list else -1
            # print("idx {} pattern {}".format(idx, pat_shiny))
            if idx > 0:
                """
                print(
                    "adding secondary_list {} {} {}".format(idx, primary, bag_list[0])
                )
                """
                if bag_list[0] not in secondary_list:
                    secondary_list.append(bag_list[0])
    print("secondary_list")
    print(secondary_list)

    third_list = []
    for i, xline in enumerate(lines):
        # print(i, xline)
        # build_items(bags_dict, xline, pat_shiny)
        bag_list = build_items(bags_dict, xline, pat_all_bags)
        # idx = thing_list.index(elem) if elem in thing_list else -1
        for secondary in secondary_list:
            idx = bag_list.index(secondary) if secondary in bag_list else -1
            # print("idx {} pattern {}".format(idx, pat_shiny))
            if idx > 0:
                """
                print(
                    "adding third_list {} {} {}".format(idx, secondary, bag_list[0])
                )
                """
                if bag_list[0] not in third_list:
                    third_list.append(bag_list[0])

    print("third_list")
    print(third_list)

    fourth_list = []
    for i, xline in enumerate(lines):
        # print(i, xline)
        # build_items(bags_dict, xline, pat_shiny)
        bag_list = build_items(bags_dict, xline, pat_all_bags)
        # idx = thing_list.index(elem) if elem in thing_list else -1
        for item in third_list:
            idx = bag_list.index(item) if item in bag_list else -1
            # print("idx {} pattern {}".format(idx, pat_shiny))
            if idx > 0:
                """
                print(
                    "adding fourth_list {} {} {}".format(idx, item, bag_list[0])
                )
                """
                if bag_list[0] not in fourth_list:
                    fourth_list.append(bag_list[0])

    print("fourth_list")
    print(fourth_list)

    print("Total number of bags = {}".format(len(primary_list) + len(secondary_list)))

    sys.exit(1)


if __name__ == "__main__":
    main()
