import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for row in arr:
  for col in row:
    print(col)
    
array1 = np.arange(16).reshape(4,4)
rule = ['toggle', 0, 1, 2, 3]
cmd, row_from, col_from, row_to, col_to = rule
print(arr[row_from:row_to, col_from:col_to])

light_grid = np.full((4, 4), False, dtype=bool)
print(light_grid[row_from:row_to, col_from:col_to])
light_grid[row_from:row_to, col_from:col_to] = True
print(light_grid[row_from:row_to, col_from:col_to])



def test(rule, arr):
    print("===== TEST ==")
    cmd, row_from, col_from, row_to, col_to = rule
    print(arr[row_from:row_to, col_from:col_to])
    arr[row_from:row_to, col_from:col_to] = False
    print(arr[row_from:row_to, col_from:col_to])

test(rule, light_grid)

def rules(rule, arr):
    
    #print("=======RULES===")
    #print(arr)
    cmd, row_from, col_from, row_to, col_to = rule
    if cmd == "turn on":
        # print(arr[row_from:row_to, col_from:col_to])
        arr[row_from:row_to, col_from:col_to] = True
        # print(arr[row_from:row_to, col_from:col_to])
    elif cmd == "turn off":
        arr[row_from:row_to, col_from:col_to] = True
        #print(arr[row_from:row_to, col_from:col_to])
    elif cmd == "toggle":
        #print("TOGGLE:\n\n", arr[row_from:row_to, col_from:col_to])
        subarr = arr[row_from:row_to, col_from:col_to]
        for idx, x in np.ndenumerate(subarr):
          #print(idx, x)
          subarr[idx[0],idx[1]] = not x
  
    print(arr)
    
    return
    
rules(rule, light_grid)
