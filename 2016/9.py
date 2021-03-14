import re

"""
--- Day 9: Explosives in Cyberspace ---
The format compresses a sequence of characters. Whitespace is ignored. To indicate that some sequence should be repeated, a marker is added to the file, like (10x2). To decompress this marker, take the subsequent 10 characters and repeat them 2 times. Then, continue reading the file after the repeated data. The marker itself is not included in the decompressed output.

If parentheses or other characters appear within the data referenced by a marker, that's okay - treat it like normal data, not a marker, and then resume looking for markers after the decompressed section.

For example:

ADVENT contains no markers and decompresses to itself with no changes, resulting in a decompressed length of 6.
A(1x5)BC repeats only the B a total of 5 times, becoming ABBBBBC for a decompressed length of 7.
(3x3)XYZ becomes XYZXYZXYZ for a decompressed length of 9.
A(2x2)BCD(2x2)EFG doubles the BC and EF, becoming ABCBCDEFEFG for a decompressed length of 11.
(6x1)(1x3)A simply becomes (1x3)A - the (1x3) looks like a marker, but because it's within a data section of another marker, it is not treated any differently from the A that comes after it. It has a decompressed length of 6.
X(8x2)(3x3)ABCY becomes X(3x3)ABC(3x3)ABCY (for a decompressed length of 18), because the decompressed data from the (8x2) marker (the (3x3)ABC) is skipped and not processed further.

"""


def void(*args):
    pass


# used to control whether to debug print or not
dprint = void
# dprint = print


def process_marker(line_portion):
    # extract marker
    current_idx = 0
    marker = ""
    for ch in line_portion[current_idx:]:
        marker += line_portion[current_idx]
        current_idx += 1
        if ch == ")":
            break
    marker_inst = marker[1:-1]
    num_subsequent_chars, repeat = marker_inst.split("x")
    num_subsequent_chars = int(num_subsequent_chars)
    repeat = int(repeat)
    dprint(marker_inst, num_subsequent_chars, repeat)
    dprint(">>>", current_idx, line_portion[current_idx:])
    temp = line_portion[current_idx : current_idx + num_subsequent_chars]
    count = num_subsequent_chars * repeat
    return count, num_subsequent_chars + current_idx


def process_input(lines, part):
    print("======== Part 1 ==========")
    total_length = 0
    for line in lines:
        decompress = []
        current_idx = 0
        line_len = len(line)
        while True:
            dprint("while {} {} {}".format(current_idx, line_len, line[current_idx:]))
            if current_idx >= line_len:
                break
            if line[current_idx] == "(":
                count, ch_len = process_marker(line[current_idx:])
                total_length += count
                current_idx += ch_len
                dprint("<<<", current_idx, ch_len)
                dprint("<<<", line[current_idx:10] + ".....")
            else:
                current_idx += 1
                total_length += 1
        # decom_msg = "".join(decompress)
        # print("decompressed message = {}".format(decom_msg))
        dprint("======================")
        # total_length += len(decom_msg)

    print("total_length {}".format(total_length))


def main():

    with open("9.in") as fp:
        lines = [line.strip() for line in fp]
    # print("=========", lines)
    process_input(lines, "part 1")
    # process_input(lines, part2, "part 2")

    return


if __name__ == "__main__":
    main()
