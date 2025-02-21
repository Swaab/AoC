import numpy as np

file_name = "C:/Users/danie/Documents/repos/2024/day16/input.txt"


with open(file_name) as f:
    lines = f.readlines()

    maze = [list(line.strip()) for line in lines if line[0] == "#"]
    maze = np.array(maze)
