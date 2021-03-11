# from 2020 day 11
import re
import sys
import collections
from itertools import permutations
from itertools import combinations
from itertools import product


def void(*args):
    pass


# used to control whether to debug print or not
# dprint = print
dprint = void


class Player:
    def __init__(self, hit_points, damage=0, armor=0):
        self.init_hit_points = hit_points
        self.init_damage = damage
        self.init_armor = armor
        self.reset()

    def __repr__(self):
        rep = "Hit Points {}, Damage {},  Armor {}".format(
            self.hit_points, self.damage, self.armor
        )
        return rep

    def reset(self):
        self.hit_points = self.init_hit_points
        self.damage = self.init_damage
        self.armor = self.init_armor


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


def deal(attacker, defender):
    dprint("=======", attacker, defender)
    hits = attacker.damage - defender.armor
    defender.hit_points -= hits
    return defender.hit_points


def do_combat(p1, p2, items):
    tot_cost, p1.damage, p1.armor = 0, 0, 0
    for item in items:
        name, values = item
        cost, damage, armor = values
        tot_cost += cost
        p1.damage += damage
        p1.armor += armor
    dprint("Player1: {} Cost: {} \n {}".format(p1, tot_cost, items))

    i = 0
    while True:
        if (i % 2) == 0:
            if remaining_hitpoints := deal(p1, p2) <= 0:
                return "player", tot_cost
        else:
            if remaining_hitpoints := deal(p2, p1) <= 0:
                return "boss", tot_cost
        i += 1


Shopitem = collections.namedtuple("Shopitem", "cost damage armor")


def main():
    you = Player(100)
    boss = Player(104, 8, 1)

    dprint(you)
    dprint(boss)

    # Armor = collections.namedtuple('Armor', 'cost damage armor')
    # Rings = collections.namedtuple('Rings', 'cost damage armor')

    with open("day20_input.txt") as fp:
        weapons, armor, rings, boss_data = fp.read().split("\n\n")

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
    rings_dict["Damage +0"] = Shopitem(cost=0, damage=0, armor=0)
    rings_dict["Defense +0"] = Shopitem(cost=0, damage=0, armor=0)
    highest_cost = 0
    for i, v in weapons_dict.items():
        wl = []
        cost, damage, armor = v
        you.damage = damage
        you.armor = armor
        wl.append((i, v))

        for ii, vv in armor_dict.items():
            al = []
            cost, damage, armor = vv
            you.damage += damage
            you.armor += armor
            al.append((ii, vv))

            rings_combinations = [v for v in combinations(rings_dict.items(), 2)]
            for combo in rings_combinations:
                rl = []
                # dprint("=============")
                for vvv in combo:
                    iii, shop_item = vvv
                    cost, damage, armor = shop_item
                    you.damage += damage
                    you.armor += armor
                    rl.append(vvv)
                    # dprint(z[0], z[1])
                items = wl + al + rl
                # dprint(items)
                # dprint(">>>>>>>", you, boss)
                you.reset()
                boss.reset()
                winner, tot_cost = do_combat(you, boss, items)
                if winner == "boss":
                    if tot_cost > highest_cost:
                        highest_cost = tot_cost
                        print("=============")
                        print(
                            "Winner = {} Cost {} {} {}".format(
                                winner, tot_cost, you, boss
                            )
                        )
                        print(items)

    # rings_damage_dict = {
    #     key: value for (key, value) in rings_dict.items() if key.startswith("Damage")
    # }
    # rings_damage_dict["Damage +0"] = Shopitem(cost=0, damage=0, armor=0)
    # rings_defense_dict = {
    #     key: value for (key, value) in rings_dict.items() if key.startswith("Defense")
    # }
    # rings_defense_dict["Defense +0"] = Shopitem(cost=0, damage=0, armor=0)
    #
    # for i, v in rings_damage_dict.items():
    #     dprint(i, v)
    # for i, v in rings_defense_dict.items():
    #     dprint(i, v)

    sys.exit()


if __name__ == "__main__":
    main()
