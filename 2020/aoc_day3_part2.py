#!/usr/bin/python

# aoc_day3_part1.py
"""
--- Day 3: Toboggan Trajectory ---
With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy, it's certainly not safe: there's very minimal steering and the area is covered in trees. You'll need to see which angles will take you near the fewest trees.

Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your puzzle input) of the open squares (.) and trees (#) you can see. For example:

..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times:

..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
In this example, traversing the map using this slope would cause you to encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?

--- Part Two ---

Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?

0 [1, 1]
Right: 1 Down: 1 Number of trees hit is 78
1 [3, 1]
Right: 3 Down: 1 Number of trees hit is 262
2 [5, 1]
Right: 5 Down: 1 Number of trees hit is 66
3 [7, 1]
Right: 7 Down: 1 Number of trees hit is 69
4 [1, 2]
Right: 1 Down: 2 Number of trees hit is 29
Total Number of trees hit is 504
Answer: 2698900776
"""

import sys
import re


def process_slope(slope_right, slope_down, lines):
    trees_hit = 0
    row = 0
    col = 0
    line_length = len(lines[0].strip())

    while row + slope_down < len(lines):
        row += slope_down
        if col + slope_right < line_length:
            col += slope_right
        else:
            col = col + slope_right - line_length
        # print("..../..../..../..../..../..../..../..../")
        # print(lines[row].strip())
        # print("{}:{} value {}".format(row, col, lines[row][col]))
        if lines[row][col] == "#":
            trees_hit += 1
            # print("Hit {}:{} value {}".format(row, col, lines[row][col]))
    return trees_hit


def main():
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    # slopes = [[3, 1]]
    total_trees_hit = 0
    hit_values = []

    with open("day3_input.txt") as f:
        lines = f.readlines()
    # print(lines)

    for i, slope in enumerate(slopes):
        print(i, slope)
        right, down = slope
        hits = process_slope(right, down, lines)
        total_trees_hit += hits
        print("Right: {} Down: {} Number of trees hit is {}".format(right, down, hits))
        hit_values.append(hits)

    print("Total Number of trees hit is {}".format(total_trees_hit))

    x = 0
    for h in hit_values:
        if x == 0:
            x = h
        else:
            x = x * h
    print("Answer: {}".format(x))

    sys.exit(1)


if __name__ == "__main__":
    main()
