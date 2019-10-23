t_x, t_y = 1,2
can_put_list = [(1,2)]
if not list(set((t_x, t_y)) & set(can_put_list)) == []:
    print('y')