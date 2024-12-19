file_name = "C:/Users/danie/Documents/repos/2024/day11/input.txt"

MAX_REP = 75
import math

#     if val == 1:
#         b= 1*2024
#         # 2 | 0 | 2 | 4
#     if val == 2:
#         b = 2*2024
#         c = 4048
#     if val == 3:
#         b = 3*2024
#         c = 6072
#     if val == 4:
#         b = 4 * 2024
#         c = 8096
def blink(iteration, val):
    print(iteration)
    if iteration == MAX_REP:
        return 1
    # s = str(val)
    # n = int(math.log10(val)) + 1


    if val == 0:
        return blink(iteration+1, 1)
    else :
        length = int(math.log10(val)) + 1
        if length%2==0:
            n = math.pow(10, length / 2)

            # The first part of the number i
            left = (val // n)
            # the second part
            right = (val % n)

            return blink(iteration+1, left) +  blink(iteration+1,right)
        else:
            return blink(iteration+1, val*2024)

with open(file_name) as f:
    lines = f.readlines()
    stones = [int(item) for item in lines[0].strip().split(' ')]

    som = 0
    res = []
    for j,stone in enumerate(stones):
        som += blink(0, stone)
        print('stone', j)


    print(som)