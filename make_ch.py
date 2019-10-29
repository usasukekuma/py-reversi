from game_master import *
from basic_player import *
import csv
import copy
kihu_put_list = []



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

def new_csv(f_name):
    with open(f_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(list_c)

def a_csv(f_name):
    with open(f_name, 'a', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(list_c)


if __name__ == "__main__":
    print('新規 n or 追記 a')
    ty = str(input())
    if ty == 'n':
        print('ファイル名を決めるなっし')
        f_name = str(input())
        f_save = new_csv
    elif ty == 'a':
        print('ファイルパスを入力')
        f_name = str(input())
        f_save = a_csv
    print('ch_pla npz path')
    npz = str(input())
    player_1 = ch_player
    player_2 = random_action
    print('試合数を選ぶなっし(0以外を入力してくださいなっし)')
    battle_time = int(input())
    print(str(battle_time)+'回ではじめるなっし')
    append_l = csv_list
    list_c = []
    for n in range(0, battle_time):
        list_a = []
        othello = game_master()
        othello.view()
        i = 0
        k = 0
        kihu_count = 0
        while not k == 100:
            turn = othello.player_check(i)
            #  黒のターン
            if turn == BLACK:
                color = 'B'
                print('黒の番です')
                current_board = [othello.board_copy()]
                can_put_list = othello.can_put_list(BLACK)
                if not can_put_list == []:
                    x, y, u = player_1(can_put_list, current_board, npz)
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
                current_board = [othello.board_copy()]
                can_put_list = othello.can_put_list(WHITE)
                if not can_put_list == []:
                    x, y, u = player_2(can_put_list, current_board, kihu_count)
                    print(can_put_list)
                    append_l(x, y, color)
                else:
                    i += 1
                    x, y = 8, 8
                    append_l(x, y, color)
                    continue
            othello.put_stone(x, y, turn)
            othello.view()
            kihu_count += 1
            i += 1
            k = 0
            if othello.can_put_list(BLACK) == []:
                k += 50
            if othello.can_put_list(WHITE) == []:
                k += 50
        tmp_w, score_B, score_W = othello.end()
        if score_W > score_B:
            list_c.append('WW')
        elif score_W < score_B:
            list_c.append('WB')
        elif score_W == score_B:
            list_c.append('WD')
        list_c.append('\n')
    print('saving..........')
    f_save(f_name)
    print('complete!')


