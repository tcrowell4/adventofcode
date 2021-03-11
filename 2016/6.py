from collections import defaultdict
import numpy as np


def void(*args):
    pass


# used to control whether to debug print or not
# dprint = print
dprint = void


def process_input(lines):
    print("========Part1==========")
    msg = []
    msg2 = []
    possible, not_possible = 0, 0
    arr = np.array(lines)
    dprint(arr.shape)
    for x in arr.T.reshape(-1, arr.shape[0]):
        d = defaultdict(int)
        dprint("=================")
        dprint(x)
        for ch in x:
            d[ch] += 1
        for i, v in d.items():
            dprint(i, v)
        max_key = max(d, key=lambda k: d[k])
        max_value = d[max_key]
        dprint("max data", max_key, max_value)
        for i, v in d.items():
            if v == max_value:
                msg.append(i)
                break
        min_key = min(d, key=lambda k: d[k])
        min_value = d[min_key]
        dprint("min data", min_key, min_value)
        for i, v in d.items():
            if v == min_value:
                msg2.append(i)
                break

    print("Message Part 1 is {}".format("".join(msg)))
    print("Message Part 2 is {}".format("".join(msg2)))


def main():
    with open("6.in") as fp:
        lines = [list(line.strip()) for line in fp]
    # print("=========", lines)
    process_input(lines)

    return


if __name__ == "__main__":
    main()
