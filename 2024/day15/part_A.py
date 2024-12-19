import numpy as np

file_name = "C:/Users/danie/Documents/repos/2024/day15/input.txt"


def next_pos(row, col, move):
    if move == "^":
        return row - 1, col
    if move == "<":
        return row, col - 1
    if move == ">":
        return row, col + 1
    if move == "v":
        return row + 1, col


def step(maze, row, col, move) -> np.array:
    next_row, next_col = next_pos(row, col, move)

    sign = maze[next_row, next_col]
    if sign == "#":
        return maze, row, col
    elif sign == ".":
        maze[row, col] = "."
        maze[next_row, next_col] = "@"
    elif sign == "O":
        # aparte condities voor links/recht/boven/onder

        follow_up_row, follow_up_col = next_pos(next_row, next_col, move)
        val = maze[follow_up_row, follow_up_col]
        while val not in [".", "#"]:
            follow_up_row, follow_up_col = next_pos(follow_up_row, follow_up_col, move)
            val = maze[follow_up_row, follow_up_col]
        if val == ".":
            maze[follow_up_row, follow_up_col] = "O"
            maze[row, col] = "."
            maze[next_row, next_col] = "@"
        else:
            # cant move
            return maze, row, col

    else:
        print("should come here")

    return maze, next_row, next_col


with open(file_name) as f:
    lines = f.readlines()

    maze = [list(line.strip()) for line in lines if line[0] == "#"]
    maze = np.array(maze)
    print(maze)
    print()

    height, width = maze.shape

    l = [line.strip() for line in lines[height + 1 :]]
    l = list("".join(l))
    # l = [list(line) for line in lines[height + 1 :]]
    moves = np.array(l).flatten()

    start_pos = np.argwhere(maze == "@")[0]
    row = start_pos[0]
    col = start_pos[1]
    for move in moves:
        maze, row, col = step(maze, row, col, move)

        # print(maze)
        # print()
    som = 0
    positions = np.argwhere(maze == "O")
    for position in positions:
        som += position[0] * 100 + position[1]

    print(som)
