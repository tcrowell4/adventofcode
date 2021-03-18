import re
import sys
from collections import namedtuple, defaultdict

"""
--- Day 10: Balance Bots ---
"""


def pause():
    programPause = input("Press the <ENTER> key to continue...")


def void(*args, **kwargs):
    pass


# used to control whether to debug print or not
dprint = void
# dprint = print


def entryExit(func):
    def wrapper(*args, **kwargs):
        dprint("Before function call")
        result = func(*args, **kwargs)
        dprint("After function call")
        return result

    return wrapper


Bot = namedtuple("Bot", ["bot", "low_cmd", "low_dest", "high_cmd", "high_dest"])


def balance_bots(bot_rules_dict, bot_inventory_dict, bin_dict):
    while True:
        for i, v in bot_inventory_dict.items():
            if len(v) == 2:
                low = min(v)
                high = max(v)
                cmd = bot_rules_dict[i]
                if high == 61 and low == 17:
                    print(f"bot: {i}  {high} {low} {cmd} {v}")
                dprint(f"{high} {low} {cmd} {v}")
                # process low
                if cmd.low_cmd == "bot":
                    bot_inventory_dict[cmd.low_dest].append(low)
                else:
                    bin_dict[cmd.low_dest].append(low)

                if cmd.high_cmd == "bot":
                    bot_inventory_dict[cmd.high_dest].append(high)
                else:
                    bin_dict[cmd.high_dest].append(high)
                # reset inventory not that it has moved
                bot_inventory_dict[i] = []
                break
            else:
                continue
        else:
            print("bot processing is complete")
            return


# @entryExit
def process_input(lines, part):
    bot_rules_dict = defaultdict(Bot)
    bot_inventory_dict = defaultdict(list)
    bin_dict = defaultdict(list)
    commands = []

    print("======== Part 1 ==========")

    re_comp_val = re.compile(r"value (?P<value>[0-9]*) goes to bot (?P<bot_to>[0-9]*)")
    re_comp_bot = re.compile(
        r"bot (?P<bot_num>[0-9]*) gives low to (?P<dest_low>\w+) (?P<bot_low>[0-9]*) and high to (?P<dest_high>\w+) (?P<bot_high>[0-9]*)"
    )

    for line in lines:
        commands.append(line.strip())
        if line.startswith("value"):
            mval = re_comp_val.search(line)
            if mval is None:
                print("Invalid Value Format")
            else:
                bot_inventory_dict[mval["bot_to"]].append(int(mval["value"]))
        elif line.startswith("bot"):
            mbot = re_comp_bot.search(line)
            pb = Bot(
                mbot["bot_num"],
                mbot["dest_low"],
                mbot["bot_low"],
                mbot["dest_high"],
                mbot["bot_high"],
            )
            # dprint(pb)
            bot_rules_dict[mbot["bot_num"]] = pb

    balance_bots(bot_rules_dict, bot_inventory_dict, bin_dict)

    pause()

    dprint("Bot Inventory")
    for k, v in bot_inventory_dict.items():
        dprint(f"{k:4}:{v}")

    dprint("Bot Rules Dict")
    for k, v in bot_rules_dict.items():
        dprint(f"{k:4}:{v}")

    dprint("Bin Dict")
    for k, v in bin_dict.items():
        dprint(f"{k:4}:{v}")
    print(bin_dict["0"][0], bin_dict["1"][0], bin_dict["2"][0])
    print(int(bin_dict["0"][0]) * int(bin_dict["1"][0]) * int(bin_dict["2"][0]))


def main():

    with open("10.in") as fp:
        lines = [line.strip() for line in fp]
    # print("=========", lines)
    process_input(lines, "part 1")
    # process_input(lines, part2, "part 2")

    return


if __name__ == "__main__":
    main()
