file_name = "/Users/swaab/Documents/GIT-Projects/AoC/2023/day1/input.txt"

import re

str_nums = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
}
sum = 0
with open(file_name) as f:
    lines = f.readlines()
    for line in lines:
        for key,val in str_nums.items():
            line = line.replace(key, key + str(val) + key)
        print(line)
        nums = re.findall(r'\d+', line)
        last_number = nums[len(nums)-1]
        sum += int((nums[0][0]) + last_number[len(last_number)-1])


print(sum)