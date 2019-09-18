import csv
import numpy as np

end_file = [[0, 1, 2, 3, 4, 5, 6],
            [1, 2, 3, 4, 5, 6, 7]]

def save_list(name):
    with open(name + '.csv', 'w') as f:
        writer = csv.writer(f)


name = input()
save_list(name)
