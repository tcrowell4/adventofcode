#!/usr/bin/python

# aoc_day1_part1.py
"""
--- Day 9: Encoding Error ---
With your neighbor happily enjoying their video game, you turn your attention to an open data port on the little screen in the seat in front of you.

Though the port is non-standard, you manage to connect it to your computer through the clever use of several paperclips. Upon connection, the port outputs a series of numbers (your puzzle input).

The data appears to be encrypted with the eXchange-Masking Addition System (XMAS) which, conveniently for you, is an old cypher with an important weakness.

XMAS starts by transmitting a preamble of 25 numbers. After that, each number you receive should be the sum of any two of the 25 immediately previous numbers. The two numbers will have different values, and there might be more than one such pair.
"""

import sys
import re


def process_next_num(lines, preamble_length):
    # print(line, type(line))
    # preamble_length = len
    next_idx = preamble_length + 1
    while next_idx < len(lines):
        preamble = lines[next_idx - preamble_length : next_idx]
        # print(preamble)
        ret, invalid = process_preamble(preamble, lines[next_idx], next_idx)

        if ret == False:
            return False, invalid
        next_idx += 1
    return


def process_preamble(preamble, next_num, idx):
    # print("next_num = {} preamble = {}".format(next_num, preamble, idx))
    for num in preamble:
        if next_num - num in preamble:
            """
            print(
                "valid:  {} = {}+ {}".format(
                    next_num, num, preamble[preamble.index(next_num - num)]
                )
            )
            """
            return True, next_num

    print("{} is not valid".format(next_num))
    return False, next_num


def find_invalid_sums(invalid, lines):
    idx = 0
    next_idx = 0
    sums = 0
    sum_list = []
    while idx < len(lines):
        sums += lines[idx]
        sum_list.append(lines[idx])
        # print("sums {} lines[idx] {} sum_list {}".format(sums, lines[idx], sum_list))
        if sums > invalid:
            next_idx += 1
            sums = 0
            sum_list = []
            idx = next_idx
            continue
        if sums == invalid:
            print("Consecutive Sums found {}".format(sum_list))
            return sum_list
        else:
            idx += 1


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    lines = []
    with open("day9_input.txt") as fp:
        for line in fp:
            lines.append(int(line.strip()))

    ret, invalid = process_next_num(lines, 25)
    if ret == False:
        print("{} is not valid".format(invalid))
        # Part 2
        sum_list = find_invalid_sums(invalid, lines)
        max_num = max(sum_list)
        min_num = min(sum_list)
        print("Maximum element in the list is :", max_num)
        print("Minimum element in the list is :", min_num)
        print("Sum = {} + {} = {}".format(max_num, min_num, max_num + min_num))

    return


if __name__ == "__main__":
    main()
