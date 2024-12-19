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

sum = 0
with open(file_name) as f:
    lines = f.readlines()

    # create diagonal lines
    rows = len(lines)
    cols = len(lines[0]) - 1 # remove 1 for \n
    # print(width,height)
    x = 0
    y = 0

    l = []
    s = ""

    for i in range(cols):
        y = 0
        s = ""
        for j in range(i+1).__reversed__():
            if y < rows:
                # print(j,y)
                s += lines[y][j]
                y+=1
        l.append(s)


    if rows < cols:
        tmp = rows
        rows = cols
        cols = tmp

    for row_start in range(rows-cols+2):
        x = cols - 1
        s = ""
        for y in range(rows)[row_start+cols-2:rows]:
            if y < rows and x >=0:
                print(x,y)
                s += lines[y][x]
                y+=1
                x-=1

        l.append(s)


    print(l)