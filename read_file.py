from game_master import *
import copy
import pandas as pd

list_bwin_battle = []
list_wwin_battle = []
list_dwin_battle = []
list_bstone = []
list_bboard = []
list_wstone = []
list_wboard = []
tmp_1 = []
tmp_2 = []

def conve(put_st):
    for_convert = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1),
                   (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2),
                   (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3),
                   (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4),
                   (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6),
                   (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)]
    t_x, t_y = for_convert[put_st]
    return t_x, t_y


#  ファイル名とか初期設定
tmp_count = []
print('input file path csv/.csv')
csv_name = input()
print('saving model path model/.npz')
saving_name = input()
print('black_win or white_winどっちのモデルをつくる？')
sha = input()
print('resultの保存パスを選ぶ（results以下を選択)')
result_out = str(input())
#  --------------
print('loading...なっしー！')
df = pd.read_csv(csv_name, header=None) # 文字列が含まれるので
df = df.replace('\r\n', '', regex=True)
df = df.replace('\n', '', regex=True)
tmp = df.values.tolist()
print('converting to listなっし')
print(tmp)
tmp = [x for a in tmp for x in a]
tmp_1 = [x for x in tmp if x]
a = 0
a += int(tmp_1.count('WW'))
a += int(tmp_1.count('WB'))
a += int(tmp_1.count('WD'))
print('盤面を復元するなっし！')
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
if sha == 'black_win' or 'b' or 'black':
    shi = list_bwin_battle
elif sha == 'white_win' or 'w' or 'white':
    shi = list_wwin_battle

othello = game_master()
for d in shi:
    if d == 'B':
        turn = BLACK
        continue
    elif d == 'W':
        turn = WHITE
        continue
    elif d == 100 or d == -100:
        othello = game_master()
        continue
    elif d == 64:
        if turn == BLACK:
            # deep copy　じゃないと外のリストのみこぴーされる
            list_bboard.append(copy.deepcopy(othello.board))
            list_bstone.append(d)
        elif turn == WHITE:
            list_wboard.append(copy.deepcopy(othello.board))
            list_wstone.append(d)
        continue
    else:
        if turn == BLACK:
            list_bboard.append(copy.deepcopy(othello.board))
            list_bstone.append(d)
            ax, ay = conve(int(d))
            #  白のターン
        elif turn == WHITE:
            list_wboard.append(copy.deepcopy(othello.board))
            list_wstone.append(d)
            ax, ay = conve(int(d))
        othello.put_stone(ax, ay, turn)
print('復元は終わったなっし')
if sha == 'black_win' or 'b' or 'black':
    input_board = list_bboard
    output_stone = list_bstone
elif sha == 'white_win' or 'w' or 'white':
    input_board = list_wboard
    output_stone = list_wstone




