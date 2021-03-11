# from 2020 day 11
import hashlib


def pause():
    programPause = input("Press the <ENTER> key to continue...")


def process_directions(nav):

    # facing = 90  # facing East to begin with (90 degrees)
    # x = 0  # East-West location
    # y = 0  # North-South location
    grid = Grid()
    # grid.print_coords()
    starting = grid.get_vector()
    dprint("starting", starting)
    visited = set()

    for instruction in nav:
        dprint(instruction)
        current = grid.execute_move(instruction)
        dprint("current {} \n Path {}".format(current, grid.path))

    # the man
    dprint(starting, current)
    man_dist = abs(starting.x - current.x) + abs(starting.y - current.y)
    print("Manhattan Distance = {}".format(man_dist))
    print(grid)
    pause()


def main():
    doorid = "uqwqemis"

    password = []
    i = 0
    while True:
        str2hash = doorid + str(i)
        result = hashlib.md5(str2hash.encode())
        hexhash = result.hexdigest()
        if hexhash.startswith("00000"):
            password.append(hexhash[5])
            print(
                "password is {} {} hash {}".format("".join(password), str2hash, hexhash)
            )
        if len(password) == 8:
            break
        i += 1
    print("final password is {}".format("".join(password)))

    return


if __name__ == "__main__":
    main()
