import csv
tmp = []
with open('k.csv') as f:
    for row in f.read().splitlines():
        tmp.append(list(row))

print(tmp[203])
