from enum import Enum
from typing import List
import numpy as np
# file_name = "/Users/swaab/Documents/GIT-Projects/AoC/2023/day6/input.txt"
file_name = "/2024/day11/input.txt"
import sys
import numpy

def next(prev, row,col,table):
    width, height = map.shape
    if  0 <=row <width and 0<=col<height:
        val = table[row, col]
        if val-1 == prev:
            # print(row,col, "val: ",prev, val)
            if val == 9:
                return 1
            else:
                return find_paths(table, row,col)
        else:
            return 0
    else:
        return 0

def find_paths(table, row, col):
    prev_val = table[row, col]
    som = 0
    # print(prev_val)
    som += next(prev_val, row+1, col, table)
    som += next(prev_val, row, col+1, table)
    som += next(prev_val, row-1, col, table)
    som += next(prev_val, row, col-1, table)
    return som

with open(file_name) as f:
    lines = f.readlines()
    lines = [list(line.strip()) for line in lines]
    map = np.array(lines)
    map = map.astype(np.int64)

    # print(map.shape)
    width, height = map.shape
    # print(map)

    starts_pos = np.argwhere(map == 0)
    som =0
    for start in starts_pos:
        som+=find_paths(map, start[0], start[1])
        # print(som)

    print(som)