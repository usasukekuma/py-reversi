from game_master import *

def append_list(x, y, color):
    if x == 8 and y == 8:
        z = 65
    else:
        z = x + y*8
    for cy in range(0,8):
        for cx in range(0,8):
            list_c.append(othello.board[cy][cx])
    list_c.append(color)
    list_c.append(z)


print('ランダムファイルを作るなっし')
print('試合数を選ぶなっし(0以外を入力してくださいなっし)')

battle_time = int(input())
print(str(battle_time)+'回ではじめるなっし')

player_1 = random_action
player_2 = random_action
list_c = []
for n in range(0, battle_time):
    list_a = []
    othello = game_master()
    othello.view()
    i = 0
    while not othello.can_put_list(BLACK) == [] or not othello.can_put_list(WHITE) == []:
        turn = othello.player_check(i)
        #  黒のターン
        if turn == BLACK:
            color = 'B'
            current_board = [othello.board_copy()]
            hand = '黒の'
            othello.player_print(hand)
            can_put_list = othello.can_put_list(BLACK)
            if not can_put_list == []:
                x, y = player_1(can_put_list, current_board)
                print(can_put_list)
                append_list(x, y, color)
            else:
                i += 1
                x, y = 8, 8
                append_list(x, y, color)
                continue
        #  白のターン
        elif turn == WHITE:
            color = 'W'
            current_board = [othello.board_copy()]
            hand = '白の'
            othello.player_print(hand)
            can_put_list = othello.can_put_list(WHITE)
            if not can_put_list == []:
                x, y = player_2(can_put_list, current_board)
                print(can_put_list)
                append_list(x, y, color)
            else:
                i += 1
                x, y = 8, 8
                append_list(x, y, color)
                continue
        othello.put_stone(x, y, turn)
        othello.view()
        i += 1
    tmp_w = othello.end()
    if tmp_w == b_LOSE:
        list_c.append('WW')
    elif tmp_w == b_WIN:
        list_c.append('WB')
    elif tmp_w == DRAW:
        list_c.append('WD')
    list_c.append('\n')

with open('nassyi.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(list_c)


