from collections import defaultdict
import numpy as np
import re


def void(*args):
    pass


# used to control whether to debug print or not
dprint = void
dprint = print


def validate_ABBA(entry):
    # dprint(entry)
    for i, ch in enumerate(entry):
        # dprint(entry[i : i + 4], entry[i : i + 2], entry[i + 3 : i + 1 : -1])
        if len(entry[i:]) < 4:
            return False
        if entry[i] == entry[i + 1]:
            continue

        if entry[i : i + 2] == entry[i + 3 : i + 1 : -1]:
            dprint("valid ABBA", entry)
            return True
    else:
        return False


def process_input(lines):
    print("========Part1==========")
    p = re.compile(r"(\[\w+\]|\w+)")

    cnt = 0
    TLS_IP = []

    for line in lines:
        TLS_valid = False

        data = p.findall(line)
        # dprint(data)
        for d in data:
            if validate_ABBA(d):
                if d[0] == "[":
                    dprint(">>> valid ABBA but inside brackets")
                    TLS_valid = False
                    break
                else:
                    dprint(">>> valid ABBA")
                    TLS_valid = True

        if TLS_valid:
            TLS_IP.append(line)
            cnt += 1

    print("Part 1 Valid TLS {} {}".format(cnt, len(TLS_IP)))
    # print("Message Part 2 is {}".format("".join(msg2)))


def main():
    with open("7.in") as fp:
        lines = [line.strip() for line in fp]
    # print("=========", lines)
    process_input(lines)

    return


if __name__ == "__main__":
    main()
