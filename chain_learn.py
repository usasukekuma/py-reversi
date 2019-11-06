from make_read import *
from chainer.datasets import TupleDataset, split_dataset_random
from chainer.iterators import SerialIterator
import chainer
from chainer import iterators,optimizers,training
import chainer.links as L
import chainer.functions as F
import subprocess

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


# ------データ作成---------
x = np.array(input_board, 'float32')
t = np.array(output_stone, 'int32')
# read_fileと一連託生
dataset = TupleDataset(x, t)
ss = len(dataset)
split_at = int(ss*0.8)
train, test = split_dataset_random(dataset, split_at, seed=0)
#  すべての試合の８割を訓練と検証に、、
train_iter = SerialIterator(train, batch_size=100, repeat=True, shuffle=True)
#  訓練データを100個＝１セットに　シャッフルもするお！
valid_iter = iterators.SerialIterator(test, batch_size=100, shuffle=False, repeat=False)
#  ------end------


N = N()  # ネットをつくるお
model = L.Classifier(N)  # classfierのデフォ損失関数はF.softmax_cross_entropy
optimizer = optimizers.SGD(lr=0.1)  # 勾配関数
optimizer.setup(model)
updater = training.StandardUpdater(train_iter, optimizer)
#  updater イテレータ・オプティマイザを統括し、順伝播・損失・逆伝播の計算、そしてパラメータの更新（オプティマイザの呼び出し）という、
#  訓練ループ内の定型的な処理を実行します。 by tutorial
trainer = training.Trainer(updater, (1000, 'epoch'), out='results/'+result_out)
#  trainer アップデータを受け取り、訓練全体の管理を行います。イテレータを用いてミニバッチを繰り返し作成し、オプティマイザを使ってネットワークのパラメータを更新します。
#  訓練の終了タイミングの決定や、設定されたエクステンションの呼び出しも担います

trainer.extend(extensions.ProgressBar())
trainer.extend(extensions.Evaluator(valid_iter, model, device=gpu_id))
trainer.extend(extensions.LogReport(trigger=(50, 'epoch'), log_name='log'))

'''
trainer.extend(extensions.Evaluator(test, model, -1))
trainer.extend(extensions.PrintReport(
    ['epoch', 'main/loss', 'main/accuracy', 'validation/main/loss', 'validation/main/accuracy', 'elapsed_time']))

trainer.extend(extensions.PlotReport(['fc1/W/grad/mean'], x_key='epoch', file_name='mean.png'))
trainer.extend(extensions.PlotReport(['main/loss', 'val/main/loss'], x_key='epoch', file_name='loss.png'))
trainer.extend(
    extensions.PlotReport(['main/accuracy', 'validation/main/accuracy'], x_key='epoch', file_name='accuracy.png'))
'''
print(saving_name)
trainer.run()
print('学習は終わった。保存する')
serializers.save_npz(saving_name, model)
print('モデルを'+saving_name+'で保存しました')
if shut == 'Y' or shut == 'yes' or shut == 'y':
    cmd = 'shutdown -s -f -t 0'
    subprocess.run(cmd, shell=True)