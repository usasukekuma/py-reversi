from board import *
from ch_play import *
from basic_player import *
import time
ERROR_count = 0
B_error_count = 0
W_error_count = 0
j_1 = 0


class game_master(Board):
    def put_stone(self, x, y, player):  # 石を置くメソッド
        # すでに石があればおけない(Noneでないところ＝石がある）
        if self.board[y][x] is not EMP:  # Noneの比較は＝ではなくisをつかう。リストy行目のｘ列目だから
            return False  # Falseでおけないよ！ってする
        # ひっくり返せないときはおけない
        turn_over = self.turn_over_list(x, y, player)
        if turn_over == [] :  # リストがからのとき＝ひっくり返す石がない
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
                if ax == 0 and ay == 0:  # 0*0はない
                    continue  # 次のループへ
                turn_over_tmp = []
                count = 0
                while(True):
                        count += 1  # 現在地からずらす
                        # check_?で調べる石の座標
                        check_x = x + (ax * count)  # 現在地からｘ軸方向に１ずつ＋ー移動
                        check_y = y + (ay * count)  # 現在地からy軸方向に１ずつ＋ー移動
                        # check座標がBOARD_SIZEの範囲内か
                        if 0 <= check_x < BOARD_SIZE and 0 <= check_y < BOARD_SIZE:
                            put = self.board[check_y][check_x]
                            # 石がないときその方向はそこで終了
                            if put == EMP:
                                break
                            if not put == player and not put == EMP:  # 自分の石があったとき。
                                turn_over_tmp.append((check_x, check_y))
                            # 相手の石があればひっくりかえせるリストに追加位
                            elif put == player:
                                if not turn_over_tmp == []:
                                    turn_over.extend(turn_over_tmp)
                                elif turn_over_tmp == []:
                                    break
                        else:
                            break
        return turn_over  # turn_overがこの関数の戻り値

    def can_put_list(self, player):  # おける場所リスト
        can_put = []
        for bx in range(BOARD_SIZE):
            for by in range(BOARD_SIZE):
                if self.board[by][bx] is not EMP:
                    continue
                elif self.turn_over_list(bx, by, player) == []:
                    continue
                else:
                    can_put.append((bx, by))
        return can_put

    def player_check(self, i):
        if i % 2 == 0:
            return BLACK
        else:
            return WHITE

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
            return self.winner


def player_type(t_player):
    if t_player == 1:
        tp = ch_player
        pp = 'deepくん'
    elif t_player == 2:
        tp = random_action
        pp = 'ランダムくん'
    elif t_player == 3:
        tp = human_player
        pp = 'ふなっしー'
    else:
        sys.exit()
    return tp, pp


if __name__ == "__main__":
    print('オセロゲームなっし')
    B_winner_count = 0
    W_winner_count = 0
    D_winner_count = 0
    print('黒プレーヤーを選択なっし\ndeepくん→1\nランダムくん→2\n人→3')
    t_player_b = int(input())
    player_1, p_b = player_type(t_player_b)
    print('白プレーヤーを選択なっし\ndeepくん→1\nランダムくん→2\n人→3')
    t_player_w = int(input())
    player_2, p_w = player_type(t_player_w)
    if p_b == 'deepくん':
        print('input black model path model/')
        black_npz_path = input()
        j_1 += 1
    if p_w == 'deepくん':
        print('input white model path model/')
        white_npz_path = input()
        j_1 += 1
    print('試合数を選ぶなっし(0以外を入力してくださいなっし)')
    battle_time = int(input())
    print(str(p_b)+'VS'+str(p_w)+'の'+str(battle_time)+'回の試合を開始するなっしー！')

    #  ゲーム開始
    time_s = time.perf_counter()
    for n in range(0, battle_time):
        othello = game_master()
        othello.view()
        i = 0
        nyu = 0
        while not k == 100:
            turn = othello.player_check(i)
            #  黒のターン
            if turn == BLACK:
                current_board = [othello.board_copy()]
                print('黒の番です')
                can_put_list = othello.can_put_list(BLACK)
                if not can_put_list == []:
                    x, y, j = player_1(can_put_list, current_board, black_npz_path)
                    if j == 1:
                        B_error_count += 1
                else:
                    i += 1
                    nya = 65
                    continue
            #  白のターン
            elif turn == WHITE:
                current_board = [othello.board_copy()]
                print('白の番です')
                can_put_list = othello.can_put_list(WHITE)
                if not can_put_list == []:
                    x, y, j = player_2(can_put_list, current_board, white_npz_path)
                    if j == 1:
                        W_error_count += 1
                else:
                    i += 1
                    nya = 65
                    continue
            othello.put_stone(x, y, turn)
            othello.view()
            i += 1
        k = 0
        if othello.can_put_list(BLACK) == []:
            k += 50
        if othello.can_put_list(WHITE) == []:
            k += 50
        tmp_w = othello.end()
        if tmp_w == b_LOSE:
            W_winner_count += 1
        elif tmp_w == b_WIN:
            B_winner_count += 1
        elif tmp_w ==DRAW:
            D_winner_count += 1
    time_e = time.perf_counter()

    print(str(battle_time)+'回の試合が終了しました。\nresult・・・')
    print('黒'+str(B_winner_count)+'回'+'白'+str(W_winner_count)+'回、勝ちました.'+'引き分けは'+str(D_winner_count)+'回です')
    print('勝率は,黒：'+str((B_winner_count/battle_time)*100)+'%\n白：'+str((W_winner_count/battle_time)*100)+'%\n''引き分け：'
          +str((D_winner_count/battle_time)*100)+'%です。')
    if not j_1 == 0:
    print(str(battle_time)+'回の実行時間は'+str(time_e-time_s)+'秒です')



