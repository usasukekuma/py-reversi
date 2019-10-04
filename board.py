EMP = 0
BLACK = 1
WHITE = 2
BOARD_SIZE = 8
b_WIN = 100
b_LOSE = -100
DRAW = 50
PASS = 3

class Board(object):
    def __init__(self):  # classを呼び出すと自動で呼び出されるメソッド
        # 8*8のリストをつくる
        self.board = []
        for a in range(BOARD_SIZE):  # BOARD_SIZE-1の範囲でループ
            # ↑で行↓で列
            self.board.append([EMP for b in range(BOARD_SIZE)])  # 初期値になにもないNONEを指定する(0はWHITEとして定義）

        self.board[3][3] = WHITE  # 初期石
        self.board[4][4] = WHITE
        self.board[3][4] = BLACK
        self.board[4][3] = BLACK

    def view(self):  # Boardを表示するメソッド
        print('\n')
        for disc_y in self.board:  # stoneリスト（行
            for disc_x in disc_y:  # stoneリスト（列
                if disc_x == WHITE:
                    print('W', end=" ")
                elif disc_x == BLACK:
                    print('B', end=" ")
                else:
                    print("*", end=" ")
            print("\n", end="")

    def board_copy(self):
        board_copy = self.board.copy()
        return board_copy
