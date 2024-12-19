from enum import Enum
from typing import List
import numpy as np
# file_name = "/Users/swaab/Documents/GIT-Projects/AoC/2023/day6/input.txt"
file_name = "C:/Users/danie/Documents/repos/2024/day8/input.txt"
import sys
import numpy

def find_pos(pos, counter, d, is_plus=True):
    keep_looking = True
    while keep_looking:
        if is_plus:
            freq = pos + d
        else:
            freq = pos - d

        if check_freq(freq, width, height):
            counter[freq[0], freq[1]] = 1
        else:
            keep_looking = False

        pos = freq

    return counter

def check_freq(freq, width, height):
    return 0 <= freq[0] < width and 0 <= freq[1] < height

with open(file_name) as f:
    lines = f.readlines()
    lines = [list(line.strip()) for line in lines]
    map = np.array(lines)
    width, height = map.shape
    list = np.unique(map).tolist()
    empty = np.zeros(map.shape)
    list.remove('.')
    for tower in list:
            locations = np.argwhere(map == tower)
            for i,start in enumerate(locations):
                for end in locations[i+1:]:
                    distance = [start[0]-end[0], start[1]-end[1]]
                    empty = find_pos(start, empty, distance)
                    empty = find_pos(start, empty, distance, False)
                    empty = find_pos(end, empty, distance, False)
                    empty = find_pos(end, empty, distance, )

    # 813 To low
    print(np.where(empty == 0, '.', '#'))
    som= np.count_nonzero(empty == 1)
    print(som)