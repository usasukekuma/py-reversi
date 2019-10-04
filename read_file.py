from game_master import *
import pandas as pd
import itertools


list_bwin_battle = []
list_wwin_battle = []
list_dwin_battle = []
list_bstone = []
lits_bboard = []
list_wstone = []
list_wboard = []

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
        list_bwin_battle.extend(tmp_2)
        list_bwin_battle.append(b_WIN)
        tmp_2 = []
    elif c == 'WW':
        list_wwin_battle.extend(tmp_2)
        list_wwin_battle.append(b_LOSE)
        tmp_2 = []
    elif c == 'WD':
        list_dwin_battle.extend(tmp_2)
        tmp_2 = []
    else:
        tmp_2.append(c)

#  ボード復元
print(list_bwin_battle)
othello = game_master()
othello.view()
for d in list_bwin_battle:
    othello.view()
    if d == 'B':
        turn = BLACK
        continue
    elif d == 'W':
        turn = WHITE
        continue
    elif d == 100:
        othello = game_master()
        turn = None
        continue
    elif d == 65:
        if turn == BLACK:
            lits_bboard.append(othello.board_copy())
            list_bstone.append(d)
        continue
    else:
        if turn == BLACK:
            lits_bboard.append(othello.board)
            list_bstone.append(d)
        x, y, = conv(d)
        othello.put_stone(x, y, turn)
print(lits_bboard)
print(list_bwin_battle)
print(list_bstone)



