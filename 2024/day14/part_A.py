file_name = "C:/Users/danie/Documents/repos/2024/day14/input.txt"


class Robot:

    def __init__(self, s):
        pos, vel = s.strip().replace("p=", "").replace("v=", "").split(" ")
        x, y = pos.split(",")
        vertical, horizontal = vel.split(",")
        self.col = int(x)
        self.row = int(y)
        self.vertical = int(vertical)
        self.horizontal = int(horizontal)

    def __str__(self):
        return f"pos[{self.col},{self.row}] velocity[{self.vertical},{self.horizontal}]"


import numpy as np

with open(file_name) as f:
    lines = f.readlines()
    robots = [Robot(line) for line in lines]

    # grid size
    cols = 101
    rows = 103

    time = 100  # seconds

    res = np.zeros((rows, cols))
    for robot in robots:
        # determine pos in
        x = (robot.col + (time * robot.vertical)) % cols
        y = (robot.row + (time * robot.horizontal)) % rows
        res[y, x] += 1

    middle_row = int(rows / 2) + 1
    middle_col = int(cols / 2) + 1
    q1 = res[0 : middle_row - 1, 0 : middle_col - 1]
    q2 = res[0 : middle_row - 1, middle_col:cols]
    q3 = res[middle_row:rows, 0 : middle_col - 1]
    q4 = res[middle_row:rows, middle_col:cols]

    som = np.sum(q1) * np.sum(q2) * np.sum(q3) * np.sum(q4)
    print(som)
