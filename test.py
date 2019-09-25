from game_master import *
import csv
import numpy as np

list_c = []
othello = game_master()
for x in range(0, 8):
    for y in range(0, 8):
        list_a = othello.board[y][x]
        list_c.append(list_a)
with open('sample.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(list_c)
