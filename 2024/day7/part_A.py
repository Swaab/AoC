from enum import Enum
from typing import List
import numpy as np
# file_name = "/Users/swaab/Documents/GIT-Projects/AoC/2023/day6/input.txt"
file_name = "C:/Users/danie/Documents/repos/2024/day7/input.txt"
import sys
import numpy

def calc(goal, val, l):
    if len(l) == 0:
        return val == goal
    else:
        return calc(goal, val + l[0], l[1:]) or calc(goal, val * l[0], l[1:])  or calc(goal, int(str(val) + str(l[0])), l[1:])

with open(file_name) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    som = 0
    for line in lines:
        n, l = line.split(": ")
        n = int(n)
        l = [int(item) for item in l.split(' ') ]

        if calc(n, 0, l):
            som += n

    print(som)
