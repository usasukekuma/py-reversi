from random_player import *

if __name__ == "__main__":
    othello = random_player()
    othello.view()
    turn = BLACK
    for i in range(0, 60):
        turn = othello.player_check(i)
        if turn == BLACK:
            hand = '黒の'
            othello.player_print(hand)
            x, y = othello.random_action(turn)
        else:
            hand = '白の'
            othello.player_print(hand)
            x, y = othello.random_action(turn)
        othello.put_stone(x, y, turn)
        othello.view()
    othello.end()