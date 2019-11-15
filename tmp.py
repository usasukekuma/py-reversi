p = [(0,1),(1,1),(1,2)]
l = [0, 1, 2]
s = l[p.index((1, 1))]
l[p.index((1, 1))] = s+3
print(l)