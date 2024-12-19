file_name = "C:/Users/danie/Documents/repos/2024/day3/input.txt"

def flatten(l):
    return [x for xs in l for x in xs]

som = 0
with open(file_name) as f:
    lines = f.readlines()
    rows = []
    s= ""
    for line in lines:
        # print(line)
        s += line
    do_list = s.split('do()')
    do_list = [do.split('don\'t()')[0] for do in do_list]
    do_list = [do.split("mul(") for do in do_list]
    do_list = flatten(do_list)
    for mul in do_list:
        nums = mul.split(")")[0].split(',')
        if (len(nums) ==2):
            try:
                # note zouden geen -getallen in moeten zitten
                a = int(nums[0])
                b = int(nums[1])
                if a<1000 and b <1000 and a >=0 and b>=0:
                    som +=  a*b
            except:
                pass

# not: 95786593
# good: 92082041
print(som)