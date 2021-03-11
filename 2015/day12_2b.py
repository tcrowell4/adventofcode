#!/usr/bin/python
# The performance with this one is tremendous as opposed to the others
# The difference is changing the string to a list.  I would have to presume
# that the difference between append and extend is that much better.

import sys
import re
import json


def pause():
    programPause = input("Press the <ENTER> key to continue...")


def go(lines, count):
    for line in lines:
        xline = [x for x in line]
        print("\n*********", xline)

        for i in range(count):
            if i % 5 == 0:
                print(">>  loopcount = {}  ".format(i))
            xline = looksay(xline)
            # print("<<", len(xline), xline)
        print("\n", len(xline))


def get(file):

    go(lines)

    return


def dump_json(x, indent, s=0):
    tmp = []
    indent = indent + 2
    # print(type(x), x)
    if type(x) == int:
        return x
    if isinstance(x, dict):

        for key, value in x.items():
            if value == "red":
                print("RED+++++++++<<<<<<<<<<<<<<<<<<<")
                return 0
            print("{}key {!r} -> value {!r}".format(" " * indent, key, value))
            s += dump_json(value, indent)

    if isinstance(x, (list, tuple)):
        for value in x:
            print("{}data {}".format(" " * indent, value))
            s += dump_json(value, indent)
    return s


def main():
    with open("day12.json", "r") as read_file:
        data = json.load(read_file)
    num_list = []
    total = dump_json(data, 0)
    print("Total= {}".format(total))

    sys.exit(1)

    return


if __name__ == "__main__":
    main()
