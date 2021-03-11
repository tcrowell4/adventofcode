#!/usr/bin/python

# day19_part1.py
"""

"""

import sys
import pprint
import re
import numpy as np


def process_food(fooditems: list, allergens):
    sublist = {}
    final_allergan = {}
    foodlist = []
    for allergen in allergens:
        x = [food_item[1] for food_item in fooditems if allergen in food_item[0]]
        # print("allergen {} x {}".format(allergen, x))
        intersect = set(x[0]).intersection(*x)
        foods = [i for i in intersect]
        # print("foods {}".format(foods))
        sublist[allergen] = foods
        # print("foods {}".format(foods))
        foodlist.append(foods)
        print("allergen {} intersect {}".format(allergen, intersect))

    print("foodlist {}".format(foodlist))
    print("sublist")
    for i, v in sublist.items():
        print("allergen {} set {}".format(i, v))
        # print("set i[1] {}".format(set(i[1])))
        # intersect2 = set(i[1]).intersection(*foodlist)
        # print("allergen {} intersect2 {}".format(allergen, intersect2))

    sw = True
    while sw:
        sw = False
        for i, v in sublist.items():
            print("i:{} v:{}".format(i, v))
            if isinstance(v, list) and len(v) == 1:
                sublist[i] = v[0]  # change from list to string
                # if v[0] is in any other value item then remove it
                for x, y in sublist.items():
                    if isinstance(y, str):
                        continue  # skip if already a string
                    print("x:{} y:{} v:{}".format(x, y, v))
                    if (v[0] in y) and (len(y) > 1):
                        before = y
                        y.remove(v[0])
                        print("Key {} before {} after {}".format(x, before, y))
                        sublist[x] = y  # update with new food list
                        sw = True

    print("final sublist")
    for i, v in sublist.items():
        print("allergen {} set {}".format(i, v))

    return sublist


def process_input(lines: list):
    food = set()
    allergens = set()
    allitems = []
    sum = 0
    tile_dict = {}
    food_dict = {}

    for raw_line in lines:
        # print(raw_line)
        food.update([food_item for food_item in raw_line[0].strip().split(" ")])
        # build set of all allergens
        allergens.update(
            [
                allergens_item.strip("\) | \,")
                for allergens_item in raw_line[1].split(" ")
            ]
        )
        w_food = [food_item for food_item in raw_line[0].strip().split(" ")]
        for word in w_food:
            if word not in food_dict:
                food_dict[word] = 0
            food_dict[word] += 1
        # build allergens list for current line
        w_allergies = [
            allergens_item.strip("\) | \,") for allergens_item in raw_line[1].split(" ")
        ]
        # print("w_allergies", w_allergies)
        allitems.append((w_allergies, w_food))
    # print("food {}".format(food))
    # print("allergens {}".format(allergens))
    # print("allitems {}".format(allitems))

    allergens_identified = process_food(allitems, allergens)

    # remove
    allergen_str = ""
    for i in sorted(allergens_identified.keys()):
        v = allergens_identified[i]
        del food_dict[v]
        allergen_str += "{},".format(v)

    for i, v in food_dict.items():
        print("food {} : {}".format(i, v))
        sum = sum + v

    print("Sum {}".format(sum))
    print("allergens {}".format(allergen_str))


def main():
    with open("day21_input.txt", "r") as f:
        lines = [line.strip().split("(contains ") for line in f.readlines()]

    # print(tiles)
    process_input(lines)

    sys.exit(1)


if __name__ == "__main__":
    main()
