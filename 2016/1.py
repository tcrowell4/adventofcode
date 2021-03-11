# from 2020 day 11
import re
import sys
import collections
from itertools import permutations
from itertools import combinations
from itertools import product

Vector = collections.namedtuple("Vector", "x y")
Coord = collections.namedtuple("Coord", "xy_index direction")


def void(*args):
    pass


# used to control whether to debug print or not
# dprint = print
dprint = void


class Grid:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.starting = Vector(x, y)
        self.heading = 0
        self.change_amt = 90
        self.path = []
        self.bunny_hq_found = False

        # key is the facing direction,
        # the tuple(index in the vector, determines direction)
        # Vector(x,y)
        # current Vector(4,4) moving 180 for a distance of 5
        # coord[180] = (1,-1)  change the y position in the Coord in the
        # negative direction 5 places
        # Vector[1]= 4    4  +  (5 (distance_to_move) * -1 (direction)
        #  4 +(5 * -1) = -1
        # resulting in Vector(4,-1)
        self.coords = {
            0: Coord(1, 1),
            90: Coord(0, 1),
            180: Coord(1, -1),
            270: Coord(0, -1),
        }

    def __repr__(self):
        rep = "Current Location {}:{}".format(self.x, self.y)
        return rep

    def print_coords(self):
        for i, v in self.coords.items():
            print("facing {} {} ".format(i, v))

    def get_vector(self):
        return Vector(self.x, self.y)

    def change_heading(self, degrees):
        new_heading = self.heading + degrees
        if new_heading < 0:
            new_heading = 360 + new_heading
        elif new_heading >= 360:
            new_heading = new_heading - 360

        self.heading = new_heading

    def generate_path(self, here, there):
        if here.x == there.x:
            if here.y < there.y:
                gpath = [Vector(here.x, i) for i in range(here.y + 1, there.y + 1)]
            else:
                gpath = [Vector(here.x, i) for i in range(here.y - 1, there.y - 1, 1)]
        else:
            if here.x < there.x:
                gpath = [Vector(i, here.y) for i in range(here.x + 1, there.x + 1)]
            else:
                gpath = [Vector(i, here.y) for i in range(here.x - 1, there.x - 1, -1)]
        dprint(here, there, "\n", gpath)
        return gpath

    def execute_move(self, instr):

        action = instr[0]
        amount = int(instr[1:])

        # dprint(
        #     "Before: Action: {} Amount: {}, Direction: {} Location: {}:{}".format(
        #         self.action, self.amount, self.heading, self.x, self.y
        #     )
        # )

        if action == "L":
            self.change_heading(self.change_amt * -1)
        elif action == "R":
            self.change_heading(self.change_amt)

        current_vector = Vector(self.x, self.y)
        # self.coord = self.coords.get()
        if self.heading == 90:
            self.x += amount
        elif self.heading == 270:
            self.x += amount * -1
        elif self.heading == 0:
            self.y += amount
        elif self.heading == 180:
            self.y += amount * -1

        # dprint(
        #     "After: Action: {} Amount: {}, Direction: {} Location: {}:{}".format(
        #         self.action, self.amount, self.heading, self.x, self.y
        #     )
        # )
        new_vector = Vector(self.x, self.y)
        xpath = self.generate_path(current_vector, new_vector)
        if not self.bunny_hq_found:
            for v in xpath:
                if v in self.path:
                    print("Bunny HQ is located at {}".format(v))
                    man_dist = abs(self.starting.x - v.x) + abs(self.starting.y - v.y)
                    print("Manhattan Distance = {}".format(man_dist))
                    self.bunny_hq_found = True

        self.path.extend(xpath)

        return new_vector


def pause():
    programPause = input("Press the <ENTER> key to continue...")


def process_directions(nav):

    # facing = 90  # facing East to begin with (90 degrees)
    # x = 0  # East-West location
    # y = 0  # North-South location
    grid = Grid()
    # grid.print_coords()
    starting = grid.get_vector()
    dprint("starting", starting)
    visited = set()

    for instruction in nav:
        dprint(instruction)
        current = grid.execute_move(instruction)
        dprint("current {} \n Path {}".format(current, grid.path))

    # the man
    dprint(starting, current)
    man_dist = abs(starting.x - current.x) + abs(starting.y - current.y)
    print("Manhattan Distance = {}".format(man_dist))
    print(grid)
    pause()


def main():
    with open("1_input.txt") as fp:
        lines = fp.readlines()
    # strip each line and break into individual characters
    for line in lines:
        nav_list = [x.strip() for x in line.split(",")]
        # print(nav_list)
        process_directions(nav_list)

    return


if __name__ == "__main__":
    main()
