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
        reverse_rules_dict[replace[::-1]] = target[::-1]
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

    return molecules, reverse_rules_dict


def reverse_molecule(reverse_rules_dict, starting):
    s = starting[::-1]
    count = 0
    while len(s) > 1:
        for i, x in enumerate(s):
            for target, replace in reverse_rules_dict.items():
                if target == s[i : i + len(target)]:
                    count += 1
                    # print(
                    #     s,
                    #     "\n",
                    #     i,
                    #     x,
                    #     target,
                    #     len(target),
                    #     "=",
                    #     s[i : i + len(target)],
                    #     "*",
                    #     replace,
                    #     "*"
                    #     # s[i + 1 :],
                    # )
                    m = s[:i] + replace + s[i + len(target) :]
                    print("reverse: ==============")
                    print(m[i - 3 : i + 6])
                    print(m)
                    s = m
                    break
    print("Number of changes: {}".format(count))


def main():
    with open("day19_input.txt") as fp:
        chunks = fp.read().split("\n\n")

    lines = [x.strip().split() for x in chunks[0].split("\n")]

    s, reverse_rules_dict = replacements(lines, chunks[1].strip())

    print(len(s))

    reverse_molecule(reverse_rules_dict, chunks[1].strip())
    # for x in s:
    #     print(x)


if __name__ == "__main__":
    main()
