from game_master import *
class human(game_master):
    def human_player(self, player):
        can_put_list = self.can_put_list(player)
        print('リストから選択！')
        print(str(can_put_list)+':')
        list_number = int(input())
        x, y = can_put_list[list_number]
        return x, y






