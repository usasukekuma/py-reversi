from game_master import *



copy_board = current_board



def put_stone(px, py, player):  # 石を置くメソッド
    # すでに石があればおけない(Noneでないところ＝石がある）
    if self.board[py][px] is not EMP:  # Noneの比較は＝ではなくisをつかう。リストy行目のｘ列目だから
        return False  # Falseでおけないよ！ってする
    # ひっくり返せないときはおけない
    turn_over = self.turn_over_list(px, py, player)
    if turn_over == []:  # リストがからのとき＝ひっくり返す石がない
        return False
    self.board[py][px] = player  # 置けるときにそのWorBを代入
    for sx, sy in turn_over:
        self.board[sy][sx] = player  # ひっくり返せる石をひっくり返す
    return True

def minimax_turn_over(x, y, player, copy_board):  # ひっくり返せる石のリスト
    vector = [-1, 0, 1]  # 石をおいた位置からベクトル方向
    turn_over = []
    for ay in vector:  # 行のベクトル方向を示す
        for ax in vector:  # 列のベクトル方向
            if ax == 0 and ay == 0:  # 0*0はない
                continue  # 次のループへ
            turn_over_tmp = []
            count = 0
            while (True):
                count += 1  # 現在地からずらす
                # check_?で調べる石の座標
                check_x = x + (ax * count)  # 現在地からｘ軸方向に１ずつ＋ー移動
                check_y = y + (ay * count)  # 現在地からy軸方向に１ずつ＋ー移動
                # check座標がBOARD_SIZEの範囲内か
                if 0 <= check_x < BOARD_SIZE and 0 <= check_y < BOARD_SIZE:
                    put = copy_board[check_y][check_x]
                    # 石がないときその方向はそこで終了
                    if put == EMP:
                        break
                    if not put == player and not put == EMP:
                        turn_over_tmp.append((check_x, check_y))
                    # 相手の石があればひっくりかえせるリストに追加位
                    elif put == player:  # 自分の石があったとき。
                        if not turn_over_tmp == []:
                            turn_over.extend(turn_over_tmp)
                            break
                        elif turn_over_tmp == []:
                            break
                else:
                    break
    return turn_over  # turn_overがこの関数の戻





def minimax_player(can_put_list, curent_board, args):











if __name__ == '__main__':
    othello.view()
    i = 0
    k = 0
    while not k == 100:
        k = 0
        turn = othello.player_check(i)
        #  黒のターン
        if turn == BLACK:
            current_board = [othello.board_copy()]
            print('黒の番です')
            can_put_list = othello.can_put_list(BLACK)
            if not can_put_list == []:
                x, y = player_1(can_put_list, current_board, black_npz_path)
                bput_count += 1
            else:
                print('pass')
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
                x, y = player_2(can_put_list, current_board, white_npz_path)
                wput_count += 1
            else:
                print('pass')
                i += 1
                pass_count += 1
                wput_count += 1
                continue
        othello.put_stone(x, y, turn)
        othello.view()
        i += 1
        if othello.can_put_list(BLACK) == []:
            k += 50
        if othello.can_put_list(WHITE) == []:
            k += 50