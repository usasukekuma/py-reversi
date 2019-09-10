import sys
import numpy as np
import chainer
from chainer import cuda, Function, gradient_check, report, training, utils, Variable
from chainer import datasets, iterators, optimizers, serializers
from chainer import Link, Chain, ChainList
import chainer.functions as F
import chainer.links as L
from chainer.training import extensions
from random_player import *


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

model = Classfilter(Revchain())
othello = random_player()
othello.view()
turn = BLACK
X1_ = [othello.board_copy()]
serializers.load_npz('othello_model.npz', model)
X1 = np.array(X1_, dtype=np.float32)
y1 = F.softmax(model.predictor(X1))
print("BLACK"+str(y1.data.argmax(1)))

