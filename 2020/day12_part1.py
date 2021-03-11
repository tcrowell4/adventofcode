def valid_row(row, rows):
    return 0 <= row < rows


def change_heading(current, degrees):
    new_heading = current + degrees
    if new_heading < 0:
        new_heading = 360 + new_heading
    elif new_heading >= 360:
        new_heading = new_heading - 360

    return new_heading


def execute_move(instr, face_dir, x, y):

    heading = face_dir

    action = instr[0]
    amount = int(instr[1:])

    print(
        "Action: {} Amount: {}, Direction: {} Location: {}:{}".format(
            action, amount, face_dir, x, y
        )
    )

    if (action == "E") or (action == "F" and face_dir == 90):
        x += amount
    elif (action == "W") or (action == "F" and face_dir == 270):
        x -= amount
    elif (action == "N") or (action == "F" and face_dir == 0):
        y += amount
    elif (action == "S") or (action == "F" and face_dir == 180):
        y -= amount
    elif action == "L":
        heading = change_heading(face_dir, amount * -1)
    elif action == "R":
        heading = change_heading(face_dir, amount)

    print(
        "After: Action: {} Amount: {}, Direction: {} Location: {}:{}".format(
            action, amount, heading, x, y
        )
    )

    return heading, x, y


def process_directions(nav):
    facing = 90  # facing East to begin with (90 degrees)
    x = 0  # East-West location
    y = 0  # North-South location
    for instruction in nav:
        # print(instruction)
        facing, x, y = execute_move(instruction, facing, x, y)

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
