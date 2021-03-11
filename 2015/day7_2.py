#!/usr/bin/python


import sys
import re
import numpy as np


def parse(line):
    x = line.strip()
    m = re.match("(.+) -> (\w+)",x)
    print(m[2],m[1])
    
        
    return m[2],m[1].split()
    

def go(k, dict, depth):
    d = depth+2
    v = dict.get(k)
    print("."*depth, k, v)
    
    if v == None:
        print(">"*depth,k,v)
        return int(k)
    elif type(v) == int:
        return v
    elif 'NOT' in v:
        a = go(v[1], dict,d)
        dict[k] = ~a
        return ~a
    elif 'AND' in v:
        a = go(v[0], dict,d)
        b = go(v[2], dict,d)
        dict[k] = a & b
        return a & b
    elif 'OR' in v:
        a = go(v[0], dict,d)
        b = go(v[2], dict,d)
        dict[k] = a | b
        return a | b
    elif 'RSHIFT' in v:
        b = int(v[2])
        a = go(v[0], dict,d)
        dict[k] = a >> b
        return a >> b
        
    elif 'LSHIFT' in v:
        b = int(v[2])
        a = go(v[0], dict,d)
        print("<"*depth,"{}  {} {} << {}".format(k,v,a,b))
        dict[k] = a << b
        return a << b
    else:
        r = go(v[0], dict,d)
        dict[k] = int(r)
        print("#"*depth,"{} {} is {}".format(k,v,r))
        return int(r)
    

def get(file):
    # with open(file) as fp:
        # rule_s = [parse(line) for line in fp ]
    # rd = {x[0]:x[1] for x in rule_s}
    
    with open(file) as fp:
        rd = {k: v for line in fp for (k, v) in [parse(line)]}
        
    rd['b'] = 46065
    
    print(go("a",rd, 0))

    return


def main():
    file = "day7_input.txt"
    get(file)
    sys.exit(1)

    return


if __name__ == "__main__":
    main()
