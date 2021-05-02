import re
from itertools import combinations, chain
from heapq import heappop, heappush


generators, microchips = {}, {}
with open("2016/11.in") as f:
    for floor, line in enumerate(f):
        for microchip in set(re.findall(r"\w+(?=-comp)", line)):
            microchips[microchip] = floor

        for generator in set(re.findall(r"\w+(?=\ gen)", line)):
            generators[generator] = floor

pairs = [(microchips[i], generators[i]) for i in microchips]
# pairs.extend([(0, 0)]*2)  # uncomment for part 2
# sorting the tuples for the state check normalizes for the equivalent check??
pairs = tuple(sorted(pairs))
floor = distance = 0
state = [distance, floor, pairs]


to_visit = []
heappush(to_visit, state)
visited = set([(pairs, floor)])
while to_visit:
    distance, floor, pairs = heappop(to_visit)

    if all(i == 3 for pair in pairs for i in pair):
        break

    floors = [[], [], [], []]
    for element, (x, y) in enumerate(pairs):
        floors[x].append((element, 0))  # (element_index, type)
        floors[y].append((element, 1))

    # state check:
    # if the item type is 0 (microchip) and the corresponding generator is not
    # on the same floor and there are any other generators
    # then the chip is fried and this is not a valid state
    if any(
        i == 0 and (e, 1) not in things and any(j == 1 for _, j in things)
        for things in floors
        for e, i in things
    ):
        continue

    candidates = floors[floor]

    for floor in {min(floor + 1, 3), max(floor - 1, 0)} - set([floor]):
        # things is just a look up table used in the building of new_pairs
        for things in chain(
            map(lambda x: [x], candidates), combinations(candidates, 2)
        ):

            new_pairs = tuple(
                sorted(
                    tuple(
                        floor if (e, i) in things else old for i, old in enumerate(pair)
                    )
                    for e, pair in enumerate(pairs)
                )
            )

            if (new_pairs, floor) not in visited:
                heappush(to_visit, (distance + 1, floor, new_pairs))
                visited.add((new_pairs, floor))

print(distance)
