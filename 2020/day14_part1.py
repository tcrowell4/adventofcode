import math


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
            bitlist[i] = "0"
        elif b == "1":
            bitlist[i] = "1"
    return "".join(bitlist)


def process_mem(val, mask):
    vbin = decimalToBinary36(val)
    newbin = bitmask(vbin, mask)
    newval = binarystringToDecimal(newbin)
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
            memlocation = cmd[4:-1]
            print(
                "cmd {} mem {} value {} mask {}".format(
                    cmd, memlocation, memvalue, mask
                )
            )
            new_value = process_mem(memvalue, mask)
            mem_dict[memlocation] = int(new_value)

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
