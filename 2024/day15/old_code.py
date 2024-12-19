has_moved = False
if move == "^":
    arr = maze[0:next_row, next_col]
    positions = np.argwhere(arr == ".")
    if len(positions) > 0:
        has_moved = True

        maze[positions[-1][0] : next_row, next_col] = "O"
elif move == "<":
    arr = maze[next_row, 0:next_col]
    positions = np.argwhere(arr == ".")
    if len(positions) > 0:
        has_moved = True

        maze[next_row, positions[-1][0] : next_col] = "O"
elif move == ">":
    arr = maze[next_row, next_col:width]
    print(arr)
    positions = np.argwhere(arr == ".")
    if len(positions) > 0:
        print(next_row, next_col, positions[0][0])
        has_moved = True

        maze[next_row, next_col : next_col + positions[0][0] + 1] = "O"
elif move == "v":
    arr = maze[next_row:height, next_col]
    positions = np.argwhere(arr == ".")
    if len(positions) > 0:
        maze[next_row : next_row + positions[0][0] + 1, next_col] = "O"
        has_moved = True
        # Move the robot
