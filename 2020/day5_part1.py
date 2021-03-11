#!/usr/bin/python


"""
--- Day 5: Binary Boarding ---
Part 1
Highest seat id is 826


Part 2 - Find seat
row 084 :000 :001 :002 :003 :004 :005 :007
row 84 seat 6
>>> (84*8)+6
678
"""

import sys
import re


def front_back(seat_pass):
    rows = [i for i in range(128)]
    x = len(rows)
    start = 0
    end = 128
    for fb in seat_pass[:7]:
        # print("Begin {} {}:{} ".format(fb, start, end))
        if fb == "F":
            end -= int(len(rows[start:end]) / 2)
        elif fb == "B":
            start += int(len(rows[start:end]) / 2)
        # print("End  : {} {}:{} ".format(fb, start, end))
        # print(rows[start:end])

    return rows[start:end][0]


def left_right(seat_pass):
    columns = [i for i in range(8)]
    x = len(columns)
    start = 0
    end = 8
    for lr in seat_pass[7:]:
        # print("Begin {} {}:{} ".format(lr, start, end))
        if lr == "L":
            end -= int(len(columns[start:end]) / 2)
        elif lr == "R":
            start += int(len(columns[start:end]) / 2)
        # print("End  : {} {}:{} ".format(lr, start, end))
        # print(columns[start:end])

    return columns[start:end][0]


def find_seat(seat_list):
    row = " "
    seat_string = "Starting row"
    for seat in seat_list:
        if seat[:3] != row:
            print(seat_string)
            # build next row
            row = seat[:3]
            seat_string = "row " + row + " " + seat[3:]
        else:
            seat_string = seat_string + " " + seat[3:]


def main():
    row_seat = []
    highest_id = 0
    with open("day5_input.txt") as f:
        lines = f.readlines()
        # print(lines)
    for i, xline in enumerate(lines):
        # print(i, xline)
        line = xline.strip()
        row = front_back(line)
        # print("The row number is {}".format(row))
        column = left_right(line)
        # print("The seat number is {}".format(column))
        seat_id = (row * 8) + column
        # print("Seat number {:03d}:{:03d} is Seat ID {}".format(row, column, seat_id))
        row_seat.append("{:03d}:{:03d}".format(row, column))
        if seat_id > highest_id:
            highest_id = seat_id

    print("Highest seat id is {}".format(highest_id))
    # print(sorted(row_seat))
    find_seat(sorted(row_seat))
    sys.exit(1)


if __name__ == "__main__":
    main()
