from enum import Enum
from typing import List
import numpy as np
# file_name = "/Users/swaab/Documents/GIT-Projects/AoC/2023/day6/input.txt"
file_name = "C:/Users/danie/Documents/repos/2024/day6/input.txt"
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)
import re
class Move(Enum):
    down = 'down'
    up = 'up'
    left = "left"
    right = "right"

def move(direction: Move, map, row, col):
    if direction == Move.up:
        positions = np.argwhere(map[:row,col] == "#")
        if len(positions) > 0:
            [x] = positions[len(positions)-1]
            x = x+1 # one row lower
            direction = Move.right
            map[x:row, col] = "X"
            row = x
        else:
            map[:row,col]= "X"
            return map
    elif direction == Move.right:
        positions = np.argwhere(map[row,col:] == "#")
        if len(positions) > 0:
            [y] = positions[0]
            y = y+col # one row lower
            direction = Move.down
            map[row, col:y] = "X"
            col = y-1
        else:
            map[row,col:]= "X"
            return map
    elif direction == Move.down:
        positions = np.argwhere(map[row:,col] == "#")
        if len(positions) > 0:
            [x] = positions[0]
            x = x+row # one row lower
            direction = Move.left
            map[row:x, col] = "X"
            row = x-1
        else:
            map[row:,col]= "X"
            return map
    elif direction == Move.left:
        l = map[row,:col]
        positions = np.argwhere(l== "#")
        if len(positions) > 0:
            [y] = positions[len(positions)-1]
            y = y+1 # one row lower
            direction = Move.up
            map[row, y:col] = "X"
            col = y
        else:
            map[row,:col]= "X"
            return map

    print(map, "\n")
    return move(direction, map, row, col)

with open(file_name) as f:
    lines = f.readlines()
    lines = [list(line.replace('\n',"")) for line in lines]
    map = np.array(lines)
    print(map)
    start = f
    [[row, col]] = np.argwhere(map == "^")
    res = move(Move.up, map, row, col)
    print(res)
    som = np.count_nonzero(res == "X")
    # 4818 to low
    print(som)

