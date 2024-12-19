file_name = "C:/Users/danie/Documents/repos/2023/day1/input.txt"
import numpy as np

def get_count(l):
    obj = {}
    for item in l:
       if (item in obj):
           obj[item] += 1
       else:
           obj[item] = 1

    return obj


with open(file_name) as f:
    lines = f.readlines()
    list_l = []
    list_r = []
    for line in lines:
        spl = line.split("   ")
        l,r = spl[0],spl[1]
        list_l.append(int(l.strip()))
        list_r.append(int(r.strip()))
    list_r.sort()
    list_l.sort()
    a = np.array(list_l)
    b = np.array(list_r)
    print(np.subtract(a,b).__abs__().sum())


    #  similarity:
    x = get_count(a)
    y = get_count(b)

    som = 0
    for n in x.keys():
        if n in y:
            som += n * x[n] * y[n]


    print(som)