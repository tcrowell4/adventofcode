#!/usr/bin/python


import sys
import re
import hashlib


def rules(word):
    dbl_sw = False
    xyx_sw = False
    for i in range(len(word) - 2):
        if (m := re.findall(word[i : i + 2], word)) :
            if len(m) >= 2:
                print(i, m, word[i : i + 2])
                print("pair found", word, m)
                break
            else:
                print(i, m, word[i : i + 2])
    else:
        return False

    for i in range(len(word) - 2):
        if word[i] == word[i + 2]:
            print("repeat", word, word[i : i + 3])
            return True

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
