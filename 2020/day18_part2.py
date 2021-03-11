#!/usr/bin/python

# aoc_day1_part1.py
"""

"""

import sys
import pprint
import re

import logging


def domath(a, b, op):

    if op == "+":
        return a + b
    elif op == "*":
        return a * b


# Function to find precedence
# of operators.
def precedence(op):

    if op == "+" or op == "-":
        return 2
    if op == "*" or op == "/":
        return 1
    return 0


def solve(tokens):
    level = 0
    logging.debug(" ===   tokens === {}".format(tokens))
    stack = []
    ops_stack = []
    i = 0

    while i < len(tokens):
        logging.debug("While loop i:{} {} {} {}".format(i, tokens[i], stack, ops_stack))
        if tokens[i] == " ":
            i += 1
            continue

        elif tokens[i].isdigit():
            stack.append(int(tokens[i]))

        # Current token is an opening
        # brace, push it to 'ops'
        elif tokens[i] == "(":
            ops_stack.append(tokens[i])

        # Closing brace encountered,
        # solve entire brace.
        elif tokens[i] == ")":
            logging.debug("close: stack {}, ops {}".format(stack, ops_stack))

            while len(ops_stack) != 0 and ops_stack[-1] != "(":

                val2 = stack.pop()
                val1 = stack.pop()
                op = ops_stack.pop()

                stack.append(domath(val1, val2, op))
                # pop opening brace.
            ops_stack.pop()

        # Current token is an operator.
        else:

            # While top of 'ops' has same or
            # greater precedence to current
            # token, which is an operator.
            # Apply operator on top of 'ops'
            # to top two elements in values stack.
            while len(ops_stack) != 0 and precedence(ops_stack[-1]) >= precedence(
                tokens[i]
            ):

                val2 = stack.pop()
                val1 = stack.pop()
                op = ops_stack.pop()

                stack.append(domath(val1, val2, op))

            # Push current token to 'ops'.
            ops_stack.append(tokens[i])

        logging.debug("While END Stack: {}  {}".format(stack, ops_stack))

        i += 1
    # Entire expression has been parsed
    # at this point, apply remaining ops
    # to remaining values.
    while len(ops_stack) != 0:

        val2 = stack.pop()
        val1 = stack.pop()
        op = ops_stack.pop()

        stack.append(domath(val1, val2, op))

    # Top of 'stack' contains result,
    # return it.
    return stack[-1]


def process_input(lines):
    sum = 0

    for line in lines:
        ans = solve(line)
        sum += ans
        logging.info("=================== {} ".format(ans))
        logging.info("===================")

    return sum


def main():
    logging.basicConfig(
        # level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
        level=logging.INFO,
        format="%(levelname)s - %(message)s",
    )
    # x = ["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]
    #
    # sum = process_input(x)
    # logging.debug(">>>>>>>>>>>>>  Sum Total {}".format(sum))
    # sys.exit(1)

    with open("day18_input.txt") as fp:
        lines = fp.readlines()
    # strip each line and break into individual characters
    input_list = list(map(lambda x: x.strip(), lines))
    # logging.debug(input_list)
    sum = process_input(input_list)
    print(">>>>>>>>>>>>>  Sum Total {}".format(sum))

    sys.exit(1)


if __name__ == "__main__":
    main()
