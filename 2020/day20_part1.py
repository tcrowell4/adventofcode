#!/usr/bin/python

# day19_part1.py
"""

"""

import sys
import pprint
import re
import numpy as np


def process_rules(rules, key, processed_rules, depth):
    z = True
    s = ""
    depth += 1
    if depth > 15:
        return s
    while z:
        values = rules.get(key)
        # print("==============")
        # print("k:values {}:{}".format(key, values))
        # s = s + " "
        if values:
            for v in values:
                # print("key:{} v:{}".format(key, v))
                if v.isdigit():
                    # print("process next rule {}".format(v))
                    x = process_rules(rules, v, processed_rules, depth)
                    s = s + x
                    print("process      rule {} x:{} ".format(v, x))
                    processed_rules[v] = x
                    # print("process      rule {} x:{} s:{}".format(v, x, s))
                    z = False  # continue
                elif v == "|":
                    s = s + v
                    continue
                else:
                    # print("found v {}".format(v))
                    z = False
                    s = s + v[1]
        if len(s) > 1:
            s = "({})".format(s)
    return s


def match_edge(edges: dict, id):
    edge_match = []
    print("Current Id: {}".format(id))
    for i, edge in enumerate(edges[id]):
        # print("Edge: {}: {} ".format(i, edge))
        for k, v in edges.items():
            if k == id:
                continue
            # only match the original edges looking for neighbors
            for ie, edg in enumerate(v[:5]):
                if edg == edge:
                    print(".....Edge {} found Id:{} {} {}".format(i, k, ie, edg))
                    if k not in edge_match:
                        edge_match.append(k)
    return edge_match


def parse_tile(raw_tile):
    # north edge is row 0
    tile_id = raw_tile[0]
    tile_edges = []
    tile_array = np.array([[g for g in data] for data in raw_tile[1:]])
    "north"
    tile_edges.append("".join(tile_array[0]))
    "east"
    tile_edges.append("".join(tile_array[:, -1]))
    "south"
    tile_edges.append("".join(tile_array[-1]))
    "west"
    tile_edges.append("".join(tile_array[:, 0]))
    # Reversed edges
    "north"
    tile_edges.append("".join(tile_array[0])[::-1])
    "east"
    tile_edges.append("".join(tile_array[:, -1])[::-1])
    "south"
    tile_edges.append("".join(tile_array[-1])[::-1])
    "west"
    tile_edges.append("".join(tile_array[:, 0])[::-1])

    return tile_id, tile_edges


def process_input(tiles: list):
    corners = []
    sum = 0
    tile_dict = {}

    for raw_tile in tiles:
        # print(tile)
        # rules[key] = [list(map(int, r.split('-'))) for r in ranges.split('or')]
        id, edges = parse_tile(raw_tile)
        tile_dict[id] = edges

        # arr = np.array(raw_tile[1:])
        # print(arr)
        # for line in arr:
        #     print(line)

    for k, v in tile_dict.items():
        print("===========================")
        print("Tile id: {}".format(k))
        print("Edge Strings:\n {}".format(v))
        edges = match_edge(tile_dict, k)
        # collect the corners that are found
        if len(edges) == 2:
            corners.append(int(k.split()[1][:-1]))

    print("Corners {}".format(corners))
    print(np.prod(corners, dtype=np.uint64))
    return corners


def main():
    with open("day20_input.txt", "r") as f:
        tiles = [row.split("\n") for row in f.read().strip().split("\n\n")]

    # print(tiles)
    sum = process_input(tiles)

    sys.exit(1)


if __name__ == "__main__":
    main()
