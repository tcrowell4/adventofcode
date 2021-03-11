def valid_row(row, rows):
    return 0 <= row < rows


def rotate_waypoint(instr, wx, wy):
    # to rotate always rotate to the right
    # a left rotate = 360-amount to convert to right

    action = instr[0]
    amount = int(instr[1:])

    if action == "R":
        degrees = amount
    else:
        degrees = 360 - amount

    if degrees == 90:
        wxx = wy
        wyy = wx * -1
    elif degrees == 180:
        wxx = wx * -1
        wyy = wy * -1
    elif degrees == 270:
        wxx = wy * -1
        wyy = wx

    return wxx, wyy


def move_waypoint(instr, wx, wy):

    action = instr[0]
    amount = int(instr[1:])

    print("Action: {} Amount: {}, Waypoint: {}:{}".format(action, amount, wx, wy))

    if action == "E":
        wx += amount
    elif action == "W":
        wx -= amount
    elif action == "N":
        wy += amount
    elif action == "S":
        wy -= amount
    elif (action == "L") or (action == "R"):
        wx, wy = rotate_waypoint(instr, wx, wy)

    print("After Action: {} Amount: {}, Waypoint: {}:{}".format(action, amount, wx, wy))

    return wx, wy


def move_ship(instr, x, y, wx, wy):

    action = instr[0]
    amount = int(instr[1:])

    print(
        "Action: {} Amount: {}, Location: {}:{} Waypoint: {}:{}".format(
            action, amount, x, y, wx, wy
        )
    )

    x = x + (wx * amount)
    y = y + (wy * amount)

    print(
        "After Action: {} Amount: {}, Location: {}:{} Waypoint: {}:{}".format(
            action, amount, x, y, wx, wy
        )
    )

    return x, y


def process_directions(nav):
    x = 0  # East-West location
    y = 0  # North-South location
    wx = 10  # East-West waypoint
    wy = 1  # North-South waypoint
    for instruction in nav:
        print("*********** ", instruction, "***********")
        if instruction[0] == "F":
            x, y = move_ship(instruction, x, y, wx, wy)
        else:
            wx, wy = move_waypoint(instruction, wx, wy)

    man_dist = abs(x) + abs(y)
    print("Manhattan Distance = {}".format(man_dist))


def main():
    with open("day12_input.txt") as fp:
        lines = fp.readlines()
    # strip each line and break into individual characters
    nav_list = list(map(lambda x: x.strip(), lines))
    # print(nav_list)
    process_directions(nav_list)

    return


if __name__ == "__main__":
    main()
