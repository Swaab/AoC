from enum import Enum
from marshal import dumps
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


def add_pos_dir(pos_to_dir, row, col, direction):
    if row in pos_to_dir:
        if col in pos_to_dir[row]:
            val = pos_to_dir[row][col]
            if direction in val:
                return pos_to_dir, True
            else:
                val.append(direction)
        else:
            pos_to_dir[row][col]= [direction]
    else:
        pos_to_dir[row]= {col: [direction]}

    return pos_to_dir, False

def move(direction: Move, map, row, col, pos_to_dir):
    is_loop = False
    if direction == Move.up:
        positions = np.argwhere(map[:row,col] == "#")
        if len(positions) > 0:
            [x] = positions[len(positions)-1]
            x = x+1 # one row lower
            map[x:row, col] = "X"
            pos_to_dir, is_loop = add_pos_dir(pos_to_dir, row, col, direction )

            direction = Move.right
            row = x
        else:
            map[:row,col]= "X"
            return map
    elif direction == Move.right:
        positions = np.argwhere(map[row,col:] == "#")
        if len(positions) > 0:
            [y] = positions[0]
            y = y+col # one row lower
            map[row, col:y] = "X"
            pos_to_dir, is_loop = add_pos_dir(pos_to_dir, row, y-1, direction )

            direction = Move.down
            col = y-1
        else:
            map[row,col:]= "X"
            return map
    elif direction == Move.down:
        positions = np.argwhere(map[row:,col] == "#")
        if len(positions) > 0:
            [x] = positions[0]
            x = x+row # one row lower
            map[row:x, col] = "X"
            pos_to_dir, is_loop = add_pos_dir(pos_to_dir, x-1, col, direction )

            direction = Move.left
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
            map[row, y:col] = "X"
            pos_to_dir, is_loop = add_pos_dir(pos_to_dir, row, col, direction )

            direction = Move.up
            col = y
        else:
            map[row,:col]= "X"
            return map

    if is_loop:
        return None

    # print(map, '\n')
    return move(direction, map, row, col, pos_to_dir)

som = 0
with open(file_name) as f:
    lines = f.readlines()
    lines = [list(line.replace('\n',"")) for line in lines]
    map = np.array(lines)
    dir = {}
    start = f
    [[row, col]] = np.argwhere(map == "^")
    res = move(Move.up, map, row, col, dir)

    # Check for loops
    coordinates = np.argwhere(res == "X")
    for [x,y] in coordinates:
        print(x,y)
        dir = {}
        tmp = np.array(lines)
        tmp[x,y] = "#"
        none_if_loop = move(Move.up, tmp, row, col, dir)
        # print(none_if_loop)
        if none_if_loop is None:
            som+=1
    # 4818 to low
    print(som)

