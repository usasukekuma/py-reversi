""""
from game_master import *
import csv
import numpy as np

with open('nassyi.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    battle_data = [row for row in reader]
print('csv生データ'+str(battle_data))

for i in range(0,64):
    for_convert = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
                   (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),
                   (0,2),(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),
                   (0,3),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(7,3),
                   (0,4),(1,4),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4),
                   (0,5),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(7,5),
                   (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6),
                   (0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7)]

    print('input')
    x = int(input())
    y = for_convert[x]
    print(y)
"""
import pickle
with open('a.pickle', 'rb') as f:
    c =pickle.load(f)
print(type(c))
print(c)

