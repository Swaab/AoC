from enum import Enum
from typing import List
import numpy as np
# file_name = "/Users/swaab/Documents/GIT-Projects/AoC/2023/day6/input.txt"
file_name = "C:/Users/danie/Documents/repos/2024/day11/input.txt"



MAX_REP = 25

def blink2(iteration, val):
    if iteration == MAX_REP:
        return [val]
    s = str(val)
    n = len(s)
    if val == 0:
        return 1
    elif n%2==2:
        return [int(s[0:n/2]), int(s[n/2:n])]
    else:
        return val*2024


def blink(iteration, val):
    if iteration == MAX_REP:
        return [val]
    s = str(val)
    n = len(s)
    if val == 0:
        return [blink(iteration+1, 1)]
    elif n%2==2:
        return [blink(iteration+1, int(s[0:n/2])), blink(iteration+1, int(s[n/2:n]))]
    else:
        return [blink(iteration+1, val*2024)]

with open(file_name) as f:
    lines = f.readlines()
    stones = [int(item) for item in lines[0].strip().split(' ')]

    # vals = stones.copy()
    som = 0
    for j,stone in enumerate(stones):
        res = blink(MAX_REP, stone)
        som += len(res)
        print('stone', j)

            #     s = str(stone)
            #     n = len(s)
            #     if stone == 0:
            #         tmp.append(1)
            #     elif n % 2 == 0:
            #         middle = int(n / 2)
            #         tmp.append(int(s[0:middle]))
            #         tmp.append(int(s[middle:n]))
            #         # tmp.append() = stone[0:j] + [int(s[0:n / 2]), int(s[n / 2:n])] + stone[j:]
            #     else:
            #         tmp.append(stone * 2024)
            # vals = tmp

    print(som)

    #
    # for i in range(MAX_REP):
    #     tmp = []
    #     for j, stone in enumerate(vals):
    #         s = str(stone)
    #         n = len(s)
    #         if stone == 0:
    #             tmp.append(1)
    #         elif n % 2 == 0:
    #             middle = int(n / 2)
    #             tmp.append(int(s[0:middle]))
    #             tmp.append(int(s[middle:n]))
    #             # tmp.append() = stone[0:j] + [int(s[0:n / 2]), int(s[n / 2:n])] + stone[j:]
    #         else:
    #            tmp.append(stone * 2024)
    #     vals = tmp
    #
    #
    # print(len(vals))