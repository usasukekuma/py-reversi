from game_master import *
import pandas as pd
import itertools


list_bwin = []
list_wwin = []
list_dwin = []
n_f = [list_bwin, list_wwin, list_dwin]
tmp_count = []


df = pd.read_csv('a.csv', header=None) # 文字列が含まれるので
df = df.replace('\r\n', '', regex=True)
tmp = df.values.tolist()
tmp = list(itertools.chain.from_iterable(tmp))
tmp_1 = [x for x in tmp if x]
print(tmp_1)
a = 0
a += int(tmp_1.count('WW'))
a += int(tmp_1.count('WB'))
a += int(tmp_1.count('WD'))
tmp_2 = []
for c in tmp_1:
    if c == 'WB':
        list_bwin.extend(tmp_2)
        list_bwin.append(b_WIN)
        tmp_2 = []
    elif c == 'WW':
        list_wwin.extend(tmp_2)
        list_wwin.append(b_LOSE)
        tmp_2 = []
    elif c == 'WD':
        list_dwin.extend(tmp_2)
        tmp_2 = []
    else:
        tmp_2.append(c)
print(list_bwin)
print(list_bwin.count(100))
othello = game_master()
for d in list_bwin:
    othello.view()
    if d == 'B':
        turn = BLACK
        continue
    elif d == 'W':
        turn = WHITE
        continue
    elif d == 100:
        othello = game_master()
    x, y = conv(d)
    othello.put_stone(x, y, turn)

