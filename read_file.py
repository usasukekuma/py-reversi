from game_master import *
import pandas as pd
import itertools

list_bwin = []
list_wwin = []
list_dwin = []
n_f = [list_bwin, list_wwin, list_dwin]
tmp_count = []

othello = game_master()
df = pd.read_csv('a.csv', header=None) # 文字列が含まれるので
df = df.replace('\r\n', '', regex=True)
tmp = df.values.tolist()
tmp = list(itertools.chain.from_iterable(tmp))
tmp_1 = [x for x in tmp if x]
print(tmp_1)




tmp_cb = [i for i, x in enumerate(tmp) if x == 'WB']
tmp_cw = [i for i, x in enumerate(tmp) if x == 'WW']
tmp_cd = [i for i, x in enumerate(tmp) if x == 'WD']

tmp_w = []
tmp_d = []
tmp_b = []

