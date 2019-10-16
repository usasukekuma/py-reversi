from game_master import *
import pickle
from basic_player import *
import csv

def xy_converter(x, y):
    if x == 8 and y == 8:
        z = 64
    else:
        z = x + y*8
    return z

def csv_list(x, y, color):
    """"
    list_c.append(othello.board_copy())
    """
    list_c.append(color)
    z = xy_converter(x, y)
    list_c.append(z)


def pickle_list(x, y, color):
    list_c.append(othello.board_copy())
    list_c.append(color)
    z =xy_converter(x, y)
    list_c.append(z)


def csv_m(f_name):
    with open(f_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(list_c)

u= 999
print('ランダムファイルを作るなっし\nファイル名を決めるなっし')
f_name = str(input())
print('プレイヤー1を選ぶなっし ランダム→r or 入力→ｎ')
p1 = str(input())
print('プレイヤー2を選ぶなっし ランダム→r or 入力→ｎ')
p2 = str(input())
if p1 == 'r':
    player_1 = random_action
elif p1 == 'n':
    player_1 = input_player
if p2 == 'r':
    player_2 = random_action
elif p2 == 'n':
    player_2 = input_player
print('試合数を選ぶなっし(0以外を入力してくださいなっし)')
battle_time = int(input())
print(str(battle_time)+'回ではじめるなっし')
f_save = csv_m
append_l = csv_list

list_c = []
for n in range(0, battle_time):
    list_a = []
    othello = game_master()
    othello.view()
    i = 0
    k = 0
    while not k == 100:
        turn = othello.player_check(i)
        #  黒のターン
        if turn == BLACK:
            color = 'B'
            print('黒の番です')
            current_board = [othello.board_copy()]
            can_put_list = othello.can_put_list(BLACK)
            if not can_put_list == []:
                x, y, u = player_1(can_put_list, current_board, u)
                print(can_put_list)
                append_l(x, y, color)
            else:
                i += 1
                x, y = 8, 8
                append_l(x, y, color)
                continue
        #  白のターン
        elif turn == WHITE:
            color = 'W'
            print('白の番です')
            can_put_list = othello.can_put_list(WHITE)
            if not can_put_list == []:
                x, y, u = player_2(can_put_list, current_board, u)
                print(can_put_list)
                append_l(x, y, color)
            else:
                i += 1
                x, y = 8, 8
                append_l(x, y, color)
                continue
        othello.put_stone(x, y, turn)
        othello.view()
        i += 1
        k = 0
        if othello.can_put_list(BLACK) == []:
            k += 50
        if othello.can_put_list(WHITE) == []:
            k += 50
    tmp_w = othello.end()
    if tmp_w == b_LOSE:
        list_c.append('WW')
    elif tmp_w == b_WIN:
        list_c.append('WB')
    elif tmp_w == DRAW:
        list_c.append('WD')
    list_c.append('\n')
print('saving..........')
f_save(f_name)
print('complete!')


