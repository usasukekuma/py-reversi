from game_master import *
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


save_list(othello, file_name)


