import sys

A_UPPERCASE = ord("A")
ALPHABET_SIZE = 26


def _decompose(number):
    """Generate digits from `number` in base alphabet, least significants
    bits first.

    Since A is 1 rather than 0 in base alphabet, we are dealing with
    `number - 1` at each iteration to be able to extract the proper digits.
    """

    while number:
        number, remainder = divmod(number - 1, ALPHABET_SIZE)
        yield remainder


def base_10_to_alphabet(number):
    """Convert a decimal number to its base alphabet representation"""

    return "".join(chr(A_UPPERCASE + part) for part in _decompose(number))[::-1]


def base_alphabet_to_10(letters):
    """Convert an alphabet number to its decimal representation"""

    return sum(
        (ord(letter) - A_UPPERCASE + 1) * ALPHABET_SIZE ** i
        for i, letter in enumerate(reversed(letters.upper()))
    )


def validate(pw):
    low_pw = pw.lower()
    # print(low_pw)
    for i, x in enumerate(low_pw):
        if x in ("i", "o", "l"):
            # print("failed illegal", low_pw)
            low_pw = low_pw[: i + 1] + "z" * (len(low_pw) - (i + 1))
            return low_pw

    ordv = [ord(x) for x in low_pw]

    z = 0
    cnt = 0
    for v in ordv:
        # print(v, z)
        if v - z == 1:
            cnt += 1
            z = v
            if cnt == 2:
                # print("break")
                break
            continue
        cnt = 0
        z = v
    if cnt != 2:
        # print("failed consecutive", cnt, low_pw, ordv)
        return low_pw

    repeats = []
    z = ""
    for x in low_pw:
        # if len(low_pw) - i <= 2:
        #     print("failed repeats", repeats, low_pw)
        #     return False
        if x == z and (x not in repeats):
            repeats.append(x)
        else:
            z = x
    if len(repeats) < 2:
        # print("failed repeats", repeats, low_pw)
        return low_pw

    return True


pw = "ghizzzzz"
pw = "ghijklmn"
pw = "vzbxkghb"

# print(validate(pw))
# print(validate("hijklmmn"))
# print(validate("abbceffg"))
# print(validate("abbcegjk"))
# print(validate("abcdffaa"))
# print(validate("ghjaabcc"))
# sys.exit()

for i in range(8 ** 26):
    num = base_alphabet_to_10(pw.upper())
    num += 1
    pw = base_10_to_alphabet(num)
    save_pw = pw
    if (pw := validate(pw)) == True:
        print("next valid pw", save_pw.lower())
        break

    # print(num, pw.lower())

pw = save_pw.lower()
for i in range(8 ** 26):
    num = base_alphabet_to_10(pw.upper())
    num += 1
    pw = base_10_to_alphabet(num)
    save_pw = pw
    if (pw := validate(pw)) == True:
        print("next valid pw", save_pw.lower())
        break
