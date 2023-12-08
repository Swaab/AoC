from typing import List
import numpy as np
file_name = "/Users/swaab/Documents/GIT-Projects/AoC/2023/day3/input.txt"

import re


def check_around_number(data:np.ndarray, row, i_start,i_end):
    width, height = data.shape
    if i_start == 0:
        min_i = 0
    else:
        min_i = i_start-1

    max_i = i_end + 1 if i_end + 1 <= width else i_end

    if row -1 < 0:
        min_y = 0
    else:
        min_y = row -1

    if row + 2 > height:
        max_y = height
    else:
        max_y = row + 2

    # data range:
    area = data[min_y:max_y, min_i:max_i]
    clean = np.empty((width,height), dtype=str)
    clean[min_y:max_y, min_i:max_i] = data[min_y:max_y, min_i:max_i]

    # find star indices:
    # TODO: augment with initial indices to get the corret ones
    return np.argwhere(clean == "*")

    # return data[min_y:max_y,min_i:max_i]



sum = 0
with open(file_name) as f:
    lines = f.readlines()
    all =np.array([list(line.strip()) for line in lines])
    star_dict = {}
    for idx, line in enumerate(lines):
        numbers = re.findall(r'\d+', line)
        pos = 0
        for n in numbers:
            i = line[pos:].index(n) + pos
            pos = i+len(n)
            stars = check_around_number(all,idx,i,pos)
            for (i,j) in stars:
                if i in star_dict:
                    if j in star_dict[i]:
                        star_dict[i][j].append(n)
                    else:
                        star_dict[i][j] = [n]
                else:
                    star_dict[i] = {j:[n]}

    print(star_dict)
    for row,val in star_dict.items():
        for val in val.values():
            if len(val) == 2:
                sum += int(val[0]) * int(val[1])

print(sum)