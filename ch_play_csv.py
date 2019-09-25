import chainer
import chainer.links as L
import chainer.function as F
import numpy as np
from chainer import Chain


class MLP(chainer, Chain):
    def __init__(self):
        super(MLP, self).__init__(
            l1=L.Linear(64, 100),
            l2=L.Linear(100, 100),
            l3=L.Linear(100, 65)
        )

    def __call__(self, x):
        h1 = F.relu(self.l1(x))
        h2 = F.relu(self.l2(h1))
        y = self.l3(h2)
        return y
