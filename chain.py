import sys
import random
import chainer
import chainer.links as L
import chainer.function as F
import numpy as np
from chainer import Chain, Link, ChainList,datasets, iterators,cuda
from chainer import Function, report, training, utils, Variable, optimizers, serializers
from chainer.training import extensions
from read_file import *


n_input = 64
n_hidden = 100
n_output = 65

gpu_id = 0

class Reversi(Chain):
    def __init__(self):
        super().__init__()
        with self.init_scope():
            self.l1 = L.Linear(n_input, n_hidden)
            self.l2 = L.Linear(n_hidden, n_hidden)
            self.l3 = L.Linear(n_hidden, n_output)

    def __call__(self, x):
        h1 = F.relu(self.l1(x))
        h2 = F.relu(self.l2(h1))
        y = self.l3(h2)
        return y

class Classfier(Chain):
    def __init__(self, predictor):
        super(Classfier, self).__init__(predictor=predictor)

    def __call__(self, x, t):
        y = self.predictor(x)
        loss = F.softmax_cross_entropy(y, t)
        accuracy = F.accuracy(y, t)
        report({'loss':loss, 'accuracy':accuracy},self)
        return loss


X = np.array(input_board, dtype=np.float32)
y = np.array(output_stone, dtype=np.int32)

train = datasets.TupleDataset(X, y)  # 学習用データを作る datasetsは学習用データを作ってくれる tupleで形を決めている
train_iter = iterators.SerialIterator(train, batch_size=100)  # iteratoorsは学習データをシャッフルしたりすてくれる
# バッチサイズはデータを分けるサイズを指定する　１００ずつ
model = Classfilter(Reversi())
optimizer = optimizers.SGD()  # SGD法を選択
optimizer.setup(model)

updater = training.StandardUpdater(train_iter, optimizer)
trainer = training.Trainer(updater, (1000, 'epoch'), out='results')

trainer.extend(extensions.ProgressBar())
trainer.run()
serializers.save_npz(saving_name, model)