#!/usr/bin/python

#aoc_day2_part2.py
"""
--- Part Two ---
While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?

Number of valid passwords is 352
Number of passwords is 1000
"""

import sys
import re

def process_rule(rule, letter, passwd):
    r = rule.split('-')
    first = int(r[0])
    second = int(r[1])

    if passwd[first-1] == letter and passwd[second-1] != letter:
        print("{} {} {} {}".format(first, second, letter, passwd))
        return(True)

    if passwd[first-1] != letter and passwd[second-1] == letter:
        print("{} {} {} {}".format(first, second, letter, passwd))
        return(True)

    return(False)




# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    num_valid = 0

    with open('day2_input.txt') as f:
        lines = f.readlines()
    #print(lines)
    for i, line in enumerate(lines):
        passrules = line.strip().split(' ')
        rule = passrules[0]
        rule_chr = passrules[1]
        passwd = passrules[2]
        if process_rule(rule, rule_chr[0], passwd):
        #print("Min={} Max={} {} {} {}".format(min, max, rule, rule_chr, passwd))
                num_valid += 1

    print("Number of valid passwords is {}".format(num_valid))
    print("Number of passwords is {}".format(len(lines)))

    sys.exit(1)

if __name__ == '__main__':
  main()
