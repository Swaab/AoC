from typing import List
import numpy as np
file_name = "/Users/swaab/Documents/GIT-Projects/AoC/2023/day5/input.txt"

import re

def check_map(des, source, range, val):

    if source <= val < source + range:
        return des + (val-source)

    return None

def check_all(maps:List, val):
    for [des, source, range] in maps:
        res = check_map(des, source, range, val)
        if res is not None:
            return res

    return val

with open(file_name) as f:
    lines = f.readlines()
    seeds = re.findall(r'\d+', lines[0])
    seed_map = list(zip(seeds[::2], seeds[1::2]))
    print(seed_map)
    map_i = -1
    d = {}
    for line in lines[1:]:
        if "map:" in line:
            map_i +=1
        else:
            mappings = re.findall(r'\d+', line)
            if len(mappings) == 3:
                if map_i in d:
                    d[map_i].append([int(n) for n in mappings])
                else:
                    d[map_i] = [[int(n) for n in mappings]]

    l = []
    for (start, r) in seed_map:
        start = int(start)
        r = int(r)
        for i in range(start, start+r):
            search_val = i
            for key in d.keys():
                search_val = check_all(d[key], int(search_val))

            l.append(search_val)

    print(min(l))


