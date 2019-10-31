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
N3 = N3()# ネットをつくるお
model5 = L.Classifier(N5)
model3 = L.Classifier(N3)


# classfierのデフォ損失関数はF.softmax_cross_entropy

#　　モデルを読み込んで実際に手を打つ
def load_ch5(current_board,npz_path):
    serializers.load_npz(npz_path, model5)
    X1 = np.array(current_board, dtype=np.float32)
    y1 = F.softmax(model5.predictor(X1))
    tm1 = y1.data.argsort()
    putting_list = [x1 for a1 in tm1 for x1 in a1]
    return putting_list

def load_ch3(current_board,npz_path):
    serializers.load_npz(npz_path, model3)
    X1 = np.array(current_board, dtype=np.float32)
    y1 = F.softmax(model3.predictor(X1))
    tm1 = y1.data.argsort()
    putting_list = [x1 for a1 in tm1 for x1 in a1]
    return putting_list

def single_ch(can_put_list, current_board, npz_path):
    putting_list = load_ch5(current_board,npz_path)
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
            ppf = (int(put_perf[eval_index]))
            eval_list.append(ppf)
        txy = can_put_list[eval_list.index(max(eval_list))]
        x, y = txy
        return x, y



def ch_winner(can_put_list, current_board):
    eval_list_w = []
    put_perf = []
    put_pers = []
    put_pert = []
    f_putting_list = load_ch5(current_board, npz_path='model/SGD/10sb_2957brwr_1000e_5n.npz')
    s_putting_list = load_ch3(current_board, npz_path='model/SGD/20sb_1462brwr_1000e_3n.npz')
    t_putting_list = load_ch5(current_board, npz_path='model/SGD/4458b_brwr_1000e_5n.npz')
    len_can_put_list = len(can_put_list)

    for xy in can_put_list:
        x, y = xy
        z = x + y * 8
        put_perf.append(f_putting_list.index(z))  #それぞれのモデルで予測した置ける場所に対する順位（評価値）
        put_pers.append(s_putting_list.index(z))  #putting_listは低→高順なので　index番号が大きほど勝てそうと予測したということ
        put_pert.append(t_putting_list.index(z))  #なのでインデックス番号を取得して、can_put_listのインデックス番号と対応するように保存

    for eval_index in range(0, len_can_put_list):
        ppf = (put_perf[eval_index]) * 1  # 格納された順位（評価値を取得）
        pps = (put_pers[eval_index]) * 1  #can_put_listのインデックス番号と対応するので[0]で抜き出したものは
        ppt = (put_pert[eval_index]) * 1  #can_put_list[0]に格納された座標の評価値
        eval_put = ppf + pps + ppt
        eval_list_w.append(eval_put)
    return eval_list_w



def ch_loser(can_put_list, current_board):
    eval_list_l = []
    put_perl = []
    eval_list_w = ch_winner(can_put_list,current_board)
    l_putting_list = load_ch5(current_board, npz_path='model/SGD/kihu203b_10batch_1000e_5n.npz')

    for xy in can_put_list:
        x, y = xy
        z = x + y * 8
        put_perl.append(l_putting_list.index(z))

    for eval_idx in range(0,len(eval_list_w)):
        w_p = eval_list_w[eval_idx]
        ppl = (put_perl[eval_idx]) * 1
        if ppl == 0:
            ppl = 0
        else:
            ppl = -ppl
        print(ppl)
        print(w_p)
        eval_put_l = w_p + ppl
        print(eval_put_l)
        eval_list_l.append(eval_put_l)
    return eval_list_l
def ch_multi_plyaer(can_put_list, current_board, npz_path):
    eval_list = []
    if npz_path == 'LOSER':
        eval_list = ch_loser(can_put_list,current_board)
    else:
        eval_list = ch_winner(can_put_list,current_board)
    print(eval_list)
    print(can_put_list)
    txy = can_put_list[eval_list.index(max(eval_list))]
    x, y = txy
    return x, y