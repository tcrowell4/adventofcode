from collections import defaultdict


def execute_move(instr, x, y):

    action = instr
    amount = 1

    print(
        "Action: {} Location: {}:{}".format(
            action,  x, y
        )
    )

    if action == ">":
        x += amount
    elif action == "<":
        x -= amount
    elif action == "^":
        y += amount
    elif action == "v":
        y -= amount

    print(
        "After: Action: {}  Location: {}:{}".format(
            action,  x, y
        )
    )

    return x, y


def process_directions(nav):


    for instruction in nav:
        x = 0  # East-West location
        y = 0  # North-South location

        robo_x = 0
        robo_y = 0

        santa_homes = set()
        santa_homes.add((0,0))
        robo_homes = set()
        robo_homes.add((0,0))
        print("=====  instructions {}".format(instruction))
        for i, direction in enumerate(instruction):
            if i % 2 == 0:
                print(direction)
                x, y = execute_move(direction, x, y)
                santa_homes.add((x,y))
            else:
                robo_x, robo_y = execute_move(direction, robo_x, robo_y)
                robo_homes.add((robo_x,robo_y))

        print("number of unique santa_homes {}".format(len(santa_homes)))
        print("number of unique robo_homes {}".format(len(robo_homes)))

        uniq = santa_homes.union(robo_homes)
        print("unique", len(uniq))

    # man_dist = abs(x) + abs(y)
    # print("Manhattan Distance = {}".format(man_dist))


def main():
    with open("day3_input.txt") as fp:
        lines = fp.readlines()
    # strip each line and break into individual characters
    nav_list = list(map(lambda x: x.strip(), lines))
    # print("=========",nav_list)
    process_directions(nav_list)

    return


if __name__ == "__main__":
    main()
