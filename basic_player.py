import random

def human_player(can_put_list, trash_0, trash1):
    print('リストから選択！')
    print(str(can_put_list)+':')
    list_number = int(input())
    act_x = can_put_list[list_number]
    x, y = act_x
    return x, y, 0

def random_action(can_put_list, trash, trash1):
    act_x = random.choice(can_put_list)
    print(act_x)
    x, y = act_x
    return x, y, 0








