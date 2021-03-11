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
    x = 0  # East-West location
    y = 0  # North-South location

    for instruction in nav:
        visits = 0
        homes = defaultdict(int)
        homes[(0,0)]
        # print("=====  instructions {}".format(instruction))
        for direction in instruction:
            print(direction)
            x, y = execute_move(direction, x, y)
            homes[(x,y)] += 1
            visits += 1
        print("{} visits ".format(visits))
        print("number of unique homes {}".format(len(homes)))

    # man_dist = abs(x) + abs(y)
    # print("Manhattan Distance = {}".format(man_dist))


def main():
    with open("day3_input.txt") as fp:
        lines = fp.readlines()
    # strip each line and break into individual characters
    nav_list = list(map(lambda x: x.strip(), lines))
    print("=========",nav_list)
    process_directions(nav_list)

    return


if __name__ == "__main__":
    main()
