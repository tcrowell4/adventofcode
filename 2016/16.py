import re


def checksum(s):
    while True:
        cs = []
        ss = [s[x : x + 2] for x in range(0, len(s), 2)]
        for c in ss:
            if c[0] == c[1]:
                cs.append("1")
            else:
                cs.append("0")

        s = "".join(cs)
        if len(s) % 2 == 1:
            return s


def process_input(s, dl):
    a = s
    # print(a)
    while len(a) <= dl:
        b = a[::-1]
        new_b = []
        for x in b:
            if x == "1":
                new_b.append("0")
            elif x == "0":
                new_b.append("1")
        a = a + "0" + "".join(new_b)
        # print(f"new_a = {a}")

    chk_sum = checksum(a[:dl])
    print(f"chk_sum = {chk_sum}")
    return


def main():

    initial_state = "10111011111001111"
    disk_length = 35651584

    process_input(initial_state, disk_length)

    return


if __name__ == "__main__":
    main()
