# Python program to find the shortest
# path between a given source cell
# to a destination cell.

from collections import deque
ROW = 45
COL = 45
DIST_50 = 0

# To store matrix cell cordinates
class Point:
    def __init__(self,x: int, y: int):
        self.x = x
        self.y = y

# A data structure for queue used in BFS
class queueNode:
    def __init__(self,pt: Point, dist: int):
        self.pt = pt # The cordinates of the cell
        self.dist = dist # Cell's distance from the source

# Check whether given cell(row,col)
# is a valid cell or not
def isValid(row: int, col: int):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)

# These arrays are used to get row and column
# numbers of 4 neighbours of a given cell
rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]

# Function to find the shortest path between
# a given source cell to a destination cell.
def BFS(mat, src: Point, dest: Point):
    global DIST_50
    
   
    
    # check source and destination cell
    # of the matrix have value 1
    if mat[src.x][src.y]!= '.' or mat[dest.x][dest.y]!= '.':
        return -1
    
    visited = [[False for i in range(COL)]
                    for j in range(ROW)]
    
    # Mark the source cell as visited
    visited[src.x][src.y] = True
    
    # Create a queue for BFS
    q = deque()
    
    # Distance of source cell is 0
    s = queueNode(src,0)
    q.append(s) # Enqueue source cell
    
    # Do a BFS starting from source cell
    while q:

        curr = q.popleft() # Dequeue the front cell
        
        if curr.dist <= 50:
            DIST_50 += 1
            print(curr.dist, curr.pt.x,curr.pt.y)
        
        # If we have reached the destination cell,
        # we are done
        pt = curr.pt
        if pt.x == dest.x and pt.y == dest.y:
            return curr.dist
        
        # Otherwise enqueue its adjacent cells
        for i in range(4):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]
            
            # if adjacent cell is valid, has path
            # and not visited yet, enqueue it.
            if (isValid(row,col) and
                mat[row][col] == '.' and
                not visited[row][col]):
                
                
                visited[row][col] = True
                Adjcell = queueNode(Point(row,col),
                                    curr.dist+1)
                q.append(Adjcell)
    
    # Return -1 if destination cannot be reached
    return -1



# Function to count total bits in a number
 
def fillarray(x,y, fav):
    val = (x*x) + (3*x) + (2*x*y) + y + (y*y)
    b = bin(val+fav).count("1")
    # print(f'{x}:{y} val {val} val+fav {val + fav} bits {b} ')
    if (b % 2) == 0:
       return '.'
    else:
       return '#'
       
def main():
    global ROW, COL

    #fav = 10
    fav = 1350
    
    rows, cols = (ROW, COL)

    mat = [[ fillarray(i,j,fav) for i in range(cols)] for j in range(rows)]
    
    for row in mat:
        #print(row)
        print(''.join(row))
    
                
    #return

# Driver code


    #source = Point(1,1)
    #dest = Point(4,7)
    source = Point(1,1)
    dest = Point(39,31)
    
    dist = BFS(mat,source,dest)
    
    if dist!=-1:
        print("Shortest Path is",dist)
    else:
        print("Shortest Path doesn't exist")

    print("DIST_50=", DIST_50)

if __name__ == "__main__":
    main()