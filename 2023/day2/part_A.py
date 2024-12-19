from enum import Enum


file_name = "C:/Users/danie/Documents/repos/2023/day2/input.txt"

class State(Enum):
    none = 'none'
    increase = 'increasing'
    decrease = 'decreasing'

def second_check(l, i):
    l1 = l.copy()
    l2 = l.copy()
    l3 = l.copy()
    del l1[i]
    del l2[i + 1]
    del l3[abs(i - 1)]
    return check(l1,True) or check(l2,True) or  check(l3,True)

def check(l, is_second=False):
    order = None
    for i in range(len(l) -1):
        diff =  abs(l[i] - l[i+1])
        if diff <1 or diff > 3:
           return 1 if second_check(l, i) and not is_second else 0

        elif l[i] < l[i+1] and (order == State.decrease or order == None) :
            order = State.decrease
        elif l[i] > l[i+1] and (order == State.increase or order == None):
            order = State.increase
        else:
            return 1 if second_check(l, i) and not is_second else 0

    return 1

sum = 0
with open(file_name) as f:
    lines = f.readlines()
    for line in lines:
        nums = [int(n) for n in line.split(" ")]
        # print(nums)
        res = check(nums)
        if res == 0:
            print(nums)
        sum += res


print(sum)