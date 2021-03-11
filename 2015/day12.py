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


def dump_json(x, num_list):
    if isinstance(x, dict):
        for key, value in x.items():
            if isinstance(value, dict):
                dump_json(value, num_list)
            elif isinstance(value, list):
                dump_json(value, num_list)
            else:
                if type(value) == int:
                    num_list.append(value)
                print("key {!r} -> value {!r}".format(key, value))

                continue
    if isinstance(x, list):
        for value in x:
            if isinstance(value, dict):
                dump_json(value, num_list)
            elif isinstance(value, list):
                dump_json(value, num_list)
            else:
                if type(value) == int:
                    num_list.append(value)
                print("data {}".format(value))
                continue


def main():
    with open("day12.json", "r") as read_file:
        data = json.load(read_file)
    num_list = []
    dump_json(data, num_list)
    # print(num_list)
    print(sum(num_list))
    print(json.dumps(data, indent=4))

    # print(type(data))
    # for dx in data:
    #     if type(list):
    #         for x in dx:
    #             print(x)
    #     elif type(dict):
    #         for k, v in dx:
    #             print("k:v {}:{}".format(k, v))
    #     else:
    #         print(type(dx))

    # print(data)

    sys.exit(1)

    return


if __name__ == "__main__":
    main()
