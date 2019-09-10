from board import *
import csv
import pandas as pd
import numpy as np
b_WIN = 100
b_LOSE = -100
DRAW = 50

class game_master(Board):
    def put_stone(self, x, y, player):  # 石を置くメソッド
        # すでに石があればおけない(Noneでないところ＝石がある）
        if self.board[y][x] is not EMP:  # Noneの比較は＝ではなくisをつかう。リストy行目のｘ列目だから
            return False  # Falseでおけないよ！ってする
        # ひっくり返せないときはおけない
        turn_over = self.turn_over_list(x, y, player)
        if not turn_over:  # リストがからのとき＝ひっくり返す石がない
            return False
        self.board[y][x] = player  # 置けるときにそのWorBを代入
        for x, y in turn_over:
            self.board[y][x] = player  # ひっくり返せる石をひっくり返す
        return True

    def turn_over_list(self, x, y, player):  # ひっくり返せる石のリスト
        vector = [-1, 0, 1]  # 石をおいた位置からベクトル方向
        turn_over = []
        for ay in vector:  # 行のベクトル方向を示す
            for ax in vector:  # 列のベクトル方向
                turn_over_tmp = []
                if ax == 0 and ay == 0:  # 0*0はない
                    continue  # 次のループへ
                count = 0
                while(True):
                        count += 1  # 現在地からずらす
                        # check_?で調べる石の座標
                        check_x = x + (ax * count)  # 現在地からｘ軸方向に１ずつ＋ー移動
                        check_y = y + (ay * count)  # 現在地からy軸方向に１ずつ＋ー移動
                        # check座標がBOARD_SIZEの範囲内か
                        if 0 <= check_x < BOARD_SIZE and 0 <= check_y < BOARD_SIZE:
                            put = self.board[check_y][check_x]
                            # 石がないとき、自分の石のときその方向はそこで終了
                            if put is EMP:
                                break
                            if put == player:  # 自分の石があったとき。
                                if turn_over_tmp is not []:
                                    turn_over.extend(turn_over_tmp)
                            # 相手の石があればひっくりかえせるリストに追加位
                            else:
                                turn_over_tmp.append((check_x, check_y))
                        else:
                            break
        return turn_over  # turn_overがこの関数の戻り値

    def can_put_list(self, player):  # おける場所リスト
        can_put = []
        for bx in range(BOARD_SIZE):
            for by in range(BOARD_SIZE):
                if self.board[by][bx] is not EMP:
                    continue
                if self.turn_over_list(bx, by, player) == []:
                    continue
                else:
                    can_put.append((bx, by))
        return can_put

    def player_check(self, i):
        if i % 2 == 0:
            turn = BLACK
        else:
            turn = WHITE
        if turn is BLACK:
            if self.can_put_list(turn) is []:
                return WHITE
            else:
                return BLACK
        else:
            if self.can_put_list(turn) is []:
                return BLACK
            else:
                return WHITE

    def player_print(self, hand):
        print(hand + '番です')

    def end(self):
            self.winner = None
            score_W = 0
            score_B = 0
            print('ゲーム終了\nスコアチェック中')
            for ay in range(8):  # 行のベクトル方向を示す
                for ax in range(8):  # 列のベクトル方向
                    check = self.board[ay][ax]
                    if check is WHITE:
                        score_W += 1
                    elif check is BLACK:
                        score_B += 1
            if score_B == score_W:
                judge = '引き分け'
                self.winner = DRAW
            elif score_W < score_B:
                judge = '黒の勝ち'
                self.winner = b_WIN
            else:
                judge = '白の勝ち'
                self.winner = b_LOSE
            print('黒{:d},白{:d}\n{}です。'.format(score_B, score_W, judge))

    def make_list(self, act_x):
        x, y = act_x
        if x == 0 and y == 0:
            c = 0
        elif act_x is None:
            c = 65
        else:
            c = x+(8*y)
        tmp = np.array(self.board_copy())
        current_board = tmp.flatten()
        self.game_list.append(current_board)
        self.game_list.append(c)

    def save_list(self, name):
        end_file = self.game_list
        with open(name+'.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(end_file)



if __name__ == "__main__":
    othello = game_master()
    othello.view()
    list0 = othello.turn_over_list(2,3,BLACK)
    list1 = othello.can_put_list(BLACK)
    print(list0,list1)