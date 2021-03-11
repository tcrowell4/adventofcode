#!/usr/bin/python

# aoc_day1_part1.py
"""

"""

import sys
import pprint
import re


def domath(a, op, b):
    print(a, op, b)
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b


def solve(problem):
    print("===   problem === {}".format(problem))
    stack = []
    i = 0
    while i < len(problem):
        print(stack)
        a = problem[i]

        if a.isdigit():
            stack.append(int(a))

        if a in ["+", "-", "*"]:
            stack.append(a)

        if a == "(":
            # outer = re.compile("\((.+)\)")
            print(problem[i:])
            inc = len(problem[i:])
            # m = outer.search(problem[i:])
            a, inc = solve(problem[i + 1 :])
            i += inc
            stack.append(a)
        if a == ")":
            print("close: stack {}, inc {}".format(stack, i))
            return stack.pop(), i + 1

        print("Stack:  {}".format(stack))

        if len(stack) == 3:
            v1, op, v2 = stack.pop(), stack.pop(), stack.pop()
            z = domath(v1, op, v2)
            stack.append(z)

        if a == " ":
            pass

        i += 1

    return stack.pop(), 0


def process_input(lines):
    sum = 0
    for line in lines:
        ans, inc = solve(line)
        sum += ans
        print(ans)

    return sum


def main():

    with open("day18_input.txt") as fp:
        lines = fp.readlines()
    # strip each line and break into individual characters
    input_list = list(map(lambda x: x.strip(), lines))
    # print(input_list)
    sum = process_input(input_list)
    print("Sum Total {}".format(sum))

    sys.exit(1)


if __name__ == "__main__":
    main()
