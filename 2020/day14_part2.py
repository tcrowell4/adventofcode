import math


def bitvariations(n):
    # print("bv n", n)
    bv = []
    for i in range(1 << n):
        s = bin(i)[2:]
        s = "0" * (n - len(s)) + s
        # print("s", s)
        bv.append(s)
        # bv = list(map(int, list(s)))
        # print("".join(bv))
    return bv


def decimalToBinary(n):
    binx = bin(n).replace("0b", "")

    return binx


def decimalToBinary36(n):
    binx = bin(n).replace("0b", "")
    bit36 = "0" * (36 - len(binx)) + binx
    return bit36


def binarystringToDecimal(b):
    return int("0b" + b, 2)


def bitmask(b36, mask):
    bitlist = list(b36)
    for i, b in enumerate(mask):
        if b == "0":
            continue
        elif b == "1":
            bitlist[i] = "1"
        elif b == "X":
            bitlist[i] = "X"
    return "".join(bitlist)


def countx(val):
    x = 0
    for v in val:
        if v == "X":
            x += 1
    return x


def process_mem_variations(memloc, vars):
    newvals = []
    msklist = list(memloc)
    # print("msklist", msklist, "\n", vars)
    foo = [pos for pos, char in enumerate(msklist) if char == "X"]
    # print("foo", foo)
    # foo is list of index to "X" in the floating bitmask
    for var in vars:
        mskl = msklist  # save a copy
        for i, c in enumerate(var):
            mskl[foo[i]] = c
        # print(mskl)
        newvar = "".join(mskl)
        # print(newvar)
        newval = binarystringToDecimal(newvar)
        # print(newval)
        newvals.append(newval)
    return newvals


def process_floating(memloc):
    memlocs = []
    float_cnt = countx(memloc)
    mem_variations = list(bitvariations(float_cnt))
    # print(mem_variations)
    memlocs = process_mem_variations(memloc, mem_variations)

    return memlocs


def process_mem(memloc, val, mask):
    vbin = decimalToBinary36(memloc)
    newbin = bitmask(vbin, mask)
    newval = process_floating(newbin)
    # print("newval", newval)
    return newval


def process_init_program(init):
    mask = ""
    mem_dict = {}
    for x in init:
        z = x.split()
        cmd = z[0]
        value = z[2]
        if cmd == "mask":
            mask = value
            print("cmd {} value {} mask {}".format(cmd, value, mask))
        elif cmd.startswith("mem"):
            memvalue = int(value)
            memlocation = int(cmd[4:-1])
            print(
                "cmd {} mem {} value {} mask {}".format(
                    cmd, memlocation, memvalue, mask
                )
            )
            new_memlocs = process_mem(memlocation, memvalue, mask)
            for mem in new_memlocs:
                mem_dict[mem] = int(memvalue)

    # print(mem_dict)
    ## This loop syntax accesses the whole dict by looping
    ## over the .items() tuple list, accessing one (key, value)
    ## pair on each iteration.
    answer = 0
    for k, v in mem_dict.items():
        answer += v

    print("Answer = {}".format(answer))


def main():
    with open("day14_input.txt") as fp:
        lines = fp.readlines()
    # strip each line and break into individual characters
    init_list = list(map(lambda x: x.strip(), lines))
    # print(nav_list)
    process_init_program(init_list)

    return
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
    eleven = "000000000000000000000000000000001011"
    seventythree = "000000000000000000000000000001001001"

    x = decimalToBinary36(634749644)
    print(x)
    print(type(x))

    x = decimalToBinary36(11)
    print(x)
    print(type(x))
    print(x == eleven)
    newx = bitmask(x, mask)
    print("binToDecimal", binarystringToDecimal(newx))
    x = decimalToBinary36(73)
    print(x)
    print(type(x))
    print(x == seventythree)
    print(x == newx)

    return

    process_bus_schedule(bus_list)

    return


if __name__ == "__main__":
    main()
