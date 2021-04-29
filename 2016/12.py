def process_input(cmds, part):
    register = {'a':0, 'b':0, 'c':1, 'd':0}
    
    # pass
    idx = 0
    while True:
        if idx >= len(cmds):
            break
        cmd, *v = cmds[idx]
        #print(f'idx:{idx} cmd = {cmd}  *v = {v} {type(v[0])}')
        if cmd == 'cpy':
            if isinstance(v[0],int):
                register[v[1]] = v[0]
            else:
                register[v[1]] = register[v[0]]
        if cmd == 'inc': register[v[0]] += 1
        if cmd == 'dec': register[v[0]] -= 1
        if cmd == 'jnz':
            if isinstance(v[0],int):
                j = v[0]
            else:
                j = register[v[0]]
            if  j != 0:
                idx += v[1]
            else:
                idx += 1
        else:
            idx += 1
        
        #print('****  register *****')
        #for k,v in register.items():
        #    print(k, v)
        #print('********************')
        
    
    for k,v in register.items():
        print(k, v)
        
        
 
def main():

    with open("12.in") as fp:
        cmds = [line.strip().split() for line in fp]
    print("=========", cmds)
    for l in cmds:
        for i in range(len(l)):
            try:
                
                x = int(l[i])
                is_dig = True
            except ValueError:
                is_dig = False
            if is_dig:
                l[i] = x
            

    
    print("=========", cmds)
    process_input(cmds, "part 1")
    # process_input(lines, part2, "part 2")

    return


if __name__ == "__main__":
    main()