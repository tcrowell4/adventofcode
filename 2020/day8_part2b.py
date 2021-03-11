#!/usr/bin/python

# aoc_day1_part1.py
"""
--- Day 8: Handheld Halting ---
--- Part Two ---
After some careful analysis, you believe that exactly one instruction is corrupted.

Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp. (No acc instructions were harmed in the corruption of this boot code.)

The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in the file. By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.


>> 273:jmp:55
>> 273:jmp:55
>> nop +55
reached the end: accumulator = 1149
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


def find_loop(code_idx, code_visits, lines):
    global accumulator

    while True:
        if code_idx == len(lines):
            print("reached the end: accumulator = {}".format(accumulator))
            # print(code_visits)
            sys.exit(1)

        if code_visits[code_idx] != "*":
            print("reached the loop: accumulator = {}".format(accumulator))
            print("[{:03d}] {}".format(code_idx, lines[code_idx].strip()))
            # print(code_visits)
            return

        print("[{:03d}] {}".format(code_idx, lines[code_idx].strip()))
        x = lines[code_idx].split()
        code_visits[code_idx] = x
        operation = x[0]
        argument = x[1]
        # print("*** {} {} ".format(code_idx, len(lines)))

        next_idx, acc_inc = process_operation(code_idx, operation, int(argument))
        # print("*** {} {} {} ".format(code_idx, next_idx, len(lines)))
        # print("return values {} {} ".format(code_idx, acc_inc))

        code_idx = next_idx

        accumulator += acc_inc


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    global accumulator
    accumulator = 0

    f = open("day8_input.txt")
    lines = f.readlines()
    # linelist = lines.split()

    # print(lines)

    nop_jmp = []
    for i, line in enumerate(lines):
        # print(line, type(line))
        x = line.split()
        if line[:3] == "nop" or line[:3] == "jmp":
            operation = x[0]
            argument = int(x[1])
            print(">>", line)
            print(">> {}:{}:{} ".format(i, operation, argument))
            s = "{}:{}:{} ".format(i, operation, argument)
            nop_jmp.append(s)

            lines_copy = lines[:]
            if operation == "nop":
                lines_copy[i] = "jmp" + line[3:]
                print(">> {}:{}:{} ".format(i, operation, argument))
                print(">>", lines_copy[i])
            else:
                lines_copy[i] = "nop" + line[3:]
                print(">> {}:{}:{} ".format(i, operation, argument))
                print(">>", lines_copy[i])

            code_idx = 0
            accumulator = 0
            code_visits = len(lines) * ["*"]
            find_loop(code_idx, code_visits, lines_copy)

    print(nop_jmp)

    sys.exit(1)

    code_idx = 0
    code_visits = len(lines) * ["*"]
    find_loop(code_idx, code_visits, lines)
    # print(code_visits)

    sys.exit(1)


if __name__ == "__main__":
    main()
