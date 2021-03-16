import re
import sys

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


def pause():
    programPause = input("Press the <ENTER> key to continue...")


def void(*args, **kwargs):
    pass


# used to control whether to debug print or not
dprint = void
# dprint = print


def entryExit(func):
    def wrapper(*args, **kwargs):
        dprint("Before function call")
        result = func(*args, **kwargs)
        dprint("After function call")
        return result

    return wrapper


def extract_marker(line, depth=0):
    # extract the leading marker and return its attributes
    close_paren = line.find(")")
    marker = line[: close_paren + 1]
    marker_inst = marker[1:-1]
    dprint("{} >>> marker {}".format(depth * " ", marker))
    num_subsequent_chars, repeat = marker_inst.split("x")
    num_subsequent_chars = int(num_subsequent_chars)
    repeat = int(repeat)

    return repeat, num_subsequent_chars, marker


@entryExit
def process_marker(line_portion, count, depth=0):
    marker_idx = 0

    dprint(depth * " ", ">>>in", line_portion[:20], end="...")
    dprint(line_portion[-10:])

    line_len = len(line_portion)
    last_char = ")"
    marker_num_characters = 0  # designed to trigger to save the initial size
    while True:
        # pause()
        num_subsequent_chars, repeat = 0, 0
        ch_count = 0
        if marker_idx >= line_len:
            break
        dprint(
            "{} >>> WHILE count {} marker_idx {} line_len {} ch {}".format(
                depth * " ", count, marker_idx, line_len, line_portion[marker_idx]
            )
        )
        # peak ahead to see if another marker is present
        if line_portion[marker_idx] == "(":
            # extract marker
            repeat, num_subsequent_chars, marker = extract_marker(
                line_portion[marker_idx:], depth
            )
            # save the initial number of characters in the marker
            if marker_num_characters == 0:
                marker_num_characters = num_subsequent_chars + len(marker)

            marker_idx += len(marker)

            if marker_idx >= line_len:
                break

            dprint(f"{depth * ' '} >>>> mid {marker_idx} {num_subsequent_chars}")
            # dprint(
            #     f"{depth * ' '} >>>> mid {line_portion[marker_idx : marker_idx + num_subsequent_chars]}"
            # )
            dprint(depth * " ", ">>> mid ", marker, num_subsequent_chars, repeat)

            # if the next character was an another marker then this needs
            # to be recursed
            if line_portion[marker_idx] == "(":
                dprint(f"{depth * ' '} >>>> recurse ")

                ch_cnt, processed_length = process_marker(
                    line_portion[marker_idx : marker_idx + num_subsequent_chars],
                    # line_portion[marker_idx:],
                    # count,
                    0,
                    depth + 4,
                )
                ch_count += ch_cnt * repeat
                dprint(f"{depth * ' '} <<<< recurse  {ch_cnt} {processed_length} ")
                marker_idx += num_subsequent_chars
            else:
                dprint(
                    f"{depth * ' '} >>>> else: normal character {line_portion[marker_idx]} "
                )
                ch_count = num_subsequent_chars * repeat
                marker_idx += num_subsequent_chars
                dprint(f"{depth * ' '} >>>> else: new marker_idx: {marker_idx} ")
        else:
            dprint(f"{depth * ' '} **** normal character {line_portion[marker_idx]} ")
            dprint(f"{depth * ' '} >>>> new marker_idx: {marker_idx} ")
            ch_count += 1
            marker_idx += 1

        count += ch_count

    ch_count = num_subsequent_chars * repeat
    count += ch_count
    dprint(f"{depth * ' '} >>>return {count} {marker_num_characters} ")
    return count, marker_num_characters

    # dprint(
    #     "{} >>>return {} idx {} final {} {}  {}".format(
    #         depth * " ",
    #         marker,
    #         marker_idx,
    #         ch_count,
    #         repeat * count,
    #         num_subsequent_chars + len(marker),
    #     )


@entryExit
def process_input(lines, part):
    print("======== Part 1 ==========")
    for line in lines:
        total_length = 0
        decompress = []
        current_idx = 0
        line_len = len(line)
        count, num_subs = process_marker(line[current_idx:], 0)
        total_length += count
        current_idx += num_subs
        dprint("<<<returned", count, current_idx, num_subs)
        dprint("<<<", line[current_idx : current_idx + 20] + ".....")

        # decom_msg = "".join(decompress)
        # print("decompressed message = {}".format(decom_msg))
        # total_length += len(decom_msg)
        print("total_length {}".format(total_length))
        dprint("======================")


def main():

    with open("9.in") as fp:
        lines = [line.strip() for line in fp]
    # print("=========", lines)
    process_input(lines, "part 1")
    # process_input(lines, part2, "part 2")

    return


if __name__ == "__main__":
    main()
