from game_master import *



with open('nassyi.csv', newline='') as f:
    nassyi_csv = csv.reader(f)
    nassyi_list = list(nassyi_csv)

battle_count = 10000

for a in range (0, battle_count):
    for b in