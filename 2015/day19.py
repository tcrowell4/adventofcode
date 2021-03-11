# from 2020 day 11


def pause():
    programPause = input("Press the <ENTER> key to continue...")


def replacements(rules, starting):

    new = []
    molecules = set()
    replace_options = []
    reverse_rules_dict = {}
    for r in rules:
        print(r)
        target, _, replace = r
        replace_options.append(replace)
        reverse_rules_dict[replace] = target
        s = starting
        for i, x in enumerate(s):
            # print(
            #     s,
            #     i,
            #     x,
            #     target,
            #     len(target),
            #     "=",
            #     s[i : i + len(target)],
            #     "*",
            #     replace,
            #     "*",
            #     s[i + 1 :],
            # )
            if target == s[i : i + len(target)]:
                m = s[:i] + replace + s[i + len(target) :]
                molecules.add(m)
                # print(m[i - 3 : i + 6])
        # pause()

    for k, v in reverse_rules_dict.items():
        print(k, v)

    return molecules


def main():
    with open("day19_input.txt") as fp:
        chunks = fp.read().split("\n\n")

    lines = [x.strip().split() for x in chunks[0].split("\n")]

    s = replacements(lines, chunks[1].strip())

    print(len(s))
    # for x in s:
    #     print(x)


if __name__ == "__main__":
    main()
