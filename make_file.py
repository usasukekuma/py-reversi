from game_master import *
from basic_player import *
import csv
import copy
kihu_put_list = []
bbw =0

def kihu_load():

    ucon = {'A1': (0, 0), 'B1': (1, 0), 'C1': (2, 0), 'D1': (3, 0), 'E1': (4, 0), 'F1': (5, 0), 'G1': (6, 0),'H1': (7, 0),
            'A2': (0, 1), 'B2': (1, 1), 'C2': (2, 1), 'D2': (3, 1), 'E2': (4, 1), 'F2': (5, 1), 'G2': (6, 1),'H2': (7, 1),
            'A3': (0, 2), 'B3': (1, 2), 'C3': (2, 2), 'D3': (3, 2), 'E3': (4, 2), 'F3': (5, 2), 'G3': (6, 2),'H3': (7, 2),
            'A4': (0, 3), 'B4': (1, 3), 'C4': (2, 3), 'D4': (3, 3), 'E4': (4, 3), 'F4': (5, 3), 'G4': (6, 3),'H4': (7, 3),
            'A5': (0, 4), 'B5': (1, 4), 'C5': (2, 4), 'D5': (3, 4), 'E5': (4, 4), 'F5': (5, 4), 'G5': (6, 4),'H5': (7, 4),
            'A6': (0, 5), 'B6': (1, 5), 'C6': (2, 5), 'D6': (3, 5), 'E6': (4, 5), 'F6': (5, 5), 'G6': (6, 5),'H6': (7, 5),
            'A7': (0, 6), 'B7': (1, 6), 'C7': (2, 6), 'D7': (3, 6), 'E7': (4, 6), 'F7': (5, 6), 'G7': (6, 6),'H7': (7, 6),
            'A8': (0, 7), 'B8': (1, 7), 'C8': (2, 7), 'D8': (3, 7), 'E8': (4, 7), 'F8': (5, 7), 'G8': (6, 7),'H8': (7, 7)}
    new_kihu = []
    in_kihu_put = []
    print('棋譜を入力')
    kihu = list(input())
    while not kihu == []:
        k = []
        k.append(kihu.pop(0))
        k.append(kihu.pop(0))
        new_kihu.append(''.join(k))
    for kihua in new_kihu:
        in_kihu_put.append(ucon[kihua])
    return in_kihu_put

def kihu_player(trash0, trash1, kihu_count):
    x, y = kihu_put_list[kihu_count]
    return x, y, 0


def xy_converter(x, y):
    if x == 8 and y == 8:
        z = 64
    else:
        z = x + y*8
    return z



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
    print('プレイヤー1を選ぶなっし ランダム→r or 入力→ｎ or 棋譜→k')
    p1 = str(input())
    print('プレイヤー2を選ぶなっし ランダム→r or 入力→ｎ or 棋譜→k')
    p2 = str(input())
    if p1 == 'r':
        player_1 = random_action
    elif p1 == 'n':
        player_1 = input_player
    elif p1 == 'k':
        player_1 = kihu_player
    if p2 == 'r':
        player_2 = random_action
    elif p2 == 'n':
        player_2 = input_player
    elif p2 == 'k':
        player_2 = kihu_player
    if p1 == 'k':
        kl = kihu_load()
        kihu_put_list.extend(copy.deepcopy(kl))
    print('試合数を選ぶなっし(0以外を入力してくださいなっし)')
    battle_time = int(input())
    print(str(battle_time)+'回ではじめるなっし')
    list_c = []
    for n in range(0, battle_time):
        list_a = []
        othello = game_master()
        i = 0
        k = 0
        kihu_count = 0
        while not k == 100:
            turn = othello.player_check(i)
            #  黒のターン
            if turn == BLACK:
                color = 'B'
                current_board = [othello.board_copy()]
                can_put_list = othello.can_put_list(BLACK)
                if not can_put_list == []:
                    x, y = player_1(can_put_list, current_board, kihu_count)
                    z = xy_converter(x, y)
                    list_c.append(z)
                else:
                    i += 1
                    x, y = 8, 8
                    list_c.append(color)
                    z = xy_converter(x, y)
                    list_c.append(z)

                    continue
            #  白のターン
            elif turn == WHITE:
                color = 'W'
                current_board = [othello.board_copy()]
                can_put_list = othello.can_put_list(WHITE)
                if not can_put_list == []:
                    x, y= player_2(can_put_list, current_board, kihu_count)
                    list_c.append(color)
                    z = xy_converter(x, y)
                    list_c.append(z)

                else:
                    i += 1
                    x, y = 8, 8
                    list_c.append(color)
                    z = xy_converter(x, y)
                    list_c.append(z)
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
        print(score_B,score_W)
        wscore = score_B - score_W
        if wscore == 0:
            list_c.append('WD')
            print('DRAW')
        elif wscore >= 1:
            list_c.append('WB')
            bbw+=1
            print('WIN')
        else:
            list_c.append('WW')
            print('Lose')
        list_c.append('\n')
        print(list_c[-2])
    print('saving..........')
    f_save(f_name)
    print('complete!')
    print(bbw)

