import sys
with open("day19_sample.txt") as f:
    fields, my_ticket = [chunk.split('\n') for chunk in f.read().strip().split('\n\n')]
        
print(fields, my_ticket)

# The list comprehension converts to the following
with open("day19_sample.txt") as f:
    # read the whole file
    x = f.read()
    print(x)
    # strip the trailing \n
    y =  x.strip()
    print("Strip\n",y)
    # split the string into chunks with double \n\n
    # converts into a list
    z =  y.split('\n\n')
    print("Split\n",z)
    #store each chunk in a separate field
    fields = z[0].split('\n')
    tickets = z[1].split('\n')
    print("Fields\n",fields)
    print("Ticket\n",my_ticket)

""" 
>>> fields = z[0].split('\n')
>>> fields
['0: 4 1 5', '1: 2 3 | 3 2', '2: 4 4 | 5 5', '3: 4 5 | 5 4', '4: "a"', #'5: "b"']
>>> tickets = z[1].split('\n')
>>> tickets
['ababbb', 'bababa', 'abbbab', 'aaabbb', 'aaaabbb']
"""


sys.exit()

rules = dict()
for line in fields:
    key, ranges = line.split(': ')
    rules[key] = [list(map(int, r.split('-'))) for r in ranges.split('or')]