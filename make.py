from game_master import *

print('ランダムファイルを作るなっし')
print('試合数を選ぶなっし(0以外を入力してくださいなっし)')

battle_time = int(input())
print(str(battle_time)+'回ではじめるなっし')

player_1 = random_action
player_2 = random_action

for n in range(0, battle_time):
    othello = game_master()
    othello.view()
    i = 0
    nyu = 0
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
            else:
                i += 1
                nya = 65
                continue
        #  白のターン
        elif turn == WHITE:
            current_board = [othello.board_copy()]
            hand = '白の'
            othello.player_print(hand)
            can_put_list = othello.can_put_list(WHITE)
            if not can_put_list == []:
                x, y = player_2(can_put_list, current_board)
                print(can_put_list)
            else:
                i += 1
                nya = 65
                continue
        othello.put_stone(x, y, turn)
        othello.view()
        i += 1
    tmp_w = othello.end()
    if tmp_w == b_LOSE:
        W_winner_count += 1
    elif tmp_w == b_WIN:
        B_winner_count += 1
    elif tmp_w == DRAW:
        D_winner_count += 1


