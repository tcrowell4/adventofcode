#!/usr/bin/python

# day19_part1.py
"""

"""

import sys
import pprint
import re


def process_rules(rules, key, processed_rules, depth):
    z = True
    s = ""
    depth += 1
    if depth > 15:
        return s
    while z:
        values = rules.get(key)
        # print("==============")
        # print("k:values {}:{}".format(key, values))
        # s = s + " "
        if values:
            for v in values:
                # print("key:{} v:{}".format(key, v))
                if v.isdigit():
                    # print("process next rule {}".format(v))
                    x = process_rules(rules, v, processed_rules, depth)
                    s = s + x
                    print("process      rule {} x:{} ".format(v, x))
                    processed_rules[v] = x
                    # print("process      rule {} x:{} s:{}".format(v, x, s))
                    z = False  # continue
                elif v == "|":
                    s = s + v
                    continue
                else:
                    # print("found v {}".format(v))
                    z = False
                    s = s + v[1]
        if len(s) > 1:
            s = "({})".format(s)
    return s


def process_input(fields, messages):
    sum = 0
    replacement = ["8: 42 | 42 8", "11: 42 31 | 42 11 31"]

    rules = dict()
    sorted_rules = {}
    for line in fields:
        key, values = line.split(": ")
        rules[key] = list(values.split(" "))
        # rules[key] = [list(map(int, r.split('-'))) for r in ranges.split('or')]

    for line in replacement:
        key, values = line.split(": ")
        rules[key] = list(values.split(" "))

    print(rules)
    pattern_string = process_rules(rules, "0", sorted_rules, 0)
    print("Final", pattern_string)

    pattern = re.compile(pattern_string)

    for message in messages:
        if re.fullmatch(pattern, message):
            sum += 1

    print("Sorted Ruleset")
    for k in sorted(sorted_rules.keys()):
        print("{} : {}".format(k, sorted_rules[k]))

    return sum


def main():
    with open("day19_input.txt", "r") as f:
        rules, messages = [row.split("\n") for row in f.read().strip().split("\n\n")]

    print(rules)
    print(messages)
    sum = process_input(rules, messages)
    print(">>>>>>>>>>>>>  Sum Total {}".format(sum))

    sys.exit(1)


if __name__ == "__main__":
    main()
