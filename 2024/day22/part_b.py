import math

file_name = "C:/Users/danie/Documents/repos/2024/day22/input.txt"


def prune(v):
    return v % 16777216


def mix(v, v2):
    return int(bin(v), 2) ^ int(bin(v2), 2)


def next_secret(v: int):
    res = prune(mix(v, v * 64))
    res = prune(mix(res, math.floor(res / 32)))
    res = prune(mix(res, res * 2048))
    return res


with open(file_name) as f:
    lines = f.readlines()

    buyers = [int(line.strip()) for line in lines]

    print(buyers)

    rep = 2000
    res = {}
    for buyer in buyers:
        prices = []
        secret = buyer
        l = []
        secret = next_secret(secret)
        price = secret % 10
        for i in range(rep):
            secret = next_secret(secret)
            new_price = secret % 10
            change = new_price - price
            price = new_price
            l.append(str(change))
            if len(l) > 4:
                l = l[1:5]
            if len(l) == 4:
                key = "".join(l)
                if key in prices:
                    # can only sell once
                    pass
                else:
                    prices.append(key)
                    if key in res:
                        res[key] += new_price
                    else:
                        res[key] = new_price

    m = max(res.values())
    print(m)
    print(list(res.keys())[list(res.values()).index(m)])
