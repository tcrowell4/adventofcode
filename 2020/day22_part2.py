#!/usr/bin/python

# day19_part1.py
"""

"""

import sys
import pprint
import re
import numpy as np


def determine_winner(p1, p2, s_winner):
    if s_winner == 1:
        winner = p1
    else:
        winner = p2

    score_values = [x for x in range(len(winner), 0, -1)]
    score = 0

    for i, _ in enumerate(winner):
        print(i, winner[i], score_values[i], winner[i] * score_values[i])
        score += winner[i] * score_values[i]
    print(winner)
    print(score_values)
    print("Final Score {}".format(score))

    # score_values = [x for x in range(len(p2), 0, -1)]
    # score = 0
    # for i, _ in enumerate(p2):
    #     print(i, p2[i], p2[i], p2[i] * score_values[i])
    #     score += p2[i] * p2[i]
    # print(p2)
    # print(score_values)
    # print("Final Score {}".format(score))


def check_duplicate_round(zrounds, zp1, zp2, zrd_cnt):
    # print("===  Rounds:", zrd_cnt, zrounds)
    for zrd in zrounds:
        # print("===  Round:", zrd_cnt, zrd, zp1, zp2)
        if (zrd[0] == zp1) and (zrd[1] == zp2):
            print("===  Round Found:", zrd_cnt, zrd)
            print("================: ", zrd[0], "=", zp1, zrd[1], "=", zp2)

            return True
    return False


def play_cards(p1, p2):
    winner = 0
    xrounds = []
    sw = False
    # xxx = (p1[:], p2[:])
    # xrounds.append(xxx)
    # print("+++++ Start xrounds", xrounds)

    num_cards = len(p1) + len(p2)
    print("Number of cards : {}".format(num_cards))
    # if both players have cards then continue playing
    rd_cnt = 0
    # print(">>>>> xrounds ...", rd_cnt, xrounds)
    while len(p1) and len(p2):
        # if sw == True:
        #     "************* Finished ***********"
        #     break
        # print(">>>>> xrounds ###", rd_cnt, xrounds)
        rd_cnt += 1

        # print(">>>>> xrounds", rd_cnt, xrounds)
        if check_duplicate_round(xrounds, p1[:], p2[:], rd_cnt) == True:
            winner = 1
            sw = True
            # break
            return p1, p2, 1, sw

        xrounds.append((p1[:], p2[:]))

        # draw card
        p1card = p1.pop(0)
        p2card = p2.pop(0)
        # print(">>>>> xrounds :::", rd_cnt, xrounds)

        # print(">>>>> append", rd_cnt, p1, p2, xrounds)

        # if both players have least as many remaining num_cards
        # start a Recursive combat game to determine winner
        if (p1card <= len(p1)) and (p2card <= len(p2)):
            newp1 = p1[:p1card]
            newp2 = p2[:p2card]
            print("=========================")
            print("Recursive Game {} ".format(rd_cnt))
            # print("player1 {} {} {}".format(p1card, p1, newp1))
            # print("player2 {} {} {}".format(p2card, p2, newp2))
            newp1, newp2, winner, sw = play_cards(newp1, newp2)
            # if sw == True:
            #     winner = 1
            #     # p1.append(p1card)
            # p1.append(p2card)
            # return p1, p2, 1, sw
            if winner == 1:
                p1.append(p1card)
                p1.append(p2card)
                # print("Player 1 wins: {} {}".format(p1card, p2card))
                # print("=========================")
            else:
                p2.append(p2card)
                p2.append(p1card)
                # print("Player 2 wins: {} {}".format(p1card, p2card))
                # print("=========================")
        else:
            # print("Regular Game {} ".format(rd_cnt))
            # print("player1 {} {}".format(p1card, p1))
            # print("player2 {} {}".format(p2card, p2))

            if p1card > p2card:
                p1.append(p1card)
                p1.append(p2card)
            else:
                p2.append(p2card)
                p2.append(p1card)

    print("player1 {}".format(p1))
    print("player2 {}".format(p2))

    if p1:
        return p1, p2, 1, sw
    else:
        return p1, p2, 2, sw


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
    p1c, p2c, winner, sw = play_cards(p1cards, p2cards)
    determine_winner(p1c, p2c, winner)

    sys.exit(1)


if __name__ == "__main__":
    main()
