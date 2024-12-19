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
rules = np.array(rules)
order = []
while len(rules) > 0:
    if len(rules) == 1:
        order.append(rules[0,0])
        order.append(rules[0,1])
        rules = []
    else:
        uniques =  np.setdiff1d(rules[:,0],rules[:,1])
        order.append(uniques[0])
        # Create a mask to identify rows to keep
        mask = ~np.isin(rules[:, 0], uniques)

        # Apply the mask to filter rows
        rules = rules[mask]

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