from collections import defaultdict
import numpy as np
import re


def void(*args):
    pass


# used to control whether to debug print or not
dprint = void
# dprint = print


def validate_ABA(entry):
    # dprint(entry)
    set_ABA = set()
    for i, _ in enumerate(entry):
        # dprint(entry[i : i + 4], entry[i : i + 2], entry[i + 3 : i + 1 : -1])
        if len(entry[i:]) < 3:
            break
        if entry[i] == entry[i + 1]:
            continue

        if entry[i] == entry[i + 2]:
            # dprint("valid ABA")
            set_ABA.add(entry[i : i + 3])

    return set_ABA


def process_input(lines):
    print("========Part2==========")
    p = re.compile(r"(\[\w+\]|\w+)")

    cnt = 0
    SSL_IP = []

    for line in lines:
        supernet_set = set()
        hypernet = []
        hypernet_set = set()
        data = p.findall(line)
        for d in data:
            if d[0] == "[":
                hypernet.append(d)
                hypernet_set.update(validate_ABA(d))
            else:
                supernet_set.update(validate_ABA(d))

        for s in supernet_set:
            bab_match = s[1] + s[0] + s[1]
            if bab_match in hypernet_set:
                SSL_IP.append(line)
                cnt += 1
                dprint(" ========================")
                dprint(bab_match, hypernet_set)
                dprint(supernet_set)
                break

    print("Part 2 Valid TLS {} {}".format(cnt, len(SSL_IP)))
    # print("Message Part 2 is {}".format("".join(msg2)))


def main():
    with open("7.in") as fp:
        lines = [line.strip() for line in fp]
    # print("=========", lines)
    process_input(lines)

    return


if __name__ == "__main__":
    main()
