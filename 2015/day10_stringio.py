#!/usr/bin/python


import sys
import re
from io import StringIO

def looksay(line):
    newline = StringIO()
    cnt = 0
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
        cnt += len(str(reps)+v)
        newline.write(str(reps)+v)
        # newline.append(str(reps)+v)
        
        #print(reps, v)
    
    print("count",cnt)
    return newline.getvalue()
        

def go(lines, count):
    for line in lines:
        xline = line
        print("\n*********", xline)
        
        for i in range(count):
            if (i%5 == 0): 
                print(">>  loopcount = {}  ".format( i ))
            xline = looksay(xline)
            #print("<<", len(xline), xline)
        print('\n',len(xline))

def get(file):
 
    go(lines)

    return


def main():
    # lines = ['1','11', '21', '1211', '111221']
    lines = ['3113322113']
    # go(lines, 40)
    go(lines, 50)
    sys.exit(1)

    return


if __name__ == "__main__":
    main()
