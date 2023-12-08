from typing import List
import numpy as np
file_name = "/Users/swaab/Documents/GIT-Projects/AoC/2023/day3/input.txt"

import re
import sys

class LinePos():

    def __init__(self, line, s):
        idx = line.index(s)
        self.start = idx
        self.end = idx+len(s)-1
        self.val = s

    def __str__(self):
        return f'{self.val}: [{self.start},{self.end}]'

class Row():
    numbers: List[LinePos]
    symbols: List[LinePos]

    def __init__(self, l: str):
        self.numbers = []
        self.symbols = []
        numbers = re.findall(r'\d+', l)
        self.line = l
        for n in numbers:
            l = re.sub( r'[0-9]', '', l)
            l = l.replace(n, "")
        symbols = [symbol for symbol in l.strip().split(".") if symbol !='']
        self.find_indices(numbers, symbols)

    def find_indices(self, nums, syms):
        position = 0
        for num in nums:
            pos = LinePos(self.line[position:], num)
            position = pos.end
            self.numbers.append(pos)
        position = 0
        for sym in syms:
            pos = LinePos(self.line[position:], sym)
            position = pos.end
            self.symbols.append(pos)

    def __str__(self):
        return f'symbols: {[str(s) for s in self.symbols]} \n numbers: {[str(s) for s in self.numbers]}'

sum = 0
with open(file_name) as f:
    lines = f.readlines()
    rows = []
    for line in lines:
        row = Row(line)
        rows.append(row)

    spots = np.full((len(rows),len(rows[0].line)-1), False)
    # find engine values
    for idx, row in enumerate(rows):
        for symbol in row.symbols:
            if idx > 0:
                spots[idx-1, symbol.start-1:symbol.end+2] = True
            spots[idx, symbol.start-1:symbol.end+2] = True
            if idx < len(rows) -1:
                spots[idx+1, symbol.start-1:symbol.end+2] = True

    for idx, row in enumerate(rows):
        for num in row.numbers:
            if any(spots[idx,num.start:num.end]):
                sum+= int(num.val)

print(sum)