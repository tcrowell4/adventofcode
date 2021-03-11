#!/usr/bin/python

# aoc_day1_part1.py
"""

"""

import sys
import pprint
import re
import numpy as np
from collections import defaultdict


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
    valid_nearby = []
    invalid = 0
    for ticket in lines:
        values = ticket.split(",")
        ticket_valid = True
        for v in values:
            if int(v) not in valid_set:
                invalid += int(v)
                ticket_valid = False
                continue
        print("invalid", invalid)
        if ticket_valid:
            valid_nearby.append(ticket)
    return invalid, valid_nearby


def process_valid_nearby(lines, fields):
    dict_ticket_positions = defaultdict(list)

    nearbytickets = []
    for ticket in lines:
        s_values = ticket.split(",")
        values = list(map(int, s_values))
        nearbytickets.append(values)

    arr = np.array(nearbytickets)
    rows, cols = arr.shape
    print(rows, cols, arr.shape)

    for key in fields:
        dict_values = fields[key]
        lastkey = key
        key_cnt = 0
        print("======  checking  Key {}".format(key))
        for i in range(cols):
            # print(">>>>", i, cols)
            # print("==== column {}".format(i))
            curr_col = arr[:, i]
            set_col = set(curr_col)
            set_dv = set(dict_values)
            if set_col.issubset(set_dv):
                key_cnt += 1
                print("Count = {:<2}  key: {:<20} column {:<2}".format(key_cnt, key, i))
                dict_ticket_positions[key].append(i)
                # print("..... set_col {}".format(set_col))
                # print("..... set_dv {}".format(set_dv))
    dict_order = find_ticket_order(dict_ticket_positions)
    # for v in values:
    #     find_valid_fields(values)
    #     if int(v) not in valid_set:
    #         invalid += int(v)
    #         ticket_valid = False
    #         continue
    return dict_order


def find_ticket_order(dTickets):
    order = {}
    new_order = {}
    used_cols = []

    for k, v in dTickets.items():
        print(len(v), k, ">", v)
        order[len(v)] = (k, v)

    for k in sorted(order.keys()):
        print(k, ">", order[k])
        key, values = order[k]
        diff = list(diff_between_lists(used_cols, values))
        print(diff, used_cols, values)
        used_cols = values
        new_order[k] = key, diff[0]

    print("==== new_order =====")
    for k in sorted(new_order.keys()):
        print(k, ">", new_order[k])

    return new_order


def diff_between_lists(first_list, sec_list):
    # Convert lists to sets
    first_set = set(first_list)
    sec_set = set(sec_list)
    # Get the differences between two sets
    differences = (first_set - sec_set).union(sec_set - first_set)
    return differences


def process_input(input):

    fields_dict = {}
    yourticket = []
    nearbytickets = []
    for line in input:
        if len(line) == 0:
            continue
        match = re.search(r"(.*): (\d*-\d*) or (\d*-\d*)", line)
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

    # pprint.pprint(fields_dict, width=200)
    dict_values = []
    for key in fields_dict:
        dict_values += fields_dict[key]
        print(key, fields_dict[key])
    all_valid_set = set(dict_values)
    # print("all_valid_set", all_valid_set)
    # print("yourticket")
    # print(yourticket)
    # print("nearbytickets")
    # print(nearbytickets)

    invalid, valid_nearby = process_nearby(nearbytickets, all_valid_set)
    print("invalid", invalid)

    print("valid_nearby", valid_nearby)

    ### Part 2
    field_order = process_valid_nearby(valid_nearby, fields_dict)
    ans = []
    answer = 0
    yt = yourticket.split(",")
    yt = list(map(int, yt))
    print("Your ticket", yt)
    for k in sorted(field_order.keys()):
        xfield, v = field_order[k]
        # print(xfield, v)
        if xfield.startswith("departure"):
            print("******", k, ">", xfield, v, yt[v], v)
            ans.append(yt[v])
    print("Departures", ans)
    answer = 1
    for x in ans:
        answer = x * answer

    print(answer)

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
