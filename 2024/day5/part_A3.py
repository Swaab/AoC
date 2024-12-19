import math
from typing import List
import numpy as np
file_name = "C:/Users/danie/Documents/repos/2024/day5/input.txt"

import re

class Rule:
    def __init__(self, n, l, r):
        self.n = n
        self.l = l
        self.r = r

# Load data
rules = []
updates = []
with open(file_name) as f:
    lines = f.readlines()
    for line in lines:
        res = line.strip().split('|')
        if len(res)==2:
            l = res[0]
            r = res[1]
            rules.append([l,r])

        else:
            res = line.strip().split(',')
            if len(res) >= 2:
               updates.append(res)


# Find unique ordered list
# rules = np.array(rules)
# IDEA: create a new list if items non existend
levels = []
for [l,r] in rules:
    # check and pick level
    for level in level:
        if l in level:
            pass
        if r in level:
            pass
        
    level_l = None
    level_r = None
    if l in levels:
        level_l = levels[l]
    if r in levels:
        level_r = levels[r]
    if level_l and level_r:
        pass
    elif level_l and level_r is None:
        levels[r] = level_l
    elif level_l is None and level_r:
        levels[l] = level_r-1
    elif level_l is None and level_r is None:
        levels[l] = 0
        levels[r] = 1



def check_updates(updates, order):
    # Check updates
    som = 0
    for update in updates:
        copy = order.copy()
        prev = None
        good = True
        for page in update:
            try:
                n = copy.index(page)
                copy = copy[n+1:]
            except:
                good = False

        if good:
            print(update)
            som += int(update[math.floor(len(update) / 2)])

    print(som)