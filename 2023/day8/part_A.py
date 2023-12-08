file_name = "/Users/swaab/Documents/GIT-Projects/AoC/2023/day8/input.txt"



def run():
    with open(file_name) as f:
        lines = f.readlines()
        instruction = lines[0]
        d = {}
        for line in lines[2:]:
            node, l, r = [w.strip() for w in line.replace("= (",",").replace(")","").replace(" ","").split(",")]
            d[node] = [l, r]

        idx = 0
        node = "AAA"
        while node !="ZZZ":
            i = idx % (len(instruction)-1)
            action = instruction[i]
            if action == 'R':
                node = d[node][1]
            elif action == 'L':
                node = d[node][0]
            else:
                raise Exception(f"not able to find{action}")
            idx += 1

        print(idx)

run()