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


class N(chainer.Chain):

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

b = [[[0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,1,2,0,0,0],
     [0,0,0,2,1,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0]]]

can_put_list = [(2, 3), (3, 2), (4, 5), (5, 4)]

N = N()  # ネットをつくるお
model = L.Classifier(N)  # classfierのデフォ損失関数はF.softmax_cross_entropy
npz_path = 'model/sgd/old/10000black_brwr.npz'
put_list = []
serializers.load_npz(npz_path, model)
X1 = np.array(b, dtype=np.float32)
y1 = F.softmax(model.predictor(X1))
tm = y1.data.argsort()[:, ::-1]  # 大きい順に並び替える
putting_list = [x for a in tm for x in a]
putting_list.remove(64)
for tmp7 in putting_list:
    print(tmp7)
    t_x, t_y = conv(tmp7)
    put_list.append((t_x, t_y))
print(put_list)
l2 = len(put_list)
for tmp8 in range(0,l2):
