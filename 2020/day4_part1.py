#!/usr/bin/python


"""
--- Day 4: Passport Processing ---
Part 1
210 valid passports
Part 2
131 valid passports
"""

import sys
import re


# byr (Birth Year) - four digits; at least 1920 and at most 2002
def is_byr_valid(value):

    if value.isdigit() and len(value) == 4:
        byr = int(value)
        if 1920 <= byr <= 2002:
            return True
        else:
            return False
    else:
        return False


# iyr (Issue Year) - four digits; at least 2010 and at most 2020
def is_iyr_valid(value):
    if value.isdigit() and len(value) == 4:
        byr = int(value)
        if 2010 <= byr <= 2020:
            return True
        else:
            return False
    else:
        return False


# eyr (Expiration Year) - four digits; at least 2020 and at most 2030
def is_eyr_valid(value):
    if value.isdigit() and len(value) == 4:
        byr = int(value)
        if 2020 <= byr <= 2030:
            return True
        else:
            return False
    else:
        return False


def is_hgt_valid(value):
    match = re.search(r"(\d*)(\w*)", value)
    hgt = int(match[1])
    m = match[2]
    if m == "cm":
        if 150 <= hgt <= 193:
            return True
        else:
            return False
    elif m == "in":
        if 59 <= hgt <= 76:
            return True
        else:
            return False
    else:
        return False


# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f
def is_hcl_valid(value):
    if value[0] == "#" and len(value) == 7:
        match = re.search(r"[A-Fa-f0-9]+", value[1:])
        if match:
            if len(match[0]) == 6:
                return True
    return False


# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
def is_ecl_valid(value):
    color = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if value in color:
        return True
    else:
        return False


# pid (Passport ID) - a nine-digit number, including leading zeroes.
def is_pid_valid(value):
    if value.isdigit() and len(value) == 9:
        return True
    else:
        return False


def validate_field(key, value):
    print("Key: {} Field Value {}".format(key, value))
    length = len(value)

    if key == "byr":
        return is_byr_valid(value)
    elif key == "iyr":
        return is_iyr_valid(value)
    elif key == "eyr":
        return is_eyr_valid(value)
    elif key == "hgt":
        return is_hgt_valid(value)
    elif key == "hcl":
        return is_hcl_valid(value)
    elif key == "ecl":
        return is_ecl_valid(value)
    elif key == "pid":
        return is_pid_valid(value)
    elif key == "cid":
        return True
    else:
        print("Invalid attribute {}".format(value))
        return False


def build_items(dict, line):
    x = line.split()
    for itm in x:
        key = itm.split(":")[0]
        value = itm.split(":")[1]
        dict[key] = value
    # print("Build leave:", dict)
    return dict


def process_items(dict, valid_pass_items):
    print("process:", dict)
    for key in sorted(valid_pass_items.keys()):
        if key not in dict:
            if key != "cid":
                print("{} not in passport".format(key))
                return False
        else:
            valid = validate_field(key, dict[key])
            print("{} {} Return={}".format(key, dict[key], valid))
            if valid != True:
                return False
    return True


def main():
    valid_passport_count = 0
    passport = {}
    pass_valid = {
        "byr": "Birth Year",
        "iyr": "Issue Year",
        "eyr": "Expiration Year",
        "hgt": "Height",
        "hcl": "Hair Color",
        "ecl": "Eye Color",
        "pid": "Passport ID",
        "cid": "Country ID",
    }
    pass_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

    with open("day4_input.txt") as f:
        lines = f.readlines()
    # print(lines)

    pass_items = []
    for i, xline in enumerate(lines):
        # print(i, xline)
        line = xline.strip()
        if len(line) == 0:
            if process_items(passport, pass_valid) == True:
                valid_passport_count += 1
            passport = {}
        else:
            pass_items = build_items(passport, line)

    if process_items(passport, pass_valid) == True:
        valid_passport_count += 1

    print("{} valid passports".format(valid_passport_count))

    sys.exit(1)


if __name__ == "__main__":
    main()
