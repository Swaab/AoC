from typing import List
import numpy as np
file_name = "/Users/swaab/Documents/GIT-Projects/AoC/2023/day4/input.txt"

import re

instances = {}
with open(file_name) as f:
    lines = f.readlines()
    for idx,line in enumerate(lines):
        # add one
        if idx in instances:
            instances[idx] += 1
        else:
            instances[idx] = 1
        for j in range(instances[idx]):
            line_counter = 0
            left,right=line.split(":")[1].split("|")
            l =  re.findall(r'\d+', left)
            r =  re.findall(r'\d+', right)
            # print(l, r)
            for n in r:
                if n in l:
                    line_counter +=1

            for i in range(idx+1,idx+1+line_counter):
                if i in instances:
                    instances[i] += 1
                else:
                    instances[i] = 1

res = sum(instances.values())
print(res)