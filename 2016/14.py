# Python 3 code to demonstrate the
# working of MD5 (string - hexadecimal)

import hashlib
from itertools import groupby
from collections import defaultdict

def find_next_five(match, seed, idx):
    for i in range(idx, idx+1000):
        # initializing string
        str2hash = f'{seed}{i}'
        z = MD5_IDX[i]
        if z == '':
            # encoding GeeksforGeeks using encode()
            # then sending to md5()
            result = hashlib.md5(str2hash.encode())
            
            s = f'{result.hexdigest()}'
            MD5_IDX[i] = s
        else:
            s = z
        
        for i in range(len(s)-5):
            if s[i:i+5] == match*5:
                return True
    return False
        
def findthree(s):
    for i in range(len(s)-3):
        if s[i:i+3] == s[i]*3:
            return s[i:i+3]
        # else:
            # continue
    else:
        return ''
        
MD5_IDX = defaultdict(str)


def main():
    seed = 'ahsbgdzn'
    idx = 0
    md5_idx = defaultdict(str)
    pads = []
    
    while len(pads) != 64:
        # initializing string
        str2hash = f'{seed}{idx}'
        z = MD5_IDX[idx]
        if z == '':
            # encoding GeeksforGeeks using encode()
            # then sending to md5()
            result = hashlib.md5(str2hash.encode())
            
            s = f'{result.hexdigest()}'
            MD5_IDX[idx] = s
        else:
            s = z
        res = findthree(s)
        if len(res) == 3:
            if find_next_five(res[0], seed, idx+1):
                pads.append(f'{idx}={s}')
                # printing the equivalent hexadecimal value.
                print("The hexadecimal equivalent of hash is : ", end ="")
                print(idx, s)
            

        idx += 1

    #print(pads)
    for i,s in enumerate(pads):
        print(i,s)

if __name__ == "__main__":
    main()