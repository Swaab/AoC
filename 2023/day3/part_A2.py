from typing import List
import numpy as np
file_name = "/Users/swaab/Documents/GIT-Projects/AoC/2023/day3/input.txt"

import re

def get_spots(lines):
    spots = []
    for line in lines:
        line = line.strip()
        l = re.sub(r'[0-9]', '.', line)
        spots.append([s != "." for s in l])
    return np.array(spots)

def add_boxes(pos: np.ndarray):
    pos_copy = pos.copy()
    for i in range(len(pos)):
        for j in range(len(pos[i])):
            if pos[i,j] == True:
                add = min(2,len(pos[i])-j)
                sub = min(1,j)
                if i > 0:
                    pos_copy[i - 1, j-sub:j+add] = True
                pos_copy[i, j-sub:j + add] = True
                if i < len(pos) - 1:
                    pos_copy[i + 1, j-sub:j+add] = True
    return pos_copy

sum = 0
with open(file_name) as f:
    lines = f.readlines()
    symbols = get_spots(lines)
    spots2 = add_boxes(symbols)
    rows = []
    for idx, line in enumerate(lines):
        numbers = re.findall(r'\d+', line)
        pos = 0
        for n in numbers:
            i = line[pos:].index(n) + pos
            pos = i+len(n)
            if any(spots2[idx, i:i+len(n)]):
                sum += int(n)
# 497433
print(sum)