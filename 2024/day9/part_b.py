from audioop import reverse
from enum import Enum
from typing import List, final
import numpy as np
# file_name = "/Users/swaab/Documents/GIT-Projects/AoC/2023/day6/input.txt"
file_name = "C:/Users/danie/Documents/repos/2024/day9/input.txt"
import sys
import numpy

class Block:

    def __init__(self, files, id, spaces):
        self.files = files
        self.id = id
        self.spaces = spaces
        self.s = [str(id)]*files

    def place_block(self, block):
        if self.spaces >= block.files:
            # update this block
            self.s += [str(block.id)]*block.files
            self.spaces -= block.files
            # update other block
            end_block.s[:end_block.files] = ["."]*block.files

            return True
        return False

    def final_s(self):
        return  self.s + ["."]*self.spaces

    def __str__(self):
        return "".join(self.final_s())

def to_space(l):
    count = 0
    id = 0
    res = []
    while count< len(l)-1:
        blocks = l[count]
        space = l[count+1]
        res.append(Block(blocks, id ,space))

        count +=2
        id+=1

        # print(id, blocks, space)

    res.append(Block(l[count],id, 0))
    # print(res)
    return res

with open(file_name) as f:
    lines = f.readlines()
    line = [int(item) for item in [list(line.strip()) for line in lines][0]]
    # print(line)
    l = to_space(line)

    for index, end_block in enumerate(reversed(l[1:])):

        for start_block in l[:len(l)-1-index]:
            if start_block.place_block(end_block):
                break


    res = []
    for block in l:
        res += block.final_s()

    som = 0
    for i in range(len(res)):
        if res[i] != ".":
            som += i* int(res[i])

    print(som)