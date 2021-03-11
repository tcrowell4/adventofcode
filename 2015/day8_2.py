#!/usr/bin/python


import sys
import re
import numpy as np
import codecs




def go(lines):
    code_cnt = 0
    encode_cnt = 0
    for line in lines:
        #newx = '\"'
        newx =""
        for x in line:
            if x == '"':
                newx = newx + '\\\"'
            elif x == '\\':
                newx = newx + '\\\\'
            else:
                newx = newx+x
                
            print(x, newx)
        #newx = newx+'\"'
        print("===", line, newx)
        code_cnt += len(line)
        encode_cnt += len(newx) + 2
        print(line)
        print(len(line), len(newx)+2)
    print(encode_cnt, code_cnt,encode_cnt -code_cnt)
        
        
        
    

def get(file):
    # with open(file) as fp:
        # rule_s = [parse(line) for line in fp ]
    # rd = {x[0]:x[1] for x in rule_s}
    
    with open(file) as fp:
        lines = [line.strip() for line in fp ]
        
    print(lines)
    
    go(lines)

    return


def main():
    file = "day8_input.txt"
    get(file)
    sys.exit(1)

    return


if __name__ == "__main__":
    main()
