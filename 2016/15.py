import re


def check_same(slots):
    v = slots[0]
    for s in slots:
        if s != v:
            return False
    return True


def process_input(lines):
    discs = []
    for line in lines:
        print(line)
        match = re.search(r"has (\d+).* position (\d+)", line)
        discs.append((int(match[1]), int(match[2])))
    discs.append((11, 0))  # part 2

    # discs = [(4, 5), (1, 2)]
    print(discs)
    time = 0
    while True:
        # if time == 1000000:
        #     break
        slots = []
        positions, start_position = discs[0]
        seed = (start_position + time) % positions
        for i, disc in enumerate(discs):
            positions, start_position = disc
            x = (start_position + time + i) % positions
            if x != seed:
                break
        else:
            print(f"Fall through at time = {time-1}  {slots}")
            return
        # print(slots)
        # if check_same(slots):
        #     print(f"Fall through at time = {time-1}  {slots}")
        #     return
        time += 1


def main():

    with open("16.in") as fp:
        lines = [line.strip() for line in fp]
    # print("=========", lines)
    process_input(lines)

    return


if __name__ == "__main__":
    main()
