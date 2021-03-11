import numpy as np

def adjacent_seats(row,col,grid):
    rows, cols = grid.shape
    #print(rows, cols, grid.shape)
    taken = 0
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
        seat = grid[grid_row][grid_col]
        #print("{:2} : {:2} {:2} {} {}:{}".format(k,*v, seat, grid_row,grid_col))
        if seat == "#":
            taken += 1

    return taken

def process_arrivals(grid):
    #print("Before:")
    #print(grid)
    gridx = grid.copy()
    rows, cols = grid.shape
    #for x in np.nditer(grid):
    #    print(x, end=' ')
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
            #print(grid[x,y], x,y)
            occupied_cnt = adjacent_seats(x,y,grid)
            if grid[x,y] == "#" and occupied_cnt >=4:
                gridx[x,y] = "L"
                moves += 1
            if grid[x,y] == "L" and occupied_cnt == 0:
                gridx[x,y] = "#"
                moves += 1

            if grid[x,y] == ".":
                gridx[x,y] = "."

            if gridx[x,y] == "#":
                occ += 1

            #print(occupied_cnt, grid[x,y], x,y)
    print("After:")
    print(gridx)
    return gridx, moves, occ
def main():
    with open("day11_input.txt") as fp:
        lines = fp.readlines()
    # strip each line and break into individual characters
    grid = list(map(lambda x: list(x.strip()), lines))
    seat_array = np.array(grid)
    moves = 1
    while moves:
        seat_array, moves, occ = process_arrivals(seat_array)
        print(moves, occ)

    return
    #print(grid)
    grid[3][5] = '#'
    #for line in grid:
    #    print(line)
    seat_array = np.array(grid)
    seat_array[4][6] = "Y"
    adjacent_seats(4,6,seat_array)
    seat_array[4][9] = "Z"
    adjacent_seats(3,6,seat_array)
    adjacent_seats(3,9,seat_array)
    print(seat_array)
    print(seat_array.shape)
    process_arrivals(seat_array)


if __name__ == "__main__":
    main()
