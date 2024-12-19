from audioop import reverse
from enum import Enum
from typing import List
import numpy as np
# file_name = "/Users/swaab/Documents/GIT-Projects/AoC/2023/day6/input.txt"
file_name = "C:/Users/danie/Documents/repos/2024/day9/input.txt"
import sys
import numpy

def to_space(l):
    count = 0
    id = 0
    res = []
    while count< len(l)-1:
        blocks = l[count]
        space = l[count+1]
        res += [str(id)]*blocks +["."]*space

        count +=2
        id+=1

        # print(id, blocks, space)

    res+= [str(id)]*l[count]
    # print(res)
    return res

with open(file_name) as f:
    lines = f.readlines()
    line = [int(item) for item in [list(line.strip()) for line in lines][0]]
    # print(line)
    l = to_space(line)

    rev = [item for item in l if item !="."]

    spaces = len(l) - len(rev)
    # final[0:len(rev)]

    final = l.copy()
    for i, symbol in enumerate(l):
        if symbol == ".":
            n = rev.pop()
            final[i] = n
            final.pop()
            spaces -=1

        check = True
        count = len(final)-1
        while check:
            if final[count] == ".":
                final.pop()
                count -=1
                spaces-=1
            else:
                check=False

        if spaces == 0:
            break


    som = 0
    for i in range(len(final)):
        som += i* int(final[i])

    print(som)