import chainer
import chainer.links as L
import chainer.function as F
import numpy as np
from chainer import Chain


n_input = 64
n_hidden = 100
n_output = 65

class MLP(chainer, Chain):
    def __init__(self):
        super().__init__()
        with self.init_scope():
            self.l1 = L.Linear(n_input, n_hidden)
            self.l2 = L.Linear(n_hidden, n_hidden)
            self.l3 = L.Linear(n_hidden, n_output)

    def __call__(self, x):
        h1 = F.relu(self.l1(x))
        h2 = F.relu(self.l2(h1))
        y = F.relu(self.l3(h2))
        return y



