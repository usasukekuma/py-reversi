import random


def random_action(can_put_list):
    act = can_put_list
    act_x = random.choice(act)
    print(act)
    print(act_x)
    return act_x

player_1 = random_action
a = []
if a == []:
    print('nassyi')
elif not a == []:
    print('pyon')