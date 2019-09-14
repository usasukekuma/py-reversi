from random_player import *
import sys

def make_list(self, act_x):
    x, y = act_x
    if x == 0 and y == 0:
        c = 0
    elif act_x == PASS:
        c = 65
    else:
        c = x + (8 * y)
    tmp = np.array(self.board_copy())
    current_board = tmp.flatten()
    self.game_list.append(current_board)
    self.game_list.append(c)

def save_list(self, name):
    end_file = self.game_list
    with open(name + '.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(end_file)

print('学習用ファイル（ランダムバージョン）をつくるなっしー\n試合数を選ぶなっしー:')
battle_time = input(int())
print(str(battle_time)+'回試合でつくるなっしー')
print('ファイル名をきめるなっしー:')
file_name = input()
print(str(file_name)+'で保存するなっしー')

for n in range(0, battle_time):
    othello = random_player()
    othello.view()
    turn = BLACK
    i = 0
    while not othello.can_put_list(BLACK) == [] and not othello.can_put_list(WHITE) == []:
        turn, PASS_ = othello.player_check(i)
        if PASS_ == PASS:
            act_x = PASS
        if turn == BLACK:
            hand = '黒の'
            othello.player_print(hand)
            t_x, t_y = othello.random_action(BLACK)
            if not list(set([(t_x, t_y)]) & set(othello.can_put_list(BLACK))) == []:
                x, y = t_x, t_y
            else:
                print('ERROR')
                sys.exit()

        elif turn == WHITE:
            hand = '白の'
            othello.player_print(hand)
            t_x, t_y = othello.random_action(WHITE)
            if not list(set([(t_x, t_y)]) & set(othello.can_put_list(WHITE))) == []:
                x, y = t_x, t_y
            else:
                print('ERROR')
                sys.exit()
        othello.put_stone(x, y, turn)
        othello.view()
        i += 1


