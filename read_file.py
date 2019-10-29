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

ucon = {0: (0, 0), 1: (1, 0), 2: (2, 0), 3: (3, 0), 4: (4, 0), 5: (5, 0), 6: (6, 0),7: (7, 0),
        8: (0, 1), 9: (1, 1), 10: (2, 1), 11: (3, 1), 12: (4, 1), 13: (5, 1), 14: (6, 1),'H2': (7, 1),
            'A3': (0, 2), 'B3': (1, 2), 'C3': (2, 2), 'D3': (3, 2), 'E3': (4, 2), 'F3': (5, 2), 'G3': (6, 2),'H3': (7, 2),
            'A4': (0, 3), 'B4': (1, 3), 'C4': (2, 3), 'D4': (3, 3), 'E4': (4, 3), 'F4': (5, 3), 'G4': (6, 3),'H4': (7, 3),
            'A5': (0, 4), 'B5': (1, 4), 'C5': (2, 4), 'D5': (3, 4), 'E5': (4, 4), 'F5': (5, 4), 'G5': (6, 4),'H5': (7, 4),
            'A6': (0, 5), 'B6': (1, 5), 'C6': (2, 5), 'D6': (3, 5), 'E6': (4, 5), 'F6': (5, 5), 'G6': (6, 5),'H6': (7, 5),
            'A7': (0, 6), 'B7': (1, 6), 'C7': (2, 6), 'D7': (3, 6), 'E7': (4, 6), 'F7': (5, 6), 'G7': (6, 6),'H7': (7, 6),
            'A8': (0, 7), 'B8': (1, 7), 'C8': (2, 7), 'D8': (3, 7), 'E8': (4, 7), 'F8': (5, 7), 'G8': (6, 7),'H8': (7, 7)}

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
print(tmp1)
tmp_2 = [x for x in tmp1 if x]
print(tmp_2)
print('盤面を復元するなっし！')
wwww = 0

for che in tmp_2:
    if che == b_WIN:
        list_bwin_battle.extend(tmp_3)
        list_bwin_battle.append(END)
        tmp_3 = []
        wwww += 1
    elif che == b_LOSE:
        list_wwin_battle.extend(tmp_3)
        list_wwin_battle.append(END)
        tmp_3 = []
    elif che == DRAW:
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

othello = game_master()
shi_len = len(shi)
for d in shi:
    if d == 'B':
        turn = BLACK
        continue
    elif d == 'W':
        turn = WHITE
        continue
    elif d == END:
        judge, score_B, score_W = othello.end()
        if ttt == 'n':
            print(score_B, score_W)
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
            print('b')
            print(score_B, score_W)
            if score_B - score_W >= score_point:
                print('a')
                print(score_B,score_W)
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
        continue
print('復元は終わったなっし')
print(wb)
if sha == 'black_win' or 'b' or 'black':
    input_board = list_bboard
    output_stone = list_bstone
elif sha == 'white_win' or 'w' or 'white':
    input_board = list_wboard
    output_stone = list_wstone
print(wwww)
print(tmp_2.count(600))
print(input_board)
print(output_stone)