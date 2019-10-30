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
t_list_bstone = []
t_list_bboard = []
t_list_wstone = []
t_list_wboard = []
tmp_2 = []
tmp_3 = []
wb = 0
END = 859

def conve(put_st):
    for_convert = {0:(0, 0), 1: (1, 0), 2:(2, 0), 3:(3, 0), 4:(4, 0), 5:(5, 0), 6:(6, 0), 7:(7, 0),
                   8:(0, 1), 9: (1, 1), 10:(2, 1), 11:(3, 1), 12:(4, 1), 13:(5, 1), 14:(6, 1),15:(7, 1),
                   16:(0, 2), 17: (1, 2), 18:(2, 2), 19:(3, 2), 20:(4, 2), 21:(5, 2), 22:(6, 2), 23:(7, 2),
                   24:(0, 3), 25: (1, 3), 26:(2, 3), 27:(3, 3), 28:(4, 3), 29:(5, 3), 30:(6, 3), 31:(7, 3),
                   32:(0, 4), 33: (1, 4), 34:(2, 4), 35:(3, 4), 36:(4, 4), 37:(5, 4), 38:(6, 4), 39:(7, 4),
                   40:(0, 5), 41: (1, 5),42:(2, 5), 43:(3, 5), 44:(4, 5), 45:(5, 5), 46:(6, 5), 47:(7, 5),
                   48:(0, 6), 49:(1, 6), 50:(2, 6), 51:(3, 6), 52:(4, 6), 53:(5, 6),54:(6, 6), 55:(7, 6),
                   56:(0, 7), 57:(1, 7), 58:(2, 7), 59:(3, 7), 60:(4, 7), 61:(5, 7), 62:(6, 7), 63:(7, 7)}
    t = for_convert[put_st]
    print(t)
    t_x, t_y = t
    return t_x, t_y



#  ファイル名とか初期設定
tmp_count = []
print('input file path csv/.csv')
csv_name = input()
print('saving model path model/.npz')
saving_name = input()
print('bwin or blose')
sha = input()
print('スコアを考慮しますか？ y or n')
ttt = input()
if ttt == 'y':
    print('黒が○石数差をつけて勝利')
    score_point = int(input())
print('resultの保存パスを選ぶ（results以下を選択)')
result_out = str(input())
#  --------------
print('loading...なっしー！')
df = pd.read_csv(csv_name, header=None)  # 文字列が含まれるので
df = df.replace('\r\n', '', regex=True)
df = df.replace('\n', '', regex=True)
tmp = df.values.tolist()
print('converting to listなっし')
tmp1 = [x for a in tmp for x in a]
tmp_2 = [x for x in tmp1 if not x == '']
print('盤面を復元するなっし！')
wwww = 0

for che in tmp_2:
    if che == 'WB':
        list_bwin_battle.extend(tmp_3)
        list_bwin_battle.append(END)
        tmp_3 = []
        wwww += 1
    elif che == 'WW':
        list_wwin_battle.extend(tmp_3)
        list_wwin_battle.append(END)
        tmp_3 = []
    elif che == 'WD':
        list_dwin_battle.extend(tmp_3)
        list_dwin_battle.append(END)
        tmp_3 = []
    else:
        tmp_3.append(che)

#  ボード復元
if sha == 'b_win' or 'b':
    shi = list_bwin_battle
elif sha == 'b_lose' or 'l':
    shi = list_wwin_battle
print(tmp_2.count('WB'))
tmp1 = []
tmp_2 = []
othello = game_master()
shi_len = len(shi)

for g in range(0,len(shi)):
    d = shi.pop(0)
    if d == 'B':
        turn = BLACK
        continue
    elif d == 'W':
        turn = WHITE
        continue
    elif d == END:
        judge, score_B, score_W = othello.end()
        if ttt == 'n':
            list_bboard.extend(copy.deepcopy(t_list_bboard))
            list_bstone.extend(copy.deepcopy(t_list_bstone))
            t_list_bboard = []
            t_list_bstone = []
            t_list_wstone = []
            t_list_wboard = []
            othello = game_master()
            wb += 1
            continue
        elif ttt == 'y':
            if score_B - score_W >= score_point:
                list_bboard.extend(copy.deepcopy(t_list_bboard))
                list_bstone.extend(copy.deepcopy(t_list_bstone))
                t_list_bboard = []
                t_list_bstone = []
                t_list_wstone = []
                t_list_wboard = []
                othello = game_master()
                wb += 1
                continue
            else:
                t_list_bboard = []
                t_list_bstone = []
                t_list_wstone = []
                t_list_wboard = []
                othello = game_master()
                continue
        elif d == 64:
            if turn == BLACK:
                # deep copy　じゃないと外のリストのみこぴーされる
                t_list_bboard.append(copy.deepcopy(othello.board))
                t_list_bstone.append(d)
            elif turn == WHITE:
                t_list_wboard.append(copy.deepcopy(othello.board))
                t_list_wstone.append(d)
            continue
        else:
            if turn == BLACK:
                t_list_bboard.append(copy.deepcopy(othello.board))
                t_list_bstone.append(d)
                ax, ay = conve(int(d))
                #  白のターン
            elif turn == WHITE:
                t_list_wboard.append(copy.deepcopy(othello.board))
                t_list_wstone.append(d)
                ax, ay = conve(int(d))
            othello.put_stone(ax, ay, turn)

print('復元は終わったなっし')
print(wb)
if sha == 'black_win' or 'b' or 'black':
    input_board = list_bboard
    output_stone = list_bstone
elif sha == 'white_win' or 'w' or 'white':
    input_board = list_wboard
    output_stone = list_wstone
print(wwww)
