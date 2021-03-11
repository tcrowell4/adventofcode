#!/usr/bin/python


import sys
import re
import hashlib


def rules(word):
    if re.search(r"ab|cd|pq|xy", word):
        return False
    match = re.findall(r"[aeiou]", word)
    if len(match) < 3:
        return False
    for i, w in enumerate(word):
        if i < len(word) - 1:
            if w == word[i + 1]:
                return True
        else:
            return False


def go(l):
    nice = 0
    for word in l:
        if rules(word):
            print("good {}".format(word))
            nice += 1
        else:
            print("bad {}".format(word))

    print("nice words", nice)


def parse(file):
    with open(file) as fp:
        lines = [line.strip() for line in fp]

    go(lines)

    return


def main():
    file = "day5_input.txt"
    parse(file)
    sys.exit(1)

    return


if __name__ == "__main__":
    main()
