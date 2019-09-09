from q_learn import *
if __name__ == "__main__":
    othello = Q_Learning()
    othello.view()
    turn = BLACK
    for turn_count in range(0, 60):
            turn = othello.player_check(turn_count)
            if turn == BLACK:
                hand = '黒の'
                othello.player_print(hand)
                x, y = othello.q_action()
            else:
                hand = '白の'
                othello.player_print(hand)
                x, y = othello.random_action(turn)
            othello.put_stone(x, y, turn)
            othello.view()
    othello.end()



