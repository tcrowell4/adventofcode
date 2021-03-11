#!/usr/bin/python

import sys
import pprint
import re
import numpy as np



def process_input(input):

    nearbytickets = []
    for ticket in input:
        s_values = ticket.split(",")
        values = list(map(int, s_values))
        nearbytickets.append(values)


    arr = np.array(nearbytickets)

    print(nearbytickets)
    print("array")
    print(arr)

    print()



    return


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.


def main():
    with open("day16_numpy.txt") as fp:
        lines = fp.readlines()
    # strip each line and break into individual characters
    input_list = list(map(lambda x: x.strip(), lines))
    # print(input_list)
    process_input(input_list)

    sys.exit(1)


if __name__ == "__main__":
    main()
