import random

def human_player(self, player):
    can_put_list = self.can_put_list(player)
    print('リストから選択！')
    print(str(can_put_list)+':')
    list_number = int(input())
    x, y = can_put_list[list_number]
    return x, y

def random_action(can_put_list, trash_0):
    act_x = random.choice(can_put_list)
    print(act_x)
    return act_x








