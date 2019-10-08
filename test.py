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

'''
class Reversi(Chain):
    def __init__(self):
        super().__init__()
        with self.init_scope():
            self.l1 = L.Linear(64, 100)
            self.l2 = L.Linear(100, 100)
            self.l3 = L.Linear(100, 65)

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



model = Classfilter(Reversi())

b = [[[0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,1,2,0,0,0],
     [0,0,0,2,1,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0]]]
model = Classfilter(Reversi())

serializers.load_npz('model/10000black_brwr.npz', model)
X1 = np.array(b, dtype=np.float32)
y1 = F.softmax(model.predictor(X1))
print(type(y1))
s = y1.data.argsort(1)
print(s)
put_st = int((y1.data.argmax(1)))
print(put_st)
'''
lista=[1,2,3,4,5,6,7,8,9]
for i in range(-1, -64,-1):
    print(lista[i])