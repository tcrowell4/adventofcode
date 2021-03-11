# from 2020 day 11

import numpy as np

def adjacent_lights(row,col,grid):
    rows, cols = grid.shape
    #print(rows, cols, grid.shape)
    on = 0
    adj_dict = {}
    adj_dict['N'] = (-1,0)
    adj_dict['NE'] = (-1,1)
    adj_dict['E'] = (0,1)
    adj_dict['SE'] = (1,1)
    adj_dict['S'] = (1,0)
    adj_dict['SW'] = (1,-1)
    adj_dict['W'] = (0,-1)
    adj_dict['NW'] = (-1,-1)
    for k, v in adj_dict.items():
        grid_row = row+v[0]
        if 0 <= grid_row < rows:
            pass
        else:
            #print("grid_row {} row {}".format(grid_row, rows))
            continue
        grid_col = col+v[1]
        if 0 <= grid_col < cols:
            pass
        else:
            #print("grid_col {} cols {}".format(grid_col, cols))
            continue
        light = grid[grid_row][grid_col]
        #print("{:2} : {:2} {:2} {} {}:{}".format(k,*v, light, grid_row,grid_col))
        if light == "#":
            on += 1

    return on

def process_lights(grid):
    gridx = grid.copy()
    rows, cols = grid.shape
    corners = {(0,0), (0,cols-1), (cols-1,0), (cols-1,cols-1)}
    gridx[0,0] = '#'
    gridx[0,cols-1] = '#'
    gridx[cols-1,0] = '#'
    gridx[cols-1,cols-1] = '#'
    #for x in np.nditer(grid):
    #    print(x, end=' ')
    # print("Before:")
    # print(gridx)
    moves = 0
    occ = 0
    """
    Note how rows and cols have been swapped in the range() function.

    Edit: It has to be that way because an array can be rectangular
    (i.e. rows != cols). a.shape is the size of each dimension in the
    order they are indexed.
    Therefore if shape is (10, 5) when you write: a[x, y]
    """
    for x in range(0, rows):
        for y in range(0, cols):
            if (x,y) in corners:
                occ += 1
                continue
            occupied_cnt = adjacent_lights(x,y,grid)
            if grid[x,y] == "#" and  not (occupied_cnt ==3 or occupied_cnt == 2):
                gridx[x,y] = "."
                # moves += 1

            if grid[x,y] == "." and occupied_cnt == 3:
                gridx[x,y] = "#"

            if gridx[x,y] == "#":
                occ += 1

            # print(occupied_cnt, grid[x,y], x,y)
    # print(gridx)
    # print("After:")
    return gridx, moves, occ
def main():
    with open("day18_input.txt") as fp:
        lines = fp.readlines()
    # strip each line and break into individual characters
    grid = list(map(lambda x: list(x.strip()), lines))
    light_array = np.array(grid)
    #lock corners on Part 2
    rows, cols = light_array.shape
    light_array[0,0] = '#'
    light_array[0,cols-1] = '#'
    light_array[cols-1,0] = '#'
    light_array[cols-1,cols-1] = '#'
    print(light_array.shape)
    moves = 1
    for turns in range(100):
        light_array, moves, occ = process_lights(light_array)
    print(moves, occ)

    print(light_array)

    return
    print(grid)
    grid[3][5] = '#'
    #for line in grid:
    #    print(line)
    light_array = np.array(grid)
    light_array[4][6] = "Y"
    adjacent_lights(4,6,light_array)
    light_array[4][9] = "Z"
    adjacent_lights(3,6,light_array)
    adjacent_lights(3,9,light_array)
    print(light_array)
    print(light_array.shape)
    process_lights(light_array)


if __name__ == "__main__":
    main()
