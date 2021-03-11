#!/usr/bin/python


import sys
import re
import numpy as np
from collections import defaultdict
import itertools
import math


def pause():
    programPause = input("Press the <ENTER> key to continue...")


def score(time, rd, times):
    winner = []
    for name, v in rd.items():
        spd, fly, rst = v
        # x = the number of complete fly/rest periods
        x = int(time / (fly + rst))
        # distance flown for complete periods
        d = x * (spd * fly)
        # determine number of secs used for complete periods
        # determine remaining seconds
        # and calc the additional distance flown
        secs_used = x * (fly + rst)
        secs_remaining = time - secs_used
        if secs_remaining <= fly:
            d += secs_remaining * spd
        else:
            d += spd * fly

        times[name] = d
    top_key = max(times, key=lambda key: times[key])
    top_time = times[top_key]

    for k, v in times.items():
        if v == top_time:
            winner.append(k)
    # if len(winner) > 1:
    #     print("Tie {} {}".format(winner, time, top_time))

    return winner


def go(lines):
    time = 2503
    rd = defaultdict(int)
    times = defaultdict(int)
    scores = defaultdict(int)

    for line in lines:
        name, _, _, speed, units, _, duration, *_, rest, _ = line.split()
        speed = int(speed)
        rest = int(rest)
        duration = int(duration)
        rd[name] = (speed, duration, rest)

    for i in range(1, time + 1):
        names = score(i, rd, times)
        for name in names:
            scores[name] += 1
    winner = max(scores, key=lambda key: scores[key])
    print("winner  {} {}".format(winner, scores[winner]))
    print(scores)

    for k, v in times.items():
        print(k, v)
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
