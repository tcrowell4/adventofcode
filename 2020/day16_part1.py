#!/usr/bin/python

# aoc_day1_part1.py
"""

"""

import sys
import pprint
import re


def extract_range(range):
    # expect pattern ddd-ddd
    # extract into two decimal fields and return
    match = re.search(r"(\d*)-(\d*)", range)
    if match:
        # print(match.groups())
        return int(match[1]), int(match[2])


def process_notes(dict, fname, range1, range2):
    start, stop = extract_range(range1)
    r1 = list(range(start, stop + 1))
    start, stop = extract_range(range2)
    r2 = list(range(start, stop + 1))
    valid = list(set(r1 + r2))
    dict[fname] = valid
    return valid


def process_nearby(lines, valid_set):
    invalid = 0
    for ticket in lines:
        values = ticket.split(",")
        for v in values:
            if int(v) in valid_set:
                continue
            else:
                invalid += int(v)
    return invalid


def process_input(input):

    fields_dict = {}
    yourticket = []
    nearbytickets = []
    for line in input:
        if len(line) == 0:
            continue
        match = re.search(r"(\w*): (\d*-\d*) or (\d*-\d*)", line)
        if match:
            valid_range = process_notes(fields_dict, match[1], match[2], match[3])
            # print("valid_range {}".format(valid_range))
            continue
        if line.startswith("your ticket:"):
            sw = "your"
            continue
        if line.startswith("nearby tickets:"):
            sw = "nearby"
            continue
        if line[0].isdigit():
            if sw == "your":
                yourticket = line
            else:
                nearbytickets.append(line)

    pprint.pprint(fields_dict, width=200)
    dict_values = []
    for key in fields_dict:
        dict_values += fields_dict[key]
    print(dict_values)
    all_valid_set = set(dict_values)
    print("all_valid_set", all_valid_set)
    print("yourticket")
    print(yourticket)
    print("nearbytickets")
    print(nearbytickets)

    invalid = process_nearby(nearbytickets, all_valid_set)
    print("invalid", invalid)

    return


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.


def main():
    pp = pprint.PrettyPrinter(indent=4)
    with open("day16_input.txt") as fp:
        lines = fp.readlines()
    # strip each line and break into individual characters
    input_list = list(map(lambda x: x.strip(), lines))
    # print(input_list)
    process_input(input_list)

    sys.exit(1)


if __name__ == "__main__":
    main()
