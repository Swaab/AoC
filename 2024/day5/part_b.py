import math
from tkinter.messagebox import RETRY
from typing import List
import numpy as np
file_name = "C:/Users/danie/Documents/repos/2024/day5/input.txt"


def fix_update(update, d):
    res = {}
    for page in update:
        count = 0
        for next_page in update:
            if page != next_page and next_page in d and page in d[next_page]:
                count+=1
        res[page] = count
    return res


def check_update(page, next, update, i , start) :
    # print(page,next)
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
            update = line.strip().split(',')

            if not check_update(update[0], update[1], update, 1, update[0]):
                res = fix_update(update, d)
                sorted_by_values = dict(sorted(res.items(), key=lambda item: item[1]))
                up = list(sorted_by_values.keys())
                som += int(up[math.floor(len(up) / 2)])

                # print()

print('errors ', min)
# 11387 To high
print('som', som)