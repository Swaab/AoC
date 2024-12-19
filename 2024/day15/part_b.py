file_name = "C:/Users/danie/Documents/repos/2024/day15/input.txt"

import numpy as np

large_width = 400
np.set_printoptions(linewidth=large_width)
import sys

np.set_printoptions(threshold=sys.maxsize)


def next_pos(row, col, move):
    if move == "^":
        return row - 1, col
    if move == "<":
        return row, col - 1
    if move == ">":
        return row, col + 1
    if move == "v":
        return row + 1, col


def base_check(next_row, next_col, move, maze):
    follow_up_row, follow_up_col = next_pos(next_row, next_col, move)
    val = maze[follow_up_row, follow_up_col]
    while val not in [".", "#"]:
        follow_up_row, follow_up_col = next_pos(follow_up_row, follow_up_col, move)
        val = maze[follow_up_row, follow_up_col]
    if val == ".":
        if move == "<":
            maze[follow_up_row, follow_up_col : next_col + 1] = maze[
                follow_up_row, follow_up_col + 1 : next_col + 2
            ]
        elif move == ">":
            maze[follow_up_row, next_col : follow_up_col + 1] = maze[
                follow_up_row, next_col - 1 : follow_up_col
            ]
        maze[row, col] = "."
        # maze[next_row, next_col] = "@"
        return maze, next_row, next_col
    else:
        # cant move
        return maze, row, col


def super_move(row, col, move, maze, maze_update):
    # Its already up or down
    sign = maze[row, col]
    next_row = row - 1 if move == "^" else row + 1
    if sign == "[":
        allowed, maze_update = super_move(next_row, col, move, maze, maze_update)
        if allowed:
            allowed, maze_update = super_move(
                next_row, col + 1, move, maze, maze_update
            )
            if allowed:
                maze_update[next_row, col] = "["
                maze_update[row, col] = "."
                maze_update[next_row, col + 1] = "]"
                maze_update[row, col + 1] = "."
                return True, maze_update

        return False, None
    elif sign == "]":
        allowed, maze_update = super_move(next_row, col, move, maze, maze_update)
        if allowed:
            allowed, maze_update = super_move(
                next_row, col - 1, move, maze, maze_update
            )
            if allowed:
                maze_update[next_row, col - 1] = "["
                maze_update[row, col - 1] = "."
                maze_update[next_row, col] = "]"
                maze_update[row, col] = "."
                return True, maze_update

        return False, None
    elif sign == ".":
        return True, maze_update
    elif sign == "#":
        return False, None
    else:
        print("shouldnt come here")


def step(maze, row, col, move) -> np.array:
    next_row, next_col = next_pos(row, col, move)

    sign = maze[next_row, next_col]
    if sign == "#":
        return maze, row, col
    elif sign == ".":
        maze[row, col] = "."
        maze[next_row, next_col] = "@"
    elif sign in ["[", "]"]:
        # aparte condities voor links/recht/boven/onder
        if move in ["<", ">"]:
            return base_check(next_row, next_col, move, maze)
        else:
            allowed, maze_update = super_move(next_row, next_col, move, maze, maze)
            if allowed:
                maze = maze_update
                maze[next_row, next_col] = "@"
                maze[row, col] = "."
            else:
                return maze, row, col
    else:
        print("should come in this step")

    return maze, next_row, next_col


with open(file_name) as f:
    lines = f.readlines()
    double_lines = []
    for line in lines:
        if line[0] == "#":
            double_lines.append(
                list(
                    line.strip()
                    .replace("#", "##")
                    .replace(".", "..")
                    .replace("O", "[]")
                    .replace("@", "@.")
                )
            )
        else:
            break
    # maze = [list(line.strip()) for line in lines if line[0] == "#"]
    maze = np.array(double_lines)
    print(maze)
    print()

    height, width = maze.shape

    l = [line.strip() for line in lines[height + 1 :]]
    l = list("".join(l))
    moves = np.array(l).flatten()

    start_pos = np.argwhere(maze == "@")[0]
    row = start_pos[0]
    col = start_pos[1]
    n = len(moves)
    for i, move in enumerate(moves):
        maze, row, col = step(maze, row, col, move)
        print(f"move {i} of {n}")
        for arr in maze:
            print("".join(arr))
    som = 0
    positions = np.argwhere(maze == "[")
    for position in positions:
        som += position[0] * 100 + position[1]

        # print(maze)

    # 1540642 to high
    print(som)
