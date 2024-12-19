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


def check_rule(a,b,rules):


for update in updates:
    # check rules
    for i in range (len(update)-1):
