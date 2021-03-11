"""

https://github.com/npanuhin/Advent-of-Code/tree/master/2020/Day%2010

In Part 2, we were asked to count the total number of distinct ways one can arrange the adapters to connect the charging outlet to the device.

This puzzle can be solved using dynamic programming: let's count the number of ways one can arrange the adapters to connect the charging outlet to the current adapter.

Consider the current adapter with the X jolt output. The puzzle statement says that it can take from X - 3 to X - 1 jolts. Thus, the number of ways... is equal to the sum of the number of ways for adapters with values X - 3 to X - 1.

The last thing one must remember is storing an array for dynamic programming. I came to the conclusion that it's best to make a dictionary rather then a list, since in general the joltage value can be very large. In the implementation below, I used Python's defaultdict instead of a regular dict, because it allows to take a value for any key (returning the default value, in this case: 0).

"""

from collections import defaultdict

with open("day10_sample.txt", 'r', encoding="utf-8") as file:
    adapters = list(map(int, file.readlines()))

adapters.append(0)
adapters.sort()
adapters.append(adapters[-1] + 3)

ways = defaultdict(lambda: 0, {0: 1})


for adapter in adapters:
    
    for parent_adapter in range(adapter - 3, adapter):
        ways[adapter] += ways[parent_adapter]
        print(adapter,ways)

print(ways[adapters[-1]])