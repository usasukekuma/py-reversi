import random
from game_master import *
class random_player(game_master):
    def random_action(self, turn):
        act = self.can_put_list(turn)
        act_x = random.choice(act)
        print(act)
        print(act_x)
        return act_x

    def human_player(self, player):
        can_put_list = self.can_put_list(player)
        print('リストから選択！')
        print(str(can_put_list)+':')
        list_number = int(input())
        act = can_put_list[list_number]
        return act

