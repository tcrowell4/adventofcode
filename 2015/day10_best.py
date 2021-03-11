#!/usr/bin/python
# The performance with this one is tremendous as opposed to the others
# The difference is changing the string to a list.  I would have to presume
# that the difference between append and extend is that much better.

import sys
import re
from io import StringIO

def pause():
    programPause = input("Press the <ENTER> key to continue...")

def looksay(data):
    newline = data
    tmp = []
    cur = newline[0]
    cnt = 0
    i = 0
    for i in newline:
        if i != cur:
            tmp.extend([str(cnt), cur])
            cnt = 0
            cur = i
        cnt += 1
    tmp.extend([str(cnt), cur])
    newline = tmp
        
    
    print(len(newline))
    # print(newline)
    #pause()
    return newline
        

def go(lines, count):
    for line in lines:
        xline = [x for x in line]
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
