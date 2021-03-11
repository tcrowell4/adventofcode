import math


def process_bus_schedule(bus):
    shortest_wait = 9999
    shortest_bus_id = 0
    start = int(bus[0])
    print("Earliest start time {}".format(start))
    ids = bus[1].split(",")
    for id in ids:
        if id == "x":
            continue

        wait_time = (math.ceil(start / int(id)) * int(id)) - start
        print("Bus id {} Wait time {}".format(id, wait_time))
        if wait_time < shortest_wait:
            shortest_wait = wait_time
            shortest_bus_id = int(id)

    print("Shortest Wait time {} Bus ID: {}".format(shortest_wait, shortest_bus_id))
    print("Bus ID * wait_time = {}".format(shortest_bus_id * shortest_wait))


def main():
    with open("day13_input.txt") as fp:
        lines = fp.readlines()
    # strip each line and break into individual characters
    bus_list = list(map(lambda x: x.strip(), lines))
    # print(nav_list)
    process_bus_schedule(bus_list)

    return


if __name__ == "__main__":
    main()
