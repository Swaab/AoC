file_name = "C:/Users/danie/Documents/repos/2024/day11/input.txt"

MAX_REP = 75
import math

def blink(iteration, val):
    # print(iteration)
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
    for i in range(MAX_REP):
        # print(i)
        tmp = []
        for stone in stones:
            if stone == 0:
                tmp.append(1)
            else:
                length = int(math.log10(stone)) + 1
                if length % 2 == 0:
                    n = math.pow(10, length / 2)

                    # The first part of the number i
                    tmp.append(int(stone // n))
                    # the second part
                    tmp.append(int(stone % n))
                else:
                    tmp.append(stone * 2024)

        stones = tmp
        print(i, len(stones))

    print(len(stones))