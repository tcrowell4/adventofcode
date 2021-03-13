import re
import numpy as np

"""
--- Day 8: Two-Factor Authentication ---
Create the initial array  rows=6, cols = 50
a1 = np.zeros((6,50),dtype=int)

>>> ashape = (3,7)
>>> a1 = np.zeros(ashape,dtype=int)
>>> a1
array([[0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0]])


rect command will create a subarray based on the rectangle size

rect 3x2 = 3 cols x 2 rows

>>> # rect 3x2 = 3 cols x 2 rows
>>> a1[:2,:3].fill(1)
>>> a1
array([[1, 1, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0]])


rotate the column or row as required with the roll command
numpy.roll(a, shift, axis=None)

axis 0 == vertical
axis 1 == horizontal


for roll to work the row or col to be rotated must also be a new subarray
rotate column x=1
np.roll won't update the array directly.

>>> # rotate column x=1 by 1
>>> a1[:,1] = np.roll(a1[:,1],1)
>>> a1
array([[1, 0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 0]])

>>> # rotate row y=0 by 4
>>> a1[0] = np.roll(a1[0], 4)
>>> a1
array([[0, 0, 0, 0, 1, 0, 1],
       [1, 1, 1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 0]])

>>> # rotate column x=1 by 1
>>> a1[:,1] = np.roll(a1[:,1],1)
>>> a1
array([[0, 1, 0, 0, 1, 0, 1],
       [1, 0, 1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 0]])
>>>

a3[]



"""


def void(*args):
    pass


# used to control whether to debug print or not
dprint = void
# dprint = print


def validate_ABBA(entry):
    # dprint(entry)
    for i, ch in enumerate(entry):
        # dprint(entry[i : i + 4], entry[i : i + 2], entry[i + 3 : i + 1 : -1])
        if len(entry[i:]) < 4:
            return False
        if entry[i] == entry[i + 1]:
            continue

        if entry[i : i + 2] == entry[i + 3 : i + 1 : -1]:
            dprint("valid ABBA", entry)
            return True
    else:
        return False


def process_input(lines, screen_size, part):
    print("======== Part 1 ==========")
    a1 = np.zeros(screen_size, dtype=int)
    for line in lines:
        if len(line) == 2:
            cmd, rect = line
            cols, rows = rect.split("x")
            cols = int(cols)
            rows = int(rows)
            a1[:rows, :cols].fill(1)
            dprint(cmd, rect, rows, cols, a1.sum())
        else:
            # ['rotate', 'column', 'x=1', 'by', '3']
            rotate, row_col, row_col_idx, _, amount = line
            row_col_idx = int(row_col_idx[2:])
            amount = int(amount)
            dprint(rotate, row_col, row_col_idx, _, amount)
            if row_col == "row":
                a1[row_col_idx] = np.roll(a1[row_col_idx], amount)
            else:
                a1[:, row_col_idx] = np.roll(a1[:, row_col_idx], amount)

    print("{} Pixels on {} ".format(part, a1.sum()))

    print("======== Part 2 ==========")

    scr_ht, scr_wid = screen_size
    for i in range(scr_ht):
        code = []
        for j in range(scr_wid):
            if a1[i, j]:
                code.append("#")
            else:
                code.append(" ")
        else:
            print("".join(code))


def main():

    part1 = (6, 50)
    part2 = (6, 5)

    with open("8.in") as fp:
        lines = [line.strip().split() for line in fp]
    # print("=========", lines)
    process_input(lines, part1, "part 1")
    # process_input(lines, part2, "part 2")

    return


if __name__ == "__main__":
    main()
