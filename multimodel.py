import sys
import numpy as np
import random
import chainer
from chainer import cuda, Function, gradient_check, report, training, utils, Variable
from chainer import datasets, iterators, optimizers, serializers
from chainer import Link, Chain, ChainList
import chainer.functions as F
import chainer.links as L
from chainer.training import extensions

n_in = 64
n_hidden = 100
n_out = 65
gpu_id = -1



# chainerのモデルで戦う　Class N は学習時と同じ構造にする
class N5(chainer.Chain):

    def __init__(self):
        super().__init__()
        with self.init_scope():
            self.l1 = L.Linear(n_in, n_hidden)
            self.l2 = L.Linear(n_hidden, n_hidden)
            self.l3 = L.Linear(n_hidden, n_hidden)
            self.l4 = L.Linear(n_hidden, n_out)

    def __call__(self, x):
        h = F.relu(self.l1(x))
        h = F.relu(self.l2(h))
        h = F.relu(self.l3(h))
        h = self.l4(h)
        return h

class N3(chainer.Chain):

    def __init__(self):
        super().__init__()
        with self.init_scope():
            self.l1 = L.Linear(n_in, n_hidden)
            self.l2 = L.Linear(n_hidden, n_hidden)
            self.l3 = L.Linear(n_hidden, n_out)

    def __call__(self, x):
        h = F.relu(self.l1(x))
        h = F.relu(self.l2(h))
        h = self.l3(h)
        return h


def conv(put_st):  #　０～６４の出力を座標に変換
    for_convert = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1),
                   (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2),
                   (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3),
                   (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4),
                   (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6),
                   (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)]
    t_x, t_y = for_convert[put_st]
    return t_x, t_y


N5 = N5()
N3 = N3()
# ネットをつくるお
model1 = L.Classifier(N5)  # classfierのデフォ損失関数はF.softmax_cross_entropy
model2 = L.Classifier(N5)
model3 = L.Classifier(N5)
model4 = L.Classifier(N5)

def first_player(current_board):
    serializers.load_npz('model/Adam/20sb_100000brwr_1000e_5n.npz', model1)
    X1 = np.array(current_board, dtype=np.float32)
    y1 = F.softmax(model1.predictor(X1))
    tm1 = y1.data.argsort()
    putting_list = [x1 for a1 in tm1 for x1 in a1]
    return putting_list


def second_player(current_board):
    serializers.load_npz('model/SGD/100000b_brwr_1000e_5n.npz', model2)
    X2 = np.array(current_board, dtype=np.float32)
    y2 = F.softmax(model2.predictor(X2))
    tm2 = y2.data.argsort()
    putting_list = [x2 for a2 in tm2 for x2 in a2]
    return putting_list

def third_player(current_board):
    serializers.load_npz('model/SGD/10sb_100000brwr_1000e_5n.npz', model3)
    X3 = np.array(current_board, dtype=np.float32)
    y3 = F.softmax(model2.predictor(X3))
    tm3 = y3.data.argsort()
    putting_list = [x3 for a3 in tm3 for x3 in a3]
    return putting_list

def loser(current_board):
    serializers.load_npz('',model4)
    X4 = np.array(current_board, dtype=np.float32)
    y4 = F.softmax(model2.predictor(X4))
    tm3 = y4.data.argsort()
    putting_list = [x4 for a4 in tm3 for x4 in a4]
    return putting_list


def ch_multi(can_put_list, current_board, npz_path):
    f_putting_list = []
    s_putting_list = []
    t_putting_list = []
    eval_list = []
    put_perf = []
    put_pers = []
    put_pert = []
    f_putting_list = first_player(current_board)
    s_putting_list = second_player(current_board)
    t_putting_list = third_player(current_board)
    len_can_put_list = len(can_put_list)
    if len_can_put_list == 1:
        x, y = can_put_list[0]
        return x, y
    else:
        for xy in can_put_list:
            x, y = xy
            z = x + y * 8
            put_perf.append(f_putting_list.index(z))
            put_pers.append(s_putting_list.index(z))
            put_pert.append(t_putting_list.index(z))

        for eval_index in range(0, len_can_put_list):
            ppf = (int(put_perf[eval_index]))*1.2
            pps = (int(put_pers[eval_index]))*1.1
            ppt = (int(put_pert[eval_index]))*0.8
            eval_put = ppf+pps+ppt
            eval_list.append(eval_put)
        txy = can_put_list[eval_list.index(max(eval_list))]
        x, y = txy
        return x, y

def ch_loser(can_put_list, current_board, npz_path):
    f_putting_list = []
    s_putting_list = []
    t_putting_list = []
    eval_list = []
    put_perf = []
    put_pers = []
    put_pert = []
    f_putting_list = first_player(current_board)
    s_putting_list = second_player(current_board)
    t_putting_list = third_player(current_board)
    len_can_put_list = len(can_put_list)
    if len_can_put_list == 1:
        x, y = can_put_list[0]
        return x, y
    else:
        for xy in can_put_list:
            x, y = xy
            z = x + y * 8
            put_perf.append(f_putting_list.index(z))
            put_pers.append(s_putting_list.index(z))
            put_pert.append(t_putting_list.index(z))

        for eval_index in range(0, len_can_put_list):
            ppf = (int(put_perf[eval_index]))*1.2
            pps = (int(put_pers[eval_index]))*1.1
            ppt = (int(put_pert[eval_index]))*0.8
            eval_put = ppf+pps+ppt
            eval_list.append(eval_put)
        txy = can_put_list[eval_list.index(max(eval_list))]
        x, y = txy
        return x, y





