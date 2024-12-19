import math
from typing import List
import numpy as np
file_name = "C:/Users/danie/Documents/repos/2024/day5/input.txt"

def check_update(page, next, update, i , start) :
    print(page,next)
    if i > 1 and (page == start or next == start):
        return False
    if page in d:
        indices = d[page]
        if next in indices:
        # do the same from page in d, but with the next and increase i
            if i==len(update)-1:
                return True
            else:
                return check_update(next, update[i+1], update,  i+1, start)
        else:
            # go through each indicex
            # for j in indices:
            #     res = check_update(j, next, update, i, start)
            #     if res:
            #         return True
            return False
    else:
        return False

som =0
min=0
with open(file_name) as f:
    lines = f.readlines()
    reading_rules = True

    d = {}
    starts = set()
    ends = set()
    for line in lines:
        if reading_rules:
            if line == "\n":
                reading_rules=False


            res = line.split('|')
            if len(res)==2:
                l = res[0].strip()
                r = res[1].strip()
                if l in d:
                    d[l].append(r)
                else:
                    d[l] = [r]

                starts.add(l)
                ends.add(r)
        else:
            # part 2; ['83', '69', '15', '79', '37', '44', '52']
            update = line.strip().split(',')
            if check_update(update[0], update[1], update, 1, update[0]):
                som += int(update[math.floor(len(update) / 2)])
            else:
                min+=1

print('errors ', min)
# 11387 To high
print('som', som)