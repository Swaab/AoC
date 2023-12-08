import math

import numpy as np

from input.input_day3 import arr

def bit_list_to_val(l):
    bitvals = [power(i) for i in list(range(0, len(l)).__reversed__())]
    return  sum(l*bitvals)

def power(x):
    return math.pow(2,x)

def part1(bits):
    height, width = bits.shape

    gamma = np.sum(bits,0) > height / 2
    epsilon = gamma == False
    gamma = bit_list_to_val(gamma)
    epsilon = bit_list_to_val(epsilon)

    print(gamma*epsilon)

def get_rating(bits, inverse=False):
    height, width = bits.shape
    index = 0
    while height > 1 and index < width:
        count = np.sum(bits[:, index])
        if count >= height / 2:
            diff = bits[:, index] == 1
        else:
            diff = bits[:, index] == 0
        bits = bits[diff==False] if inverse else bits[diff]
        index += 1
        height, _ = bits.shape
    return bits[0,:]

def part2(bits):
    oxygen = get_rating(bits)
    co2 = get_rating(bits,True)


    print(bit_list_to_val(oxygen) * bit_list_to_val(co2))

input = np.array(arr)
part1(input)
part2(input)