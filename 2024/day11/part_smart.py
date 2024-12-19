file_name = "C:/Users/danie/Documents/repos/2024/day11/input.txt"

info = {
    0: [[0], [1]],
    1: [[1], [2024], [20, 24], [2, 0, 2, 4]],
    2: [[2], [4048], [40, 48], [4, 0, 4, 8]],
    3: [[3], [6072], [60, 72], [6, 0, 7, 2]],
    4: [[4], [8096], [80, 96], [8, 0, 9, 6]],
    5: [
        [5],
        [10120],
        [20482880],
        [2048, 2880],
        [20, 48, 28, 80],
        [2, 0, 4, 8, 2, 8, 8, 0],
    ],
    6: [
        [6],
        [12144],
        [24579456],
        [2457, 9456],
        [24, 57, 94, 56],
        [2, 4, 5, 7, 9, 4, 5, 6],
    ],
    7: [
        [7],
        [14168],
        [28676032],
        [2867, 6032],
        [28, 67, 60, 32],
        [2, 8, 6, 7, 6, 0, 3, 2],
    ],
    8: [
        [8],
        [16192],
    ],
    9: [
        [9],
        [18216],
        [3686, 9184],
        [36, 86, 91, 84],
        [3, 6, 8, 6, 9, 1, 8, 4],
    ],
    16192: [
        [16192],
        [3277, 2608],
        [32, 77, 26, 8],
        [3, 2, 7, 7, 2, 6, 16192],
    ],
}
MAX_REP = 45


def get_stones(reps, stone_l):
    remaining = MAX_REP - reps
    som = 0
    for stone in stone_l:
        max = len(info[stone]) - 1
        if remaining > max:
            som += get_stones(reps + max, info[stone][max])
        else:
            som += len(info[stone][remaining])
    return som


with open(file_name) as f:
    lines = f.readlines()
    stones = [int(item) for item in lines[0].strip().split(" ")]
    keys = info.keys()

    som = 0
    res = []

    for stone in stones:
        if 0 <= stone < 10 or stone == 16192:
            res = get_stones(0, [stone])
            print(res)
        # else:
        #     length = int(math.log10(stone)) + 1
        #     if length % 2 == 0:
        #         n = math.pow(10, length / 2)
        #
        #         # The first part of the number i
        #         tmp.append(int(stone // n))
        #         # the second part
        #         tmp.append(int(stone % n))
        #     else:
        #         tmp.append(stone * 2024)

    # print(len(stones))
