file_name = "/Users/swaab/Documents/GIT-Projects/AoC/2023/day8/input.txt"

def run():
    with open(file_name) as f:
        lines = f.readlines()
        instruction = lines[0]
        d = {}
        start_keys = []
        end_keys = []
        for line in lines[2:]:
            node, l, r = [w.strip() for w in line.replace("= (",",").replace(")","").replace(" ","").split(",")]
            d[node] = [l, r]
            if "A" == node[2]:
                start_keys.append(node)
            elif "Z" == node[2]:
                end_keys.append(node)

        idx = 0
        new_run = False
        sum=1
        for reps in start_keys:
            results=[reps]
            count=0
            while not all([r[2]=="Z" for r in results]) or new_run:
                new_run = False
                i = idx % (len(instruction)-1)
                action = instruction[i]
                action_idx = 1 if action == 'R'else 0
                for r_i, result in enumerate(results):
                    results[r_i] = d[result][action_idx]
                idx += 1
                count+=1
            print(count)
            sum*=count
            # print(idx)
            new_run=True
        print(sum)

run()