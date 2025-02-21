file_name = "C:/Users/danie/Documents/repos/2024/day23/input.txt"


def find_connections(res, pc):
    count = len(res[pc])
    for connection in res[pc]:
        res[pc] = []
        count += find_connections(res, connection)

    return count


with open(file_name) as f:
    lines = f.readlines()

    connections = [line.strip().split("-") for line in lines]
    res = {}
    for connection in connections:
        left = connection[0]
        right = connection[1]
        print(left, right)
        if left in res:
            res[left].append(right)
        else:
            res[left] = [right]
        if right in res:
            res[right].append(left)
        else:
            res[right] = [left]

    l = set()
    for pc in res.keys():
        if "t" == pc[0]:
            for second in res[pc]:
                for third in res[second]:
                    if third != pc and pc in res[third]:
                        party = [pc, second, third]
                        party.sort()
                        l.add("-".join(party))

    # 2297 - to HIGHT
    print(len(l))
