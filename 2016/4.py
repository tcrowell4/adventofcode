from collections import defaultdict
import numpy as np
import re


def void(*args):
    pass


# used to control whether to debug print or not
# dprint = print
dprint = void


def get_checksum(encrypted_name):
    d = defaultdict(int)
    for ch in sorted(encrypted_name):
        d[ch] += 1
    del d["-"]
    for i, v in d.items():
        dprint(i, v)
    sd = sorted(d.items(), key=lambda kv: kv[1], reverse=True)
    x = []
    for i in range(5):
        dprint("sd[i]", sd[i])
        x.append(sd[i][0])
    checksum = "".join(x)
    dprint("checksum", checksum)
    return checksum


from string import ascii_lowercase


def caesar_shift(text, places=5):
    def substitute(char):
        if char in ascii_lowercase:
            char_num = ord(char) - 97
            char = chr((char_num + places) % 26 + 97)
        else:
            char = " "
        return char

    text = text.lower().replace(" ", "")
    return "".join(substitute(char) for char in text)


def process_input(lines):
    valid_data = []
    # valid_data.append(("qzmt-zixmtkozy-ivhz", 343))
    sector_total = 0
    p = re.compile(r"(.*)-(\d+)\[(.*)\]")
    print("========Part1==========")
    for line in lines:
        dprint(line)
        m = p.search(line)
        enc_name, sector, checksum = m.group(1), int(m.group(2)), m.group(3)
        dprint(enc_name, sector, checksum)
        calculated_checksum = get_checksum(enc_name)
        if calculated_checksum == checksum:
            sector_total += sector
            valid_data.append((enc_name, sector))
    print("Sector Total = {}".format(sector_total))
    for x in valid_data:
        ename, sec = x
        dprint("enc_name {} sector {}".format(ename, sec))
        name = caesar_shift(ename, sec)
        dprint("name", name)
        if name.startswith("north"):
            print("{} found in sector {}".format(name, sec))
            return


def main():
    with open("4.in") as fp:
        lines = [line.strip() for line in fp]
    # print("=========", lines)
    process_input(lines)

    return


if __name__ == "__main__":
    main()
