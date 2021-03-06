#!/usr/bin/python


import sys
import re
import numpy as np


def rules(rule, arr):
    
    
    print(rule)
    # print(arr)
    # print_array_properties(arr)
    cmd, row_from, col_from, row_to, col_to = rule
    if cmd == "turn on":
        # print(cmd, "\n",arr[row_from:row_to, col_from:col_to])
        arr[row_from:row_to+1, col_from:col_to+1] += 1
        # print(arr[row_from:row_to, col_from:col_to])
    elif cmd == "turn off":
        # print(cmd, "\n",arr[row_from:row_to, col_from:col_to])
        subarr = arr[row_from:row_to+1, col_from:col_to+1]
        # print("subarr\n",subarr)
        # print_array_properties(subarr)
        for idx, x in np.ndenumerate(subarr):
            #print(idx, x)
            if x > 0:
                subarr[idx[0],idx[1]] -= 1
        # arr[row_from:row_to+1, col_from:col_to+1] -= 1
        # print(cmd, "\n",arr[row_from:row_to, col_from:col_to])
    elif cmd == "toggle":
        # print("TOGGLE:\n", arr[row_from:row_to, col_from:col_to])
        arr[row_from:row_to+1, col_from:col_to+1] +=2
        # print("Toggled:\n",arr[row_from:row_to, col_from:col_to])
    # print("Count non-zeros",np.count_nonzero(arr))
    # print(np.sum(arr))
    # print("=====================")
    return
   

def parse(line):
    # print("===", line)
    x = line.strip()
    if x.startswith("turn"):
        m = re.search(r'^(\w+ \w+) (\d+),(\d+) through (\d+),(\d+)',x)
        rule = [m.group(1),int(m.group(2)),int(m.group(3)),int(m.group(4)),int(m.group(5))]
    else:
        m = re.search(r'^(\w+) (\d+),(\d+) through (\d+),(\d+)',x)
        rule = [m.group(1),int(m.group(2)),int(m.group(3)),int(m.group(4)),int(m.group(5))]
        
    return rule
    
def print_array_properties(arr):
    print("shape:", arr.shape)
    print("dim:", arr.ndim)
    print("size:", arr.size)
    
def go(l):
    light_grid = np.full((1000,1000), 0)
    print_array_properties(light_grid)
    
    for word in l:
        # print(word)
        rules(word, light_grid)
        
    # print(light_grid)
    print("Count non-zeros",np.count_nonzero(light_grid))
    print("Sum:", np.sum(light_grid))
    

def get(file):
    with open(file) as fp:
        lines = [parse(line) for line in fp]
    
    go(lines)

    return


def main():
    file = "day6_input.txt"
    get(file)
    sys.exit(1)

    return


if __name__ == "__main__":
    main()
