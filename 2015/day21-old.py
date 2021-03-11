# from 2020 day 11
import re
import sys
import collections


def pause():
    programPause = input("Press the <ENTER> key to continue...")


def shopitems(lines):

    shopitem_dict = {}
    for l in lines:
        dprint(l)
        key, cost, damage, armor = l
        shopitem_dict[key] = Shopitem(int(cost), int(damage), int(armor))

    for k, v in shopitem_dict.items():
        dprint(k, v)

    return shopitem_dict


def reverse_molecule(reverse_rules_dict, starting):
    s = starting[::-1]
    count = 0
    while len(s) > 1:
        for i, x in enumerate(s):
            for target, replace in reverse_rules_dict.items():
                if target == s[i : i + len(target)]:
                    count += 1
                    # dprint(
                    #     s,
                    #     "\n",
                    #     i,
                    #     x,
                    #     target,
                    #     len(target),
                    #     "=",
                    #     s[i : i + len(target)],
                    #     "*",
                    #     replace,
                    #     "*"
                    #     # s[i + 1 :],
                    # )
                    m = s[:i] + replace + s[i + len(target) :]
                    dprint("reverse: ==============")
                    dprint(m[i - 3 : i + 6])
                    dprint(m)
                    s = m
                    break
    dprint("Number of changes: {}".format(count))


def void(*args):
    pass


# used to control whether to debug print or not
dprint = print
# dprint = void


Shopitem = collections.namedtuple("Shopitem", "cost damage armor")


def main():

    # Armor = collections.namedtuple('Armor', 'cost damage armor')
    # Rings = collections.namedtuple('Rings', 'cost damage armor')

    with open("day20_input.txt") as fp:
        weapons, armor, rings, boss = fp.read().split("\n\n")

    # dprint(weapons, armor, rings, boss)

    regex = r"(\w+)\s+(\d+)\s+(\d+)\s+(\d+)"
    lines = [
        [m.group(1), m.group(2), m.group(3), m.group(4)]
        for x in weapons.split("\n")
        for m in [re.search(regex, x)]
        if m
    ]
    # lines = [x.strip().split() for x in weapons.split("\n")]
    weapons_dict = shopitems(lines)

    lines = [
        [m.group(1), m.group(2), m.group(3), m.group(4)]
        for x in armor.split("\n")
        for m in [re.search(regex, x)]
        if m
    ]
    # lines = [x.strip().split() for x in armor.split("\n")]
    armor_dict = shopitems(lines)
    armor_dict["No Armor"] = Shopitem(cost=0, damage=0, armor=0)

    regex = r"(\w+ .\d+)\s+(\d+)\s+(\d+)\s+(\d+)"
    lines = [
        [m.group(1), m.group(2), m.group(3), m.group(4)]
        for x in rings.split("\n")
        for m in [re.search(regex, x)]
        if m
    ]
    rings_dict = shopitems(lines)
    rings_damage_dict = {
        key: value for (key, value) in rings_dict.items() if key.startswith("Damage")
    }
    rings_damage_dict["Damage +0"] = Shopitem(cost=0, damage=0, armor=0)
    rings_defense_dict = {
        key: value for (key, value) in rings_dict.items() if key.startswith("Defense")
    }
    rings_defense_dict["Defense +0"] = Shopitem(cost=0, damage=0, armor=0)

    for i, v in rings_damage_dict.items():
        dprint(i, v)
    for i, v in rings_defense_dict.items():
        dprint(i, v)

    sys.exit()

    reverse_molecule(reverse_rules_dict, chunks[1].strip())
    # for x in s:
    #     dprint(x)


if __name__ == "__main__":
    main()
