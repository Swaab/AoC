
from enum import Enum
from typing import List
import numpy as np
# file_name = "/Users/swaab/Documents/GIT-Projects/AoC/2023/day6/input.txt"
file_name = "C:/Users/danie/Documents/repos/2024/day8/input.txt"
import sys
import numpy

def check_freq(freq, width, height):
    return freq[0] >=0 and freq[1]>=0 and freq[0] < width and freq[1] < height

with open(file_name) as f:
    lines = f.readlines()
    lines = [list(line.strip()) for line in lines]
    map = np.array(lines)
    print(map.shape)
    width, height = map.shape
    list = np.unique(map).tolist()
    empty = np.zeros(map.shape)
    list.remove('.')
    print(list)
    for tower in list:
            locations = np.argwhere(map == tower)
            for i,start in enumerate(locations):
                for end in locations[i+1:]:
                    distance = [start[0]-end[0], start[1]-end[1]]
                    freq1 = start + distance
                    freq2 = end - distance

                    if check_freq(freq1, width, height):
                        empty[freq1[0],freq1[1]] = 1
                    if check_freq(freq2, width, height):
                        empty[freq2[0], freq2[1]] = 1

    # print(np.where(array == 0, '.', '#'))

    som= np.count_nonzero(empty == 1)
    print(som)