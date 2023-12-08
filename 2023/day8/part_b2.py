file_name = "/Users/swaab/Documents/GIT-Projects/AoC/2023/day8/input.txt"

def run():
    with open(file_name) as f:
        lines = f.readlines()
        instruction = lines[0]
        d = {}
        start_keys = []
        for line in lines[2:]:
            node, l, r = [w.strip() for w in line.replace("= (",",").replace(")","").replace(" ","").split(",")]
            d[node] = [l, r]
            if "A" == node[2]:
                start_keys.append(node)

        l =[]
        for result in start_keys:
            idx = 0
            while not result[2]=="Z":
                i = idx % (len(instruction)-1)
                action = instruction[i]
                action_idx = 1 if action == 'R'else 0
                result = d[result][action_idx]
                idx += 1
            l.append(idx)
        print(f'use : "https://www.calculatorsoup.com/calculators/math/lcm.php" \n'
          f'for the result numbers {l}')
        
run()