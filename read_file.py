from game_master import *
import pandas as pd
import itertools


othello = game_master()
df = pd.read_csv('a.csv', header=None)  # 文字列が含まれるので
tmp = df.values.tolist()
print(tmp)
print(list(itertools.chain.from_iterable(tmp)))


list_bwin = []
list_wwin = []
list_dwin = []
tmp_b = []
tmp_w = []
tmp_d = []
n_f = [list_bwin, list_wwin, list_dwin]
n_s = [tmp_b, tmp_w, tmp_d]





