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


def main():
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
