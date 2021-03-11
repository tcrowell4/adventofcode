#!/usr/bin/python


import sys
import re

def looksay(line):
    newline = ""
    i = 0
    while i < len(line):
        v = line[i]
        # print(line, i)
        reps = 0
        for x in line[i:]:
            if x == v:
                reps +=1
            else:
                break
        i += reps
        newline += str(reps)+v
        #print(reps, v)
    
    
    return newline
        
        


def go(lines, count):
    for line in lines:
        xline = line
        print("*********", xline)
        
        for i in range(count):
            #print(">>  loopcount = {}  line = {}".format( i, xline))
            xline = looksay(xline)
            #print("<<", len(xline), xline)
        print(len(xline))
def get(file):
 
    go(lines)

    return


def main():
    # lines = ['1','11', '21', '1211', '111221']
    lines = ['3113322113']
    go(lines, 40)
    go(lines, 50)
    sys.exit(1)

    return


if __name__ == "__main__":
    main()
