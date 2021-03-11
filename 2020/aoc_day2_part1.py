#!/usr/bin/python

# aoc_day2_part1.py
"""
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
"""

import sys
import re


def process_rule(rule, letter, passwd):
    r = rule.split("-")
    min = int(r[0])
    max = int(r[1])

    i = 0
    for x in passwd:
        if x == letter:
            i += 1

    # print(">>>>>{} {} {} {} {}".format(min, max, i, letter, passwd))
    if i >= min and i <= max:
        print(">>>>>{} {} {} {} {}".format(min, max, i, letter, passwd))
        return True

    return False


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    num_valid = 0

    with open("day2_input.txt") as f:
        lines = f.readlines()
    # print(lines)
    for i, line in enumerate(lines):
        passrules = line.strip().split(" ")
        rule = passrules[0]
        rule_chr = passrules[1]
        passwd = passrules[2]
        if process_rule(rule, rule_chr[0], passwd):
            # print("Min={} Max={} {} {} {}".format(min, max, rule, rule_chr, passwd))
            num_valid += 1

    print("Number of valid passwords is {}".format(num_valid))
    print("Number of passwords is {}".format(len(lines)))

    sys.exit(1)


if __name__ == "__main__":
    main()
