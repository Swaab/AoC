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
    som = 0
    for buyer in buyers:
        secret = buyer
        for i in range(rep):
            secret = next_secret(secret)
            # print(f"{i}: {secret}")

        som += secret

    print(som)
