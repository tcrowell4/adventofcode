#!/usr/bin/python

# aoc_day1_part1.py
"""
--- Day 10: Adapter Array ---
Patched into the aircraft's data port, you discover weather forecasts of a massive tropical storm. Before you can figure out whether it will impact your vacation plans, however, your device suddenly turns off!

Its battery is dead.

You'll need to plug it in. There's only one problem: the charging outlet near your seat produces the wrong number of jolts. Always prepared, you make a list of all of the joltage adapters in your bag.

Each of your joltage adapters is rated for a specific output joltage (your puzzle input). Any given adapter can take an input 1, 2, or 3 jolts lower than its rating and still produce its rated output joltage.

In addition, your device has a built-in joltage adapter rated for 3 jolts higher than the highest-rated adapter in your bag. (If your adapter list were 3, 9, and 6, your device's built-in adapter would be rated for 12 jolts.)

Treat the charging outlet near your seat as having an effective joltage rating of 0.

Since you have some time to kill, you might as well test all of your adapters. Wouldn't want to get to your resort and realize you can't even charge your device!

If you use every adapter in your bag at once, what is the distribution of joltage differences between the charging outlet, the adapters, and your device?

Answer
75*32
2400
"""

import sys
import re


def process_adapters(adapters):
    j1 = 0
    j3 = 0
    # print(adapters)
    # preamble_length = len
    # for i, adapter in enumerate(adapters):
    #    print(adapter)
    # print("len(adapters) {}".format(len(adapters)))

    idx = 0
    next_idx = 0
    global valid_combos

    while idx < len(adapters):
        current_adapter = adapters[idx]
        # print("Current_adapter {}".format(current_adapter))
        next_idx = idx + 1
        while next_idx < len(adapters):
            """
            print(
                ">>>jolt idx {} nxt {} nextadap{} curr{} diff{}".format(
                    idx,
                    next_idx,
                    adapters[next_idx],
                    current_adapter,
                    adapters[next_idx] - current_adapter,
                )
            )
            """
            jolt_diff = adapters[next_idx] - current_adapter
            if jolt_diff <= 3:
                """
                print(
                    "jolt diff = {} ..... {} {} ".format(
                        adapters[next_idx] - current_adapter,
                        adapters[next_idx],
                        current_adapter,
                    )
                )
                """
                if jolt_diff == 1:
                    # next_list = adapters[:next_idx] + adapters[next_idx:]
                    next_list = adapters[:]
                    next_list.pop(next_idx)
                    print("Next iteration: {}".format(next_list))
                    ret = process_adapters(next_list)
                    if ret:
                        # print("*****", ret)
                        valid_combos.append(ret)
                    # since valid jolt found go to next entry
                break
            else:
                # anything greater than 3 won't work
                # print("invalid joltage {}".format(jolt_diff))
                return 0
            next_idx += 1

        idx = next_idx

    return adapters


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    global valid_combos
    valid_combos = []
    lines = []
    lines.append(0)  # set to initial value
    with open("day10_sample.txt") as fp:
        for line in fp:
            lines.append(int(line.strip()))
    slines = sorted(lines)
    end = int(slines[-1]) + 3

    slines.append(end)

    ret = process_adapters(slines)
    print(ret)

    z = " "

    total = 1
    for x in sorted(valid_combos):
        if x != z:
            print(x)
            total += 1
            z = x
        else:
            print("dupe", x)

    print(total)

    sys.exit(1)

    return


if __name__ == "__main__":
    main()
