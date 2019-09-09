from random_player import *
if __name__ == "__main__":
    print('make file\ninput file name')
    name = input(int())
    othello = random_player()
    othello.view()
    turn = BLACK
    for i in range(60):
        turn = othello.player_check(i)
        if turn == BLACK:
           hand = '黒の'
           othello.player_print(hand)
           act_x = othello.random_action(turn)
           othello.make_list(act_x)
           x, y = act_x
        else:
           hand = '白の'
           othello.player_print(hand)
           act_x = othello.random_action(turn)
           othello.make_list(act_x)
           x, y = act_x
        othello.put_stone(x, y, turn)
        othello.view()
    othello.end(name)
