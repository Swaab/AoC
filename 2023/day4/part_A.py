from typing import List
import numpy as np
file_name = "/Users/swaab/Documents/GIT-Projects/AoC/2023/day4/input.txt"

import re

sum = 0
with open(file_name) as f:
    lines = f.readlines()
    for line in lines:
        line_counter = 0
        left,right=line.split(":")[1].split("|")
        l =  re.findall(r'\d+', left)
        r =  re.findall(r'\d+', right)
        # print(l, r)
        for n in r:
            if n in l:
                line_counter +=1

        # print(line_counter)
        addition = 0 if line_counter == 0 else 1 if line_counter==1 else pow(2,line_counter-1)
        print(addition)
        sum+= addition

print(sum)