#!/usr/local/bin/python
import sys
from itertools import combinations, permutations
from collections import defaultdict


def find_sum_in_list(numbers, target, num_properties):

    results = result = [
        seq
        for i in range(len(numbers), 0, -1)
        for seq in combinations(numbers, i)
        if sum(seq) == target
    ]
    print(results)
    print(len(results))
    min_containers = min(results, key=len)
    print(min_containers)
    xy = 0
    for x in results:
        if len(x) == len(min_containers):
            xy += 1
    print(xy)
    return results


if __name__ == "__main__":
    # lines = [20, 15, 10, 5, 5]
    file = "day17_input.txt"

    with open(file) as fp:
        lines = [int(line.strip()) for line in fp]
    print(sorted(lines))

    find_sum_in_list(lines, 150, len(lines))
    sys.exit()
