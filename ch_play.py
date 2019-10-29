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
class N(chainer.Chain):

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


N = N()  # ネットをつくるお
model = L.Classifier(N)  # classfierのデフォ損失関数はF.softmax_cross_entropy
#　　モデルを読み込んで実際に手を打つ

def ch_player(can_put_list, current_board, npz_path):
    serializers.load_npz(npz_path,model)
    X1 = np.array(current_board, dtype=np.float32)
    y1 = F.softmax(model.predictor(X1))
    tm1 = y1.data.argsort()
    putting_list = [x1 for a1 in tm1 for x1 in a1]
    eval_list = []
    put_perf = []
    len_can_put_list = len(can_put_list)
    if len_can_put_list == 1:
        x, y = can_put_list[0]
        return x, y
    else:
        for xy in can_put_list:
            x, y = xy
            z = x + y * 8
            put_perf.append(putting_list.index(z))

        for eval_index in range(0, len_can_put_list):
            ppf = (int(put_perf[eval_index]))*1.2
            eval_list.append(ppf)
        txy = can_put_list[eval_list.index(max(eval_list))]
        x, y = txy
        return x, y
