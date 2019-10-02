list_bwin = []
list_wwin = []
list_dwin = []

for csv_row in open('data/ten.csv'):
    tmp = []
    if "WB" in csv_row:
        tmp = csv_row
        list_bwin.append(tmp)
    elif "WW" in csv_row:
        tmp = csv_row
        list_wwin.append(tmp)
    elif "WD" in csv_row:
        tmp = csv_row
        list_dwin.append(tmp)

print(list_bwin)
print(list_wwin)
print(list_dwin)