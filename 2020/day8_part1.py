#!/usr/bin/python

# aoc_day1_part1.py
"""

"""

import sys
import re


def process_operation(idx, op, arg):
    acc = 0
    if op == "acc":
        next_idx = idx + 1
        acc = arg
    elif op == "jmp":
        next_idx = idx + arg
        acc = 0
    elif op == "nop":
        next_idx = idx + 1
        acc = 0
    return next_idx, acc


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    accumulator = 0

    f = open("day8_input.txt")
    lines = f.readlines()
    # linelist = lines.split()

    # print(lines)

    # for i, line in enumerate(lines):
    #     # print(line, type(line))
    #     x = line.split()
    #     operation = x[0]
    #     argument = int(x[1])
    #     print("{} : {} ".format(operation, argument))

    code_idx = 0
    code_visits = len(lines) * ["*"]

    while True:
        if code_visits[code_idx] != "*":
            print("reached the loop: accumulator = {}".format(accumulator))
            print(code_idx, lines[code_idx].strip())
            print(code_visits)
            sys.exit(1)
        print(code_idx, lines[code_idx].strip())
        x = lines[code_idx].split()
        code_visits[code_idx] = x
        operation = x[0]
        argument = x[1]
        code_idx, acc_inc = process_operation(code_idx, operation, int(argument))
        # print("return values {} {} ".format(code_idx, acc_inc))

        accumulator += acc_inc
    print(code_visits)

    sys.exit(1)


if __name__ == "__main__":
    main()
