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


import sys

import numpy as np

np.set_printoptions(threshold=sys.maxsize)
from matplotlib import pyplot as plt


with open(file_name) as f:
    lines = f.readlines()
    robots = [Robot(line) for line in lines]

    # grid size
    cols = 101
    rows = 103

    time = 100  # seconds

    for t in range(99, 999999, 101):
        res = np.zeros((rows, cols))
        for robot in robots:
            # determine pos in
            x = (robot.col + (t * robot.vertical)) % cols
            y = (robot.row + (t * robot.horizontal)) % rows
            res[y, x] += 1

        print(t)
        # print(res)
        # print()
        plt.title = t
        plt.imshow(res, interpolation="nearest")
        plt.show()
# 99
# 200
# 301
# 402
# 503?
#  604'
# 705
