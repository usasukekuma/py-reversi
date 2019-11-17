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
# player_numは、ch_winnerの用いるモデル数
player_num = 2
loser_num = 2
# f_mul~loser_mulは、それぞれのモデルが出力した評価値の対する重み付け
f_mul = 1.2
s_mul = 1.1
t_mul = 1
loser_mul_1 = 1.5
loser_mul_2 = 1
# モデルのパス
f_npz_path = 'model/SGD/30sb_30000brwr_1000e_5n.npz'
s_npz_path = 'model/SGD/20sb_11042brwr_1000e_5n.npz'
# player_num=2のときはt_npz_pathは読み込まれないbut空にはできないので。1とかいれておく
t_npz_path = 'loser'

loser_path = 'model/SGD/loser_30sb_10000brwr_1000e_5n.npz'
loser_path2 = 'model/SGD/loser_30000brwr_1000e_5n.npz'

switch_first_half = 'model/SGD/20sb_11042brwr_1000e_5n.npz'
switch_second_half = 'LOSER'
# ↑LOSERにすると負けモデルのマイナス評価を取り入れたswitchができる＊switch_modelのelse以下をch_multi_playerにしておく
# chainerのモデルで戦う　Class N は学習時と同じ構造にする必要があるのでN３とN5両方用意してある
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


def conv(put_st):  # ０～６４の出力を座標に変換
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
N3 = N3()  # ネットをつくるお
model5 = L.Classifier(N5)
model3 = L.Classifier(N3)
# classfierのデフォ損失関数はF.softmax_cross_entropy


def load_predict(current_board, npz_path):
    # モデルのファイル名にふくまれる文字で学習時のネット構造を判別している
    if '5n' in str(npz_path):
        model = model5
    elif '3n' in str(npz_path):
        model = model3
    serializers.load_npz(npz_path, model)
    X1 = np.array(current_board, dtype=np.float32)
    y1 = F.softmax(model.predictor(X1))
    tm1 = y1.data.argsort()
    putting_list = [x1 for a1 in tm1 for x1 in a1]  # １次元配列に変換
    return putting_list


def single_ch(can_put_list, current_board, npz_path):
    putting_list = load_predict(current_board, npz_path)
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
    f_putting_list = load_predict(current_board, npz_path=f_npz_path)
    s_putting_list = load_predict(current_board, npz_path=s_npz_path)
    if player_num == 3:
        t_putting_list = load_predict(current_board, npz_path=t_npz_path)
    len_can_put_list = len(can_put_list)

    for xy in can_put_list:
        x, y = xy
        z = x + y * 8
        put_perf.append(f_putting_list.index(z))  # それぞれのモデルで予測した置ける場所に対する順位（評価値）
        put_pers.append(s_putting_list.index(z))  # putting_listは低→高順なので　index番号が大きほど勝てそうと予測したということ
        if player_num == 3:
            put_pert.append(t_putting_list.index(z))  # なのでインデックス番号を取得して、can_put_listのインデックス番号と対応するように保存

    for eval_index in range(0, len_can_put_list):
        ppf = (put_perf[eval_index]) * f_mul  # 格納された順位（評価値を取得）
        pps = (put_pers[eval_index]) * s_mul
        eval_put = ppf + pps
        if player_num == 3:
            ppt = (put_pert[eval_index]) * t_mul  # can_put_list[0]に格納された座標の評価値
            eval_put += ppt
        eval_list_w.append(eval_put)
    return eval_list_w


def ch_loser(can_put_list, current_board):
    eval_list_l = []
    put_perl = []
    put_perl2 = []

    eval_list_w = ch_winner(can_put_list, current_board)
    l_putting_list = load_predict(current_board, npz_path=loser_path)
    if loser_num == 2:
        l_putting_list_2 = load_predict(current_board, npz_path=loser_path2)

    for xy in can_put_list:
        x, y = xy
        z = x + y * 8
        put_perl.append(l_putting_list.index(z))
        if loser_num == 2:
            put_perl2.append(l_putting_list_2.index(z))

    for eval_idx in range(0, len(eval_list_w)):
        w_p = eval_list_w[eval_idx]
        ppl = (put_perl[eval_idx]) * (-loser_mul_1)
        if loser_num == 2:
            ppl2 = (put_perl2[eval_idx]) * (-loser_mul_2)
            eval_put_l = w_p + ppl +ppl2
        else:
            eval_put_l = w_p + ppl
        eval_list_l.append(eval_put_l)
    return eval_list_l


def ch_multi_player(can_put_list, current_board, npz_path):
    eval_list = []
    if len(can_put_list) == 1:
        x, y = can_put_list[0]
        return x, y
    else:
        if npz_path == 'LOSER':
            eval_list = ch_loser(can_put_list, current_board)
        else:
            eval_list = ch_winner(can_put_list, current_board)
    txy = can_put_list[eval_list.index(max(eval_list))]
    x, y = txy
    return x, y


def switch_model(can_put_list, current_board, npz_path):
    tmp1 = [b for a in current_board for b in a]
    tmp_2 = [d for c in tmp1 for d in c]
    if len(can_put_list) == 1:
        x, y = can_put_list[0]
    elif tmp_2.count(0) <= 10:
        x, y = single_ch(can_put_list, current_board, npz_path=switch_first_half)
    else:
        x, y = ch_multi_player(can_put_list, current_board, npz_path=switch_second_half)
    return x, y


def mini_check(can_put_list, eval_list):
    mini_corner = [(0, 0), (7, 0), (0, 7), (7, 7)]
    mini_side = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
                 (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7),
                 (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
                 (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6)
                 ]
    mini_cor2 = [(1, 1), (6, 1),  (1, 6), (6, 6)]
    mini_side2 = [(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (3, 1), (4, 1), (5, 1),
                  (6, 2), (6, 3), (6, 4), (6, 5), (2, 6), (3, 6), (4, 6), (5, 6)]

    for idc in mini_corner:
        if idc in can_put_list:
            ind1 = eval_list[can_put_list.index(idc)]
            eval_list[can_put_list.index(idc)] = ind1 + 30
    for ids in mini_side:
        if ids in can_put_list:
            ind2 = eval_list[can_put_list.index(ids)]
            eval_list[can_put_list.index(ids)] = ind2 + 15

    for idc2 in mini_cor2:
        if idc2 in can_put_list:
            ind3 = eval_list[can_put_list.index(idc2)]
            eval_list[can_put_list.index(idc2)] = ind3 - 30
    for ids2 in mini_side2:
        if ids2 in can_put_list:
            ind4 = eval_list[can_put_list.index(ids2)]
            eval_list[can_put_list.index(ids2)] = ind4 - 15

    return eval_list


def ch_mini(can_put_list, current_board, npz_path):
    tmp1 = [b for a in current_board for b in a]
    tmp_2 = [d for c in tmp1 for d in c]
    if len(can_put_list) == 1:
        x, y = can_put_list[0]
    else:
        if npz_path == 'LOSER':
            eval_list = ch_loser(can_put_list, current_board)
        else:
            eval_list = ch_winner(can_put_list, current_board)
        eval_list = mini_check(can_put_list, eval_list)
        txy = can_put_list[eval_list.index(max(eval_list))]
        x, y = txy
    return x, y







