#!/usr/bin/python


import sys
import re
import numpy as np
from collections import defaultdict
import itertools

def distance_between(t,dict):
    dist = 0
    # print("Calc distance")
    for i in range(0, len(t)-1):
        # print(t[i], t[i+1])
        x = dict.get((t[i],t[i+1]))
        # print(x)
        dist += x
        
        
        
    return(dist)
        
        
        


def go(lines):
    cities = set()
    city_pairs = defaultdict(int)
    for line in lines:
        c1, _, c2, _, distance = line.split()
        distance = int(distance)
        cities.add(c1)
        cities.add(c2)
        city_pairs[(c1,c2)] = distance
        city_pairs[(c2,c1)] = distance
        # print(line)
    # print(cities)
    # for k,v in city_pairs.items():
        # print(k,v)
        


    per = itertools.permutations(cities)
    perm_list = []
    for val in per:
        #print(*val)
        # print(type(val))
        
        dist = distance_between(val, city_pairs)
        perm_list.append([val, dist])
        
    #print(perm_list)
    s_dist = 9999
    s_path = ""
    l_dist = 0
    l_path = ""
    for i in perm_list:
        #print(i)
        if i[1] < s_dist: 
            s_dist = i[1]
            s_path = i[0]
        if i[1] > l_dist: 
            l_dist = i[1]
            l_path = i[0]
        
    
    print("shortest {} {}".format(s_path,s_dist))
    print("Longest  {} {}".format(l_path,l_dist))

def get(file):
    # with open(file) as fp:
        # rule_s = [parse(line) for line in fp ]
    # rd = {x[0]:x[1] for x in rule_s}
    
    with open(file) as fp:
        lines = [line.strip() for line in fp ]
        
    # print(lines)
    
    go(lines)

    return


def main():
    file = "day9_input.txt"
    get(file)
    sys.exit(1)

    return


if __name__ == "__main__":
    main()
