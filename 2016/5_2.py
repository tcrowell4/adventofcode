import hashlib


def main():
    doorid = "uqwqemis"
    # doorid = "abc"

    password = 8 * "_"
    i = 0
    while True:
        str2hash = doorid + str(i)
        result = hashlib.md5(str2hash.encode())
        hexhash = result.hexdigest()
        # print(hexhash)
        if hexhash.startswith("00000") and (hexhash[5] in "01234567"):
            print(hexhash)
            ch = hexhash[6]
            pos = int(hexhash[5])
            if password[pos] == "_":
                password = password[:pos] + ch + password[pos + 1 :]
            # password[int(hexhash[5])] = hexhash[6]
            print(
                "password is {} {} hash {}".format("".join(password), str2hash, hexhash)
            )
        if "_" not in password:
            break
        i += 1
    print("final password is {}".format("".join(password)))

    return


if __name__ == "__main__":
    main()
