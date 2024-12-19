from msilib.schema import tables
from typing import List
import numpy as np
file_name = "C:/Users/danie/Documents/repos/2024/day4/input.txt"
import numpy as np
import re

def check_around(x,y, table):
    som = 0
    if table[x,x+4:y].join() == 'xmas':
        som+=1
    if table[x-4, x: y].join() == 'smax':
        som += 1
    if table[x:y,y+4].join() == 'xmas':
        som+=1
    if table[x:y-4,y].join() == 'smax':
        som += 1
    if table[x, x + 4:y].join() == 'xmas':
        som += 1

# 012345
# 112345
# 222345
# 333345
# 444445
# 555555

# 012345
# 112345
# 222345
# 333345
# 444445
# 555555
# 666666
# 777777

def get_colum_string(arr):
    return ["".join(arr[:, col]) for col in range(arr.shape[1])]


som = 0
with open(file_name) as f:
    lines = f.readlines()
    cols = len(lines[0]) - 1 # remove 1 for \n

    table_d1 = []
    table_d2 = []
    table_cols = []
    rows = []
    i=2
    for i, row in enumerate(lines):
        row=row.strip()
        rows.append(row)
        table_cols.append(list(row))
        table_d1.append(list(("."*i)+row+('.'*(cols-i))))
        table_d2.append(list(("."*(cols-i))+row+('.'*i)))

    arr = np.array(table_d1)
    arr2 = np.array(table_d2)
    arr3 = np.array(table_cols)

    d1 = get_colum_string(arr)
    d2 = get_colum_string(arr2)
    cols =  get_colum_string(arr3)
    lines = d1+d2+rows+cols

    for s in lines:
        som += s.count("XMAS") + s.count("SAMX")

    print(som)