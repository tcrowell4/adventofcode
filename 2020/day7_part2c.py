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

Part 2
Total bags: 30899
"""

import sys
import re


def build_items(line, pattern):
    holder = "empty"
    held = ""
    match = re.findall(pattern, line)

    if not match:
        return holder

    holder = match[0]
    match2 = re.findall("\d* \w* \w* bag", line)
    # print(match)
    return holder, match2


def process_items(lines, dict):
    more = 0
    pat_all_bags = "\w* \w* bag"

    for i, xline in enumerate(lines):
        # print(i, xline)
        # build the list of bags on the current line
        holder, bag_list = build_items(xline, pat_all_bags)
        dict[holder] = bag_list
    return more


def count_bags(dict, bag, num_bags, leader):
    global bag_count
    # print(">>>> count_bags {}".format(bag))
    xcount = 0
    if bag in dict:
        bags = dict[bag]
    else:
        return
    # print("bags = {} type(bags) = {}".format(bags, type(bags)))

    for held_bag in bags:
        total = 0
        print("{} >>> bags = {} count {}".format(leader, num_bags, bag_count))
        x = re.search(r"(\d*) (\w* \w* bag)", held_bag)
        # print(x)
        if x[0] == " no other bag":
            return
        print("{}bag: {} contains {} {}".format(leader, bag, x[1], x[2]))
        # bag_count += num_bags * int(x[1])
        bag_count += int(x[1])
        print("{} num_bags {}".format(leader, num_bags))
        for xxx in range(int(x[1])):
            count_bags(dict, x[2], int(x[1]), leader + "....")
        # count_bags(dict, x[2], int(x[1]), leader + "....")

        print("{} XCount = {} Count = {}".format(leader, xcount, bag_count))
        # print("{} XCount = {} Count = {}".format(leader, xcount, count))
    return

    # print(match)


def main():
    pat_all_bags = "\w* \w* bag"
    pat_shiny = "shiny gold bag"

    global bag_count
    bag_count = 0

    with open("day7_input.txt") as f:
        lines = f.readlines()
    # print(lines)

    bags_dict = {}
    primary_list = ["shiny gold bag"]

    num_groups = 0

    process_items(lines, bags_dict)
    # print("bag: {} contains {}".format(pat_shiny, bags_dict[pat_shiny]))
    count_bags(bags_dict, pat_shiny, 1, "")
    print("Total bags: {}".format(bag_count))
    # for key in sorted(bags_dict.keys()):
    #    print(key, bags_dict[key])

    sys.exit(1)


if __name__ == "__main__":
    main()
