from board import *
from ch_play import *
from basic_player import *
import time
import numpy as np
import csv

B_winner_count = 0
W_winner_count = 0
D_winner_count = 0
B_error_count = 0
W_error_count = 0
bput_count = 0
wput_count = 0
b_skip_count = 0
w_skip_count = 0
pass_count = 0
b_sp = 0
b_ep = 0
w_sp = 0
w_ep = 0

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

    def make_report(self,repo, r_name):
        columns_1 = ['試合回数', '黒プレイヤー', '白プレイヤー', '黒が勝った回数',
                     '白が勝った回数', '引き分けの回数','黒の勝率', '白の勝率', '引き分け率',
                     '黒一回目の予想がエラーだった数/自ターン数','黒の予想に失敗したターン数/回ってきたターン数',
                     '白一回目の予想がエラーだった数/自ターン数','白の予想に失敗したターン数/回ってきたターン数']
        with open('report/'+r_name, 'w',encoding='shift_jis') as f:
            writer = csv.writer(f)
            writer.writerow(columns_1)
            writer.writerow(repo)

    def save_report(self, repo, r_name):
        with open('report/'+r_name, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(repo)


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
    print('レポートｃｓｖを作りますか？新規作成→ new or 追記 →　append　or 作らない→ no ')
    q = str(input())
    if not q == 'no':
        print('レポートファイル名を入力　report/が自動入力')
        r_name = str(input())
    print('黒プレーヤーを選択なっし\ndeepくん→1\nランダムくん→2\n人→3')
    t_player_b = int(input())
    player_1, p_b = player_type(t_player_b)
    print('白プレーヤーを選択なっし\ndeepくん→1\nランダムくん→2\n人→3')
    t_player_w = int(input())
    player_2, p_w = player_type(t_player_w)
    if p_b == 'deepくん':
        print('input black model path model/')
        black_npz_path = input()
        p_b = str(black_npz_path)
    elif not p_b == 'deepくん':
        black_npz_path = None
    if p_w == 'deepくん':
        print('input white model path model/')
        white_npz_path = input()
        p_w = str(white_npz_path)
    elif not p_w == 'deepくん':
        white_npz_path = None
    print('試合数を選ぶなっし(0以外を入力してくださいなっし)')
    battle_time = int(input())
    if battle_time == 0:
        print('ERROR')
        sys.exit()
    print(str(p_b)+'VS'+str(p_w)+'の'+str(battle_time)+'回の試合を開始するなっしー！')

    #  ゲーム開始
    time_s = time.perf_counter()
    for n in range(0, battle_time):
        othello = game_master()
        othello.view()
        i = 0
        k = 0
        while not k == 100:
            turn = othello.player_check(i)
            skip_count = 0
            #  黒のターン
            if turn == BLACK:
                current_board = [othello.board_copy()]
                print('黒の番です')
                can_put_list = othello.can_put_list(BLACK)
                if not can_put_list == []:
                    x, y, skip_count = player_1(can_put_list, current_board, black_npz_path)
                    bput_count += 1
                    if not skip_count == 0:
                        B_error_count += 1
                        b_skip_count += skip_count
                else:
                    i += 1
                    pass_count += 1
                    bput_count += 1
                    continue
            #  白のターン
            elif turn == WHITE:
                current_board = [othello.board_copy()]
                print('白の番です')
                can_put_list = othello.can_put_list(WHITE)
                if not can_put_list == []:
                    x, y, skip_count = player_2(can_put_list, current_board, white_npz_path)
                    wput_count += 1
                    if not skip_count == 0:
                        W_error_count += 1
                        w_skip_count += skip_count
                else:
                    i += 1
                    pass_count += 1
                    wput_count += 1
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

    b_p = (B_winner_count/battle_time)* 100
    w_p = (W_winner_count/battle_time)* 100
    d_p = (D_winner_count/battle_time)*100
    print(str(battle_time)+'回の試合が終了しました。\nresult・・・')
    print('黒'+str(B_winner_count)+'回'+'白'+str(W_winner_count)+'回、勝ちました.'+'引き分けは'+str(D_winner_count)+'回です')
    print(str(pass_count)+'回パスでした')
    print('勝率は,黒：'+str(b_p)+'%\n白：'+str(w_p)+
          '%\n引き分け：'+str(d_p)+'%です。')
    if p_b == str(black_npz_path):
        b_sp = (b_skip_count/bput_count)*100
        b_ep = (B_error_count/bput_count)*100
        print('黒は'+str(battle_time)+'回試合で'+str(bput_count)+'回打ちました.\n'+str(b_skip_count)+
              '回、2番目以降確率が高い手を選択。\n一回目の予想がエラーだった数/自ターン数'+str(b_sp)+'%\n'
              '黒のエラー率(予想に失敗したターン数/回ってきたターン数)\n'+str(b_ep)+'%')
    if p_w == str(white_npz_path):
        w_sp = (w_skip_count/wput_count)*100
        w_ep = (W_error_count/wput_count)*100
        print('白は' + str(battle_time) + '回試合で' + str(wput_count) + '回打ちました.\n'+str(w_skip_count)+
              '回、2番目以降確率が高い手を選択。\n一回目の予想がエラーだった数/自ターン数'+str((w_skip_count/wput_count)*100)+'%\n'
              '白のエラー率(予想に失敗したターン数/自ターン数)\n'+str(w_ep)+'%')
    print(str(battle_time)+'回の実行時間は'+str(time_e-time_s)+'秒です')
    if not q == 'no':
        repo = [battle_time, p_b, p_w, B_winner_count, W_winner_count, D_winner_count, b_p, w_p, d_p,
            b_sp, b_ep, w_sp, w_ep]
        if q == 'append':
            othello.save_report(repo, r_name)
        elif q == 'new':
            othello.make_report(repo, r_name)


