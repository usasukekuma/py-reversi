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


for_convert = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
               (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),
               (0,2),(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),
               (0,3),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(7,3),
               (0,4),(1,4),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4),
               (0,5),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(7,5),
               (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6),
               (0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7)]

B_winner_count = 0
W_winner_count = 0
loop_time = 100
# ゲーム開始
for n in range(0,loop_time):
    othello = random_player()
    othello.view()
    turn = BLACK
    i = 0
    while not othello.can_put_list(BLACK) == [] and not othello.can_put_list(WHITE) == []:
        turn = othello.player_check(i)
        #  chain_player
        if turn == BLACK:
            cu_board = [othello.board_copy()]
            hand = '黒の'
            othello.player_print(hand)
            okerundesu = othello.can_put_list(BLACK)
            print(okerundesu)
            print('思考中')
            serializers.load_npz('othello_model.npz', model)
            X1 = np.array(cu_board, dtype=np.float32)
            y1 = F.softmax(model.predictor(X1))
            #  ↑学習モデルをもとに手を算出
            put_B = int((y1.data.argmax(1)))
            print("BLACK=" + str(put_B))
            #  パスが出力されたら？本当にパス？
            if put_B == 64:  # 出力６４はパス
                if okerundesu == []:
                    #  そもそもplayer_checkで弾かれるはず
                    print('ERROR')
                    sys.exit()
                else:
                    print('ランダムに選択されました')
                    othello.random_action(BLACK)
            #  パスじゃないなら手が本当に打てるてか？
            else:
                t_x, t_y = for_convert[put_B]
                print('('+str(t_x)+','+str(t_y)+')'+'でチェック')
                if not list(set([(t_x, t_y)]) & set(okerundesu)) == []:
                    x, y = t_x, t_y
                #  pass動作
                else:
                    if okerundesu == []:
                        print('ERROR')
                        sys.exit()
                    else:
                        print('ランダムに選択されました')
                        x, y = othello.random_action(BLACK)
        #  random
        else:
            hand = '白の'
            othello.player_print(hand)
            t_x, t_y = othello.random_action(WHITE)
            if not list(set([(t_x, t_y)]) & set(othello.can_put_list(WHITE))) == []:
                x, y = t_x, t_y
            else:
                print('ERROR')
                sys.exit()
        othello.put_stone(x, y, turn)
        othello.view()
        i += 1
    tmp_w = othello.end()
    if tmp_w == b_LOSE:
        W_winner_count += 1
    elif tmp_w == b_WIN:
        B_winner_count += 1
        continue
print('黒'+str(B_winner_count)+'、白'+str(W_winner_count)+'\n黒の勝率は'+str((B_winner_count/loop_time)*100)+'%です')


