f = [[int(line), 0] for line in open('day10_sample.txt','r').readlines()]
f.append([0, 1])
f.sort()
print(f)

for idx in range(0, len(f)):
    for jdx in range(1, 4):
        if idx-jdx < 0:
            break
        if f[idx][0] - f[idx-jdx][0] <= 3:
            f[idx][1] += f[idx-jdx][1]

print(f[-1][1])
print(f)
