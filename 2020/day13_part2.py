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


def brute_force(bus):

    id_tmp = bus[1].split(",")
    ids = []
    for x in id_tmp:
        print(x)
        if x != "x":
            ids.append(int(x))
        else:
            ids.append(x)

    x = ids[0]
    next_bus_idx = 2
    y = ids[1]
    xx = 0

    # establish starting timestamp

    t = 0
    find_next_bus(t, next_bus_idx, ids)


def find_next_bus(ts, next_bus, ids):
    idx = int(ts / 17)
    for i in range(idx, idx + 1000):
        t = ids[0] * i
        if (t + next_bus) % ids[next_bus] == 0:
            print("index {} id: {} timestamp {}  {}".format(i, t, ids[0], t + next_bus))

            find_next_bus(t, 3, ids)


def main():

    # bus_list = ["0", "7, 13,x,x,59"]
    bus_list = ["0", "17,x,13,19"]

    # with open("day13_input.txt") as fp:
    #     lines = fp.readlines()
    # strip each line and break into individual characters

    # bus_list = list(map(lambda x: x.strip(), lines))
    # print(nav_list)
    brute_force(bus_list)
    return

    process_bus_schedule(bus_list)

    return


if __name__ == "__main__":
    main()
