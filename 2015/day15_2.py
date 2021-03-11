#!/usr/local/bin/python

from itertools import combinations_with_replacement, permutations
from collections import defaultdict


def find_sum_in_list(numbers, target, num_properties):
    # results = []

    results = [
        combo
        for combo in combinations_with_replacement(numbers, num_properties)
        if (sum(combo) == target)
    ]

    # print(results)
    return results


def go(ingredients, sum_perms):
    best_score = 0
    for x in sum_perms:
        sum_combo = [p for p in permutations(x)]
        score_tot = 0
        for i in sum_combo:
            # print("sum_combo", i)
            cap, dur, fla, tex, calories = 0, 0, 0, 0, 0
            for k, v in ingredients.items():
                ing, c, d, f, t, cal = v
                cap += i[k] * c
                dur += i[k] * d
                fla += i[k] * f
                tex += i[k] * t
                calories += i[k] * cal
                # print("{} {} {} {} {}".format(ing, cap, dur, fla, tex))

            if cap < 0:
                cap = 0
            if dur < 0:
                dur = 0
            if fla < 0:
                fla = 0
            if tex < 0:
                tex = 0

            score = cap * dur * fla * tex
            # print("Score: {}  {} {} {} {}".format(score, cap, dur, fla, tex))
            if (score > best_score) and (calories == 500):
                best_score = score
                best_str = "Combo {} Score {} Calories {}".format(i, score, calories)
    print("best_score", best_score)
    print(best_str)


if __name__ == "__main__":
    file = "day15_input.txt"
    ingredients = defaultdict(list)
    with open(file) as fp:
        lines = [line.strip().split() for line in fp]
    # print(lines)

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
            int(calories),
        ]

    # print(ingredients)
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
