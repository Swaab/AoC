import numpy as np

file_name = "C:/Users/danie/Documents/repos/2024/day16/input.txt"


class NumPad:

    def __init__(self):
        self.grid = np.array(
            [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["#", "0", "A"]]
        )

    def move(self, start, end):
        start_pos = np.argwhere(self.grid == start)[0]
        end_pos = np.argwhere(self.grid == end)[0]
        rows = end_pos[0] - start_pos[0]
        cols = end_pos[1] - start_pos[1]
        s = ""
        if cols < 0:
            s += "<" * abs(cols)
        if rows > 0:
            s += "v" * rows
        if rows < 0:
            s += "^" * abs(rows)
        if cols > 0:
            s += ">" * cols

        return s

    def __str__(self):
        return self.grid.__str__()


class DirPad:

    def __init__(self):
        self.grid = np.array([["#", "^", "A"], ["<", "v", ">"]])

    def move(self, start, end):
        start_pos = np.argwhere(self.grid == start)[0]
        end_pos = np.argwhere(self.grid == end)[0]
        rows = end_pos[0] - start_pos[0]
        cols = end_pos[1] - start_pos[1]
        s = ""
        # Does the order matter?
        if cols < 0:
            s += "<" * abs(cols)

        if rows > 0:
            s += "v" * rows

        if rows < 0:
            s += "^" * abs(rows)
        if cols > 0:
            s += ">" * cols

        # print(start, end, s)
        return s


def get_sequence(pad, sequence, join=True):
    res = ["A"] if join else []
    sequence = ["A"] + sequence
    for i in range(len(sequence) - 1):
        moves = pad.move(sequence[i], sequence[i + 1])
        if join:
            res += list("A".join(list(moves)) + "A")
        else:
            res += list(moves + "A")
    return res


numpad = NumPad()
dirpad = DirPad()

import re

codes = ["341A", "480A", "286A", "579A", "149A"]
codes = [
    "029A",
    "980A",
    "179A",
    "456A",
    "379A",
]

som = 0
for code in codes:
    print(code)
    sequence = get_sequence(numpad, list(code), False)
    print("finish numpad: ", "".join(sequence))
    sequence = get_sequence(dirpad, list(sequence), False)
    print("finish numpad: ", "".join(sequence))
    sequence = get_sequence(dirpad, list(sequence), False)
    res = "".join(sequence)
    length = len(sequence)
    print("finish numpad: ", res)
    n = int(re.findall(r"\d+", code)[0])
    print(f"l={length},n={n}  | sum={n* length}")
    som += n * length

# 138308 to high
print(f"final sum: {som}")
