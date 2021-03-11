#!/usr/bin/python

# aoc_day1_part1.py

import sys
import re

def go(lines):
    # surface area of the box, which is 2*l*w + 2*w*h + 2*h*l
    # little extra paper for each present: the area of the smallest side
    """
    A present with dimensions 2x3x4
    requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper
    plus 6 square feet of slack, for a total of 58 square feet.
    """
    total_paper = 0
    total_ribbon = 0

    for i,x in enumerate(lines):

        print(x)
        l, w, h = x
        lw = 2*l*w
        lwp = 2*(l+w)
        wh = 2*w*h
        whp = 2*(w+h)
        hl = 2*h*l
        hlp = 2*(h+l)
        sq_ft = lw + wh + hl
        extra = min(int(lw/2),int(wh/2),int(hl/2))
        total = sq_ft + extra
        ribbon = min(lwp,whp,hlp) + (l*w*h)
        print("{} : sqft {} extra {} = {}".format(x, sq_ft, extra, total))
        print(lw,wh,hl)
        total_paper += total
        total_ribbon += ribbon

    print("Total required", total_paper, total_ribbon)

def parse(x):
    l, w, h = x.split("x")
    return int(l), int(w), int(h)



def main():
    file = "day2_input.txt"
    with open(file) as fp:
         lines = [parse(line.strip()) for line in fp]
    go(lines)
    sys.exit(1)

    return


if __name__ == "__main__":
    main()
