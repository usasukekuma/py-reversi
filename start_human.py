
from human import *

if __name__ == "__main__":
    othello = human()
    othello.view()
    turn = BLACK
    for i in range(0, 60):
        turn = othello.player_check(i)
        if turn == BLACK:
            hand = '黒の'
        else:
            hand = '白の'
        othello.player_print(hand)
        x, y = othello.human_player(turn)
        othello.put_stone(x, y, turn)
        othello.view()
    othello.end()



