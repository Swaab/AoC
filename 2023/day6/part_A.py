from typing import List
import numpy as np
file_name = "/Users/swaab/Documents/GIT-Projects/AoC/2023/day6/input.txt"

import re

with open(file_name) as f:
    lines = f.readlines()
    time =[int(v) for v in  re.findall(r'\d+', lines[0])]
    distances = [int(v) for v in re.findall(r'\d+', lines[1])]
    res = 1
    for t,distance in zip(time,distances):
        counter = 0
        for i in range(t):
            print(i)
            speed = i
            run_time = t-i
            d = speed*run_time
            if d>distance:
                counter+=1
        res *= counter

    print(res)