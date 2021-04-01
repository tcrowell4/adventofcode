for row in x:
    gen = row[1::2]
    print(gen)
    g = np.sum(gen)         #finds the number of generators
    mc = row[2::2]
    print(mc)
    m = np.sum(mc)
    print(f'Gen = {g} Microchip {m}')
    for i in range(len(mc)):
        if mc[i] == 1:
            if gen[i] == 1:
                print('chip protected')
            else:
                print('unprotected')
                if g>0: print('fried chip')
                    
for row in x:
    gen = row[1::2]
    print(gen)
    g = np.sum(gen)         #finds the number of generators
    mc = row[2::2]
    print(mc)
    m = np.sum(mc)
    print(f'Gen = {g} Microchip {m}')
    for i in range(len(mc)):
        if mc[i] > gen[i] and g>0:
            print('unprotected')
            print('fried chip')
            
            
queue = collections.deque([x])
print(queue)