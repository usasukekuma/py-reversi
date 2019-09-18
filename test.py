import csv

def save_list(name):
    end_file = (0,1,2,3,4,5,6)
    with open(name + '.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(end_file)

name = input()
save_list(name)
