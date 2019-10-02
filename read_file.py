from game_master import *

othello = game_master()

list_bwin = []
list_wwin = []
list_dwin = []
tmp_b = []
tmp_w = []
tmp_d = []
n_f = [list_bwin, list_wwin, list_dwin]
n_s = [tmp_b, tmp_w, tmp_d]


def conv(a, b):
    print(a)

for csv_row in open('a.csv'):
    tmp = []
    if "WB" in csv_row:
        tmp = csv_row
        tmp_b.append(tmp)
    elif "WW" in csv_row:
        tmp = csv_row
        tmp_w.append(tmp)
    elif "WD" in csv_row:
        tmp = csv_row
        tmp_d.append(tmp)
print(tmp_b)
print(tmp_w[-1])


