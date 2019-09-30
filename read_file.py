from game_master import *


board_vs = []
stone = []
battle_result = []


print('試合数いくつのCSVファイルですか？')
battle_count = int(input())

with open('nassyi.csv', newline='') as f:
    nassyi_csv = csv.reader(f)
    nassyi_list = list(nassyi_csv)

battle_result = {idn: resul for idn, resul in enumerate(nassyi_list) if "WW" or 'WB' or 'WD' == resul}
print(battle_result)

