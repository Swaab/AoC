import numpy as np

file_name = "C:/Users/danie/Documents/repos/2024/day16/input.txt"


def move(grid, start, end):
    start_pos = np.argwhere(grid == start)[0]
    end_pos = np.argwhere(grid == end)[0]
    rows = end_pos[0] - start_pos[0]
    cols = end_pos[1] - start_pos[1]
    s = ""
    if cols < 0 and rows > 0:
        s += "v" * rows + "<" * abs(cols)
    elif cols > 0 and rows < 0:
        s += ">" * cols + "^" * abs(rows)
    elif cols < 0 and rows < 0:
        s += "<" * abs(cols) + "^" * abs(rows)
    elif cols > 0 and rows > 0:
        s += "v" * rows + ">" * cols
    else:
        if cols < 0:
            s += "<" * abs(cols)
        if rows > 0:
            s += "v" * rows
        if rows < 0:
            s += "^" * abs(rows)
        if cols > 0:
            s += ">" * cols

    return s


numpad = np.array([["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["#", "0", "A"]])
dirpad = np.array([["#", "^", "A"], ["<", "v", ">"]])


def get_sequence(grid, sequence):
    res = []
    sequence = ["A"] + sequence
    for i in range(len(sequence) - 1):
        moves = move(grid, sequence[i], sequence[i + 1])
        res += list(moves + "A")
    return res


import re

codes = ["341A", "480A", "286A", "579A", "149A"]
codes = [
    "029A",
    "980A",
    "179A",
    "456A",
    "379A",
]
# codes = ["789A", "120A"]
# Voor elke stap groote de afstand door rekenen

som = 0
for code in codes:
    print(code)
    sequence = get_sequence(numpad, list(code))
    print("finish numpad: ", "".join(sequence))
    sequence = get_sequence(dirpad, list(sequence))
    print("finish numpad: ", "".join(sequence))
    sequence = get_sequence(dirpad, list(sequence))
    res = "".join(sequence)
    length = len(sequence)
    print("finish numpad: ", res)
    n = int(re.findall(r"\d+", code)[0])
    print(f"l={length},n={n}  | sum={n* length}")
    som += n * length

# 138308 to high
print(f"final sum: {som}")
