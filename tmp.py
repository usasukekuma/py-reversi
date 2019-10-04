from game_master import *
b = [[0, 0, 0, 1, 1, 1, 1, 1], [2, 2, 1, 1, 1, 2, 1, 2], [2, 1, 2, 1, 2, 1, 1, 2], [2, 2, 1, 2, 1, 2, 1, 2], [2, 2, 2, 1, 2, 2, 1, 2], [2, 2, 1, 1, 1, 1, 1, 2], [2, 1, 2, 1, 1, 1, 1, 2], [1, 2, 1, 1, 1, 1, 1, 2]]


def turn_over_list(x, y, player):  # ひっくり返せる石のリスト
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
                    put = b[check_y][check_x]
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

def can_put_list(player):  # おける場所リスト
    can_put = []
    for bx in range(BOARD_SIZE):
        for by in range(BOARD_SIZE):
            if b[by][bx] is not EMP:
                continue
            elif turn_over_list(bx, by, player) == []:
                continue
            else:
                can_put.append((bx, by))
    return can_put
print(can_put_list(BLACK))