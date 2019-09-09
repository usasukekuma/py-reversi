import random
from game_master import *

class q_learning(game_master):
    def __init__(self):
        super().__init__()
        self.q_dict = {}
        self.e = 0.2
        self.alpha = 0.3
        self.gamma = 0.9
        self.last_move = None
        self.last_board = None
        self.game_turn_count = 0

    def q_action(self, player):
        self.last_board = self.board_copy()
        can_put_list = self.can_put_list(player)
        if random.random() < (1/(50+self.game_turn_count)):
            i = random.randrange(len(can_put_list))
            rand_x, rand_y = can_put_list[i]
            return rand_x, rand_y

        list_q = [self.cal_qvalue(tuple(self.last_board), act) for act in can_put_list]
        maxQ = max(list_q)  # Q値の最大値を検索
        if list_q.count(maxQ) > 1:  # 最大値が複数あるならば
            action = [i for i in range(len(can_put_list)) if list_q[i] == maxQ]  # actionに最大値を保存し、らんだむにえらぶ
            i = random.choice(action)
        else:
            i = list_q(maxQ)
        self.last_move = can_put_list[i]
        return can_put_list[i]

    def cal_qvalue(self, state, act):  # winのとき呼び出してリストになかったら1をに
        if self.q_dict.get(state, act) is None:
            self.q_dict[(state, act)] = 1
        return self.q_dict.get((state, act))

    def game_result(self):
        if self.winner == b_WIN:
            self.learn(self.last_board, self.last_move, 1)
        elif self.winner == b_LOSE:
            self.learn(self.last_board, self.last_move, 0)
        else:
            self.learn(self.last_board, self.last_move, -1)
        self.game_turn_count += 1
        self.last_move = None
        self.last_board = None

    def learn(self, last_board, last_move, r):
        qnew = self.cal_qvalue(tuple(last_board), last_move)
        if self.winner == b_LOSE:
            maxQnew = 0
        else:
            maxQnew = max([(self.cal_qvalue(tuple(self.board)), act)for act in self.can_put_list(BLACK)])
        self.q_dict[(tuple(last_board), last_move)] = qnew+self.alpha*((r*self.gamma*maxQnew)-qnew)

    def random_action(self, turn):
        act = self.can_put_list(turn)
        act_x, act_y = random.choice(act)
        print(act)
        print(act_x, act_y)
        return act_x, act_y


