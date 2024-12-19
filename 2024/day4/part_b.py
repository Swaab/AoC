file_name = "C:/Users/danie/Documents/repos/2024/day4/input.txt"
import numpy as np
import re

def get_colum_string(arr):
    return ["".join(arr[:, col]) for col in range(arr.shape[1])]


# coordinates = []

def to_coordinate (row, pos, flipped=False):
    # position == row
    col = row - (cols-pos)+1 if flipped else row - pos -1
    row = pos + 1 # +1 for getting the A
    return row,col


def get_indices(table, flipped=False):
    s_list = get_colum_string(np.array(table))
    coordinates = []
    count =0
    for i, line in enumerate(s_list):
        d1_i_mas = [m.start() for m in re.finditer('MAS', line)]
        d1_i_san =  [m.start() for m in re.finditer('SAM', line)]

        for pos in d1_i_san + d1_i_mas:
            count+=1
            coordinates.append(to_coordinate(i, pos, flipped))

    return coordinates

som = 0
with open(file_name) as f:
    lines = f.readlines()
    cols = len(lines[0]) - 1 # remove 1 for \n

    table_d1 = []
    table_d2 = []

    for i, row in enumerate(lines):
        row=row.strip()
        table_d1.append(list(("."*i)+row+('.'*(cols-i))))
        table_d2.append(list(("."*(cols-i))+row+('.'*i)))

    cord1 = get_indices(table_d1)
    cord2 = get_indices(table_d2,flipped=True)

    from collections import defaultdict

    d = defaultdict(lambda: defaultdict(int))
    for x, y in cord1 + cord2:
        d[x][y] += 1

    for x in d:
        for y in d[x]:
            if d[x][y] >=2:
                som+=1

    print(som)

