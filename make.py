from game_master import *


print('ランダムファイルを作るなっし')
print('試合数を選ぶなっし(0以外を入力してくださいなっし)')

battle_time = int(input())
print(str(battle_time)+'回ではじめるなっし')

player_1 = random_action
player_2 = random_action
list_c = []

for n in range(0, battle_time):
    othello = game_master()
    othello.view()
    i = 0
    while not othello.can_put_list(BLACK) == [] or not othello.can_put_list(WHITE) == []:
        turn = othello.player_check(i)
        #  黒のターン
        if turn == BLACK:
            current_board = [othello.board_copy()]
            hand = '黒の'
            othello.player_print(hand)
            can_put_list = othello.can_put_list(BLACK)
            if not can_put_list == []:
                x, y = player_1(can_put_list, current_board)
                print(can_put_list)
                nya = othello.put_convert(x, y)
                nyu = 'B'
            else:
                i += 1
                nya = 65
        #  白のターン
        elif turn == WHITE:
            current_board = [othello.board_copy()]
            hand = '白の'
            othello.player_print(hand)
            can_put_list = othello.can_put_list(WHITE)
            if not can_put_list == []:
                x, y = player_2(can_put_list, current_board)
                print(can_put_list)
                nya = othello.put_convert(x, y)
                nyu = 'W'
            else:
                i += 1
                nya = 65
        for cy in range(0, 8):
            for cx in range(0, 8):
                list_a = othello.board[cy][cx]
                list_c.append(list_a)
        list_c.append(nyu)
        list_c.append(nya)
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
with open('sample.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(list_c)


