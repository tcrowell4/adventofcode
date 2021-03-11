#!/usr/bin/python

# day19_part1.py
"""

"""

import sys
import pprint
import re
import numpy as np


def play_cards(p1, p2):
    num_cards = len(p1) + len(p2)
    print("Number of cards : {}".format(num_cards))
    # if both players have cards then continue playing
    while len(p1) and len(p2):
        # draw card
        p1card = p1.pop(0)
        p2card = p2.pop(0)

        if p1card > p2card:
            p1.append(p1card)
            p1.append(p2card)
        else:
            p2.append(p2card)
            p2.append(p1card)

    print("player1 {}".format(p1))
    print("player2 {}".format(p2))
    if len(p1):
        winner = p1
    else:
        winner = p2

    score_values = [x for x in range(num_cards, 0, -1)]
    score = 0
    for i, _ in enumerate(winner):
        print(i, winner[i], score_values[i])
        score += winner[i] * score_values[i]

    print("Final Score {}".format(score))


def main():
    with open("day22_input.txt", "r") as f:
        player1, player2 = [row.split("\n") for row in f.read().strip().split("\n\n")]

    print("player1", player1)
    print("player2", player2)
    # sum = process_input(tiles)
    p1cards = [int(card) for card in player1[1:]]
    p2cards = [int(card) for card in player2[1:]]
    print(p1cards)
    print(p2cards)
    play_cards(p1cards, p2cards)
    sys.exit(1)


if __name__ == "__main__":
    main()
