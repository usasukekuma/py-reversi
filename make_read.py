from game_master import *
from basic_player import *
import copy


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

def xy_converter(x, y):
    if x == 8 and y == 8:
        z = 64
    else:
        z = x + y*8
    return z



print('input数を選ぶなっし(0以外を入力してくださいなっし)')
battle_time = int(input())
print('bwin or wwin')
sha = input()
print('スコアを考慮しますか？ y or n')
ttt = input()
if ttt == 'y':
    print('黒が○石数差以上をつけて勝利')
    score_point = int(input())
print('saving model path model/.npz')
saving_name = input()
print('resultの保存パスを選ぶ（results以下を選択)')
result_out = str(input())
print(str(battle_time)+'回ではじめるなっし')
turn_count = 0
while not turn_count == battle_time:
    print(str((turn_count/battle_time)*100)+'%')
    othello = game_master()
    i = 0
    k = 0
    t_list_bboard = []
    t_list_bstone = []
    t_list_wstone = []
    t_list_wboard = []
    while not k == 100:
        turn = othello.player_check(i)
        #  黒のターン
        if turn == BLACK:
            color = 'B'
            can_put_list = othello.can_put_list(BLACK)
            if not can_put_list == []:
                x, y = random_action(can_put_list, 0, 0)
                z = xy_converter(x, y)
                t_list_bboard.append(copy.deepcopy(othello.board))
                t_list_bstone.append(z)
            else:
                i += 1
                x, y = 8, 8
                z = xy_converter(x, y)
                t_list_bboard.append(copy.deepcopy(othello.board))
                t_list_bstone.append(z)
                continue
            #  白のターン
        elif turn == WHITE:
            color = 'W'
            current_board = [othello.board_copy()]
            can_put_list = othello.can_put_list(WHITE)
            if not can_put_list == []:
                x, y = random_action(can_put_list, 0, 0)
                z = xy_converter(x, y)
                t_list_wboard.append(copy.deepcopy(othello.board))
                t_list_wstone.append(z)
            else:
                i += 1
                x, y = 8, 8
                z = xy_converter(x, y)
                t_list_wboard.append(copy.deepcopy(othello.board))
                t_list_wstone.append(z)
                continue
        othello.put_stone(x, y, turn)
        i += 1
        k = 0
        if othello.can_put_list(BLACK) == []:
            k += 50
        if othello.can_put_list(WHITE) == []:
            k += 50
    tmp_w, score_B, score_W = othello.end()
    if sha == 'black_win' or 'b' or 'black':
        if ttt == 'y':
            if score_B - score_W >= score_point:
                list_bboard.extend(copy.deepcopy(t_list_bboard))
                list_bstone.extend(copy.deepcopy(t_list_bstone))
                turn_count += 1
        elif ttt == 'n':
            if score_B > score_W:
                list_bboard.extend(copy.deepcopy(t_list_bboard))
                list_bstone.extend(copy.deepcopy(t_list_bstone))
                turn_count += 1
    elif sha == 'white_win' or 'w' or 'white':
        if ttt == 'y':
            if score_W - score_B >= score_point:
                list_wboard.extend(copy.deepcopy(t_list_bboard))
                list_wstone.extend(copy.deepcopy(t_list_bstone))
                turn_count += 1
        elif ttt == 'n':
            if score_W > score_W:
                list_wboard.extend(copy.deepcopy(t_list_bboard))
                list_wstone.extend(copy.deepcopy(t_list_bstone))
                turn_count += 1
print('100%')
if sha == 'black_win' or 'b' or 'black':
    input_board = list_bboard
    output_stone = list_bstone
elif sha == 'white_win' or 'w' or 'white':
    input_board = list_wboard
    output_stone = list_wstone



