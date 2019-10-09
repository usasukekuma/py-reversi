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



class Revchain(Chain):
    def __init__(self):
        super(Revchain, self).__init__(
            l1=L.Linear(64,100),
            l2=L.Linear(100,100),
            l3=L.Linear(100,65)
        )
    def __call__(self, x):
        h1 = F.relu(self.l1(x))
        h2 = F.relu(self.l2(h1))
        y = self.l3(h2)
        return y

class Classfilter(Chain):
    def __init__(self, predictor):
        super(Classfilter, self).__init__(predictor=predictor)

    def __call__(self, x, t):
        y = self.predictor(x)
        loss = F.softmax_cross_entropy(y, t)
        accuracy = F.accuracy(y, t)
        report({'loss':loss, 'accuracy':accuracy},self)
        return loss
def conv(put_st):
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


model = Classfilter(Revchain())


def ch_player(can_put_list,current_board,npz_path):
    serializers.load_npz(npz_path, model)
    X1 = np.array(current_board, dtype=np.float32)
    y1 = F.softmax(model.predictor(X1))
    tm = y1.data.argsort()[:, ::-1]
    putting_list = [x for a in tm for x in a]
    s_count = 0
    for put_st in putting_list:
        put_st = int(put_st)
    #  出力がパスのとき
        if put_st == 64:
            #  本当にパスならばプレイヤーが呼び出される前にスキップされるはず
            if can_put_list == []:
                print('ERROR')
                sys.exit()
            #  予測はパスだけど、打てる手がある場合（予測は完璧じゃない）
            else:
                s_count += 1
                continue
        #  予測でパスじゃないなら手が本当に打てるてか？
        elif len(can_put_list) == 1:
            x, y = can_put_list[0]
            return x, y, s_count
        else:
            t_x, t_y = conv(put_st)  # 0~63を座標に変換
            print('(' + str(t_x) + ',' + str(t_y) + ')' + 'でチェック')
            if not list(set([(t_x, t_y)]) & set(can_put_list)) == []:
                #  予測の結果が、打てる手リストに存在するならそのまま
                return t_x, t_y, s_count,
            # 手は出力されたが、おける場所ではなかった場合
            else:
                s_count += 1
                continue
