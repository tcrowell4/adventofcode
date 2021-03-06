[(4+x)%5 for x in range(10)]
	[4, 0, 1, 2, 3, 4, 0, 1, 2, 3]
[(1+x)%2 for x in range(10)]
	[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

discs=[(4,5),(1,2)]


for disc in discs:
    start_position, positions = disc
    print([(start_position+x)%positions for x in range(10)])
    
   
>>> for disc in discs:
...     start_position, positions = disc
...     print([(start_position+x)%positions for x in range(10)])
...
[4, 0, 1, 2, 3, 4, 0, 1, 2, 3]
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]


time = 0
while True:
    if time == 20: break
    slots = []
    for i,disc in enumerate(discs):
        start_position, positions = disc
        slots.append((start_position+time+i)%positions)
    print(slots)
    time += 1