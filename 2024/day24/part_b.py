file_name = "C:/Users/danie/Documents/repos/2024/day23/input.txt"


def find_connections(res, pc, connections: set):
    connections.add(pc)
    for second in res[pc]:
        for c in connections:
            if c in res[second]:
                pass
            else:
                return connections
        tmp = res.copy()
        tmp[pc] = []
        tmp_connections = connections.copy()
        tmp_connections.add(second)
        others = find_connections(tmp, second, tmp_connections)
        for item in others:
            connections.add(item)
    return connections


def find_connections2(res, pc):
    count = len(res[pc])
    for connection in res[pc]:
        res[pc] = []
        count += find_connections2(res, connection)

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

    result = []
    print(res)
    keys = []
    for pc in res.keys():
        c = find_connections(res.copy(), pc, set())
        print(f"{pc} : {len(c)}, {c}")
        result.append(len(c))
        sl = list(c)
        sl.sort()
        keys.append(",".join(sl))
    # 2297 - to HIGHT
    print(max(result))
    i = result.index(max(result))
    print(keys[i])
