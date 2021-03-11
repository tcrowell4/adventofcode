import day14_part2 as test
s = "00000000000000000000000000000000X0XX"
print(test.countx(s))
zz = test.countx(s)
binx = test.decimalToBinary(zz)
print(binx)

x = test.bitvariations(len(binx))
print(list(x))

test.process_floating(s)
