from enum import Enum
from typing import List
import numpy as np
# file_name = "/Users/swaab/Documents/GIT-Projects/AoC/2023/day6/input.txt"
file_name = "/2024/day11/input.txt"
import sys
import numpy

def next(prev, row, col,table):
    width, height = map.shape
    if  0 <=row <width and 0<=col<height:
        val = table[row, col]
        if val-1 == prev:
            # print(row,col, "val: ",prev, val)
            if val == 9:
                return [[row,col]]
            else:
                return find_paths(table, row,col)
        else:
            return []
    else:
        return []

def find_paths(table, row, col):
    prev_val = table[row, col]
    som = []
    # print(prev_val, row, col)
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

    # res =
    starts_pos = np.argwhere(map == 0)
    # print(starts_pos)
    som = 0
    for start in starts_pos:
        res = np.zeros(map.shape)
        positions =find_paths(map, start[0], start[1])
        for pos in positions:
            res[pos[0],pos[1]] = 1
        # print(som)
        som+= np.count_nonzero(res==1)

    print(som)