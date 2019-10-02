from game_master import *

othello = game_master()

<<<<<<< HEAD
board_vs = []
stone = []
battle_result = []


print('試合数いくつのCSVファイルですか？')
battle_count = int(input())
=======
list_bwin = []
list_wwin = []
list_dwin = []
tmp_b = []
tmp_w = []
tmp_d = []
n_f = [list_bwin, list_wwin, list_dwin]
n_s = [tmp_b, tmp_w, tmp_d]
>>>>>>> 6ad5fda9d09171668d04c6f552b72909054ea28e


<<<<<<< HEAD
battle_result = {idn: resul for idn, resul in enumerate(nassyi_list) if "WW" or 'WB' or 'WD' == resul}
print(battle_result)

=======

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

list_bwin = [a for a in tmp_b if not a is '"' or not a is '\n']
print(list_bwin)
print(list_wwin)
print(list_dwin)
>>>>>>> 6ad5fda9d09171668d04c6f552b72909054ea28e
