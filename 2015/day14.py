#!/usr/bin/python


import sys
import re
import numpy as np
from collections import defaultdict
import itertools


def pause():
    programPause = input("Press the <ENTER> key to continue...")


def calc_happy(t, dict):
    h = 0
    # print("Calc happy")
    for i in range(0, len(t) - 1):
        # print(t[i], t[i + 1])
        x = dict.get((t[i], t[i + 1]))
        y = dict.get((t[i + 1], t[i]))
        # print(x, y)
        h = h + x + y
    x = dict.get((t[0], t[-1]))
    y = dict.get((t[-1], t[0]))
    # print(x, y)
    h = h + x + y

    return h


def go(lines):
    time = 2503
    rd = defaultdict(int)
    times = defaultdict(int)

    for line in lines:
        name, _, _, speed, units, _, duration, *_, rest, _ = line.split()
        speed = int(speed)
        rest = int(rest)
        duration = int(duration)
        rd[name] = (speed, duration, rest)

    for name, v in rd.items():
        spd, dur, rst = v
        d = 0
        fly = 1  # switch to fly
        r = dur  # time to start resting

        for i in range(time):
            if i % 100 == 0:
                print("fly", i, fly, r, d)
            if i == r:
                if fly:
                    fly = 0  # start resting
                    r = i + rst  # rest until time to flying
                else:
                    fly = 1
                    r = i + dur

            if fly:
                d += spd
        times[name] = d
        print(name, d)

        winner = max(times, key=lambda key: times[key])
    print("winner  {} {}".format(winner, times[winner]))


def main():
    file = "day14_input.txt"
    with open(file) as fp:
        lines = [line.strip() for line in fp]
    go(lines)
    sys.exit(1)

    return


if __name__ == "__main__":
    main()
