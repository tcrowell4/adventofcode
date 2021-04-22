# Function to count total bits in a number
 
def fillarray(x,y, fav):
    val = (x*x) + (3*x) + (2*x*y) + y + (y*y)
    b = bin(val+fav).count("1")
    print(f'{x}:{y} val {val} val+fav {val + fav} bits {b} ')
    if (b % 2) == 0:
       return '.'
    else:
       return '#'
       
def main():

    fav = 10
    
    rows, cols = (7, 10)
    arr = [[ fillarray(i,j,fav) for i in range(cols)] for j in range(rows)]
    
    for row in arr:
        print(''.join(row))
    
                
    return


if __name__ == "__main__":
    main()