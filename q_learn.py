import random
from game_master import *

class Q_Learning(game_master):
    def __init__(self):
        super().__init__()
        self.q_dict = {}
        self.last_move = None
        self.last_board = None
        self.game_turn_count = 0

    def q_action(self):
        self.last_board = self.board_copy()
        can_put_list = self.can_put_list(BLACK)
        if random.random() < 0.5:
            i = random.randrange(len(can_put_list))
            rand_x, rand_y = can_put_list[i]
            return rand_x, rand_y
        list_q = [self.get_key(tuple(self.last_board), act)for act in can_put_list]
        maxQ = max(list_q)  #　最大値を検索
        if list_q.count(maxQ) > 1:  # 最大値と一致する値の数を求めて比較
            good_choice = [i for i in range(len(can_put_list)) if list_q[i] == maxQ]
            select_a = random.choice(good_choice)
        else:
            select_a = list_q.index(maxQ)
        self.last_move = can_put_list[select_a]
        q_x, q_y = can_put_list[select_a]
        return q_x, q_y

    def get_key(self, last_board, act):
        if self.q_dict.get((last_board, act)) is None:
            self.q_dict[(last_board, act)] = 1
        return self.q_dict.get((last_board, act))

    def result(self):
        if self.last_move is not None:
            if self.winner == b_WIN:
                self.cal_q(self.last_board, self.last_move, 10)
            elif self.last_move == DRAW:
                self.cal_q(self.last_board, self.last_move, 0)
            elif self.winner == b_LOSE:
                self.cal_q(self.last_board, self.last_move, -10)
            self.last_move = None
            self.last_board = None

    def cal_q(self, last_board, last_move, QV):
        Q_key = self.get_key(last_board, last_move)
        if self.winner is not None:
            maxQnew = 0
        else:
            i = self.can_put_list(BLACK)
            maxQnew = max([self.get_key(tuple(self.board), act) for act in i])
        self.q_dict[(last_board, last_move)] = Q_key + 0.3 * ((QV + 0.9 * maxQnew) - Q_key)



    def random_action(self, turn):
        act = self.can_put_list(turn)
        act_x, act_y = random.choice(act)
        print(act)
        print(act_x, act_y)
        return act_x, act_y

    def human_player(self, player):
        can_put_list = self.can_put_list(player)
        print('リストから選択！')
        print(str(can_put_list)+':')
        list_number = int(input())
        x, y = can_put_list[list_number]
        return x, y












