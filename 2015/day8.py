#!/usr/bin/python


import sys
import re
import numpy as np
import codecs




def go(lines):
    code_cnt = 0
    str_cnt = 0
    for line in lines:
        s = codecs.decode(line, 'unicode_escape')
        code_cnt += len(line)
        str_cnt += len(s)-2
        print(line)
        print(len(line), len(s)-2)
    print(code_cnt, str_cnt,code_cnt - str_cnt)
        
        
        
    

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
    file = "day8_sample.txt"
    get(file)
    sys.exit(1)

    return


if __name__ == "__main__":
    main()
