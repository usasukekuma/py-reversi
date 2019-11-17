mini_corner = [(0, 0), (7, 0), (0, 7), (7, 7)]

can_put_list = [(0, 0), (7, 0), (0, 7), (7, 7)]


for idc in mini_corner:
    if idc in can_put_list:
        print('p')