#!/usr/local/bin/python
import sys
from itertools import combinations, permutations
from collections import defaultdict


def find_sum_in_list(numbers, target, num_properties):
    # results = []

    # results = [
    #     combo
    #     for combo in combinations(numbers, num_properties)
    #     if (sum(combo) == target)
    # ]

    results = result = [
        seq
        for i in range(len(numbers), 0, -1)
        for seq in combinations(numbers, i)
        if sum(seq) == target
    ]
    # print(results)
    print(len(results))
    return results


if __name__ == "__main__":
    # lines = [20, 15, 10, 5, 5]
    file = "day17_input.txt"

    with open(file) as fp:
        lines = [int(line.strip()) for line in fp]
    print(sorted(lines))

    set_containers = set(lines)
    # print(lines)
    print(sorted(set_containers))

    find_sum_in_list(lines, 150, len(lines))
    sys.exit()

    """
    ingredients dict uses an index as the key.
    The index represents the number of the ingredient



    length of sum_perms 48
    sum_perms is the number of combinations that add up to the target totals
    for the number of ingredients
    (3, 97)
    (4, 96)
    (5, 95)
... (47, 53)
    (48, 52)
    (49, 51)
    (50, 50)


    """
    for i, line in enumerate(lines):
        key, _, capacity, _, durability, _, flavor, _, texture, _, calories = line
        ingredients[i] = [
            key[:-1],
            int(capacity[:-1]),
            int(durability[:-1]),
            int(flavor[:-1]),
            int(texture[:-1]),
        ]

    print(ingredients)
    for k, v in ingredients.items():
        print(k, v)

    # create permutations of possible order of ingredients
    x = permutations(range(len(ingredients)))
    ingred_combos = []

    nums = list(range(1, 98))
    # find combinations adding to value restricted to number of entries
    sum_perms = []
    sp = find_sum_in_list(nums, 100, len(ingredients))

    for v in sp:
        sum_perms.append(v)

    print("length of sum_perms {}".format(len(sum_perms)))

    go(ingredients, sum_perms)
