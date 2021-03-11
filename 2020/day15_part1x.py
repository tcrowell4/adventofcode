#!/usr/bin/python

# aoc_day15_part1.py
"""

"""

import sys
import re
from collections import defaultdict


def difference_between_turns(t, current_turn):
    print("................difference_between_turns", t, current_turn)
    if len(t) == 0:
        return 0
    else:
        return t[-1] - t[-2]


def play_game(inp, turns):
    numbers = defaultdict(list)
    last_number_spoken = 0
    spoken_number = 0
    for i in range(1, turns + 1):
        print("============   Start Turn {}  ======================".format(i))
        print("numbers {}".format(numbers.items()))
        print("Last number spoken ", last_number_spoken)

        if i - 1 < len(inp):
            numbers[inp[i - 1]].append(i)
            last_number_spoken = inp[i - 1]
            print(">>>numbers {}".format(numbers.items()))
            print("Starting numbers:  Turn {} Number Spoken {}".format(i, inp[i - 1]))
            last_number_spoken = inp[i - 1]
            continue
        else:
            numbers[last_number_spoken].append(i)
            turn_list = numbers.get(last_number_spoken, [])

            last_number_spoken = difference_between_turns(turn_list, i)
            # numbers[spoken_number].append(i)
            # last_number_spoken = spoken_number

        print("End  Turn {} Next Number Spoken {}".format(i, last_number_spoken))


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    input = [0, 3, 6]
    turns = 10
    play_game(input, turns)
    sys.exit()


if __name__ == "__main__":
    main()
