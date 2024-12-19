file_name = "C:/Users/danie/Documents/repos/2024/day13/input.txt"
import re


class Claw:

    def __init__(self, s):
        n = re.findall(r"\d+", s)

        self.x = int(n[0])
        self.y = int(n[1])

    def __str__(self):
        return f"Button : X={self.x}, Y={self.y}"


class Machine:

    def __init__(self, s: []):
        self.A = Claw(s[0])
        self.B = Claw(s[1])
        n = re.findall(r"\d+", s[2])
        self.x = int(n[0])
        self.y = int(n[1])

    def __str__(self):
        return f"A {self.A} \nB {self.B} \nPrize: X={self.x}, Y={self.y}"


with open(file_name) as f:
    lines = f.readlines()
    machines = [Machine(lines[i * 4 : (i + 1) * 4]) for i in range(int(len(lines) / 4))]

    max_presses = 100

    som = 0
    for machine in machines:
        print(machine, "\n")
        d = set()
        count = 0
        for i in range(max_presses):  # A (x3)
            for j in range(max_presses):  # B (x1)
                pos_x = machine.A.x * i + machine.B.x * j
                pos_y = machine.A.y * i + machine.B.y * j
                if pos_x == machine.x and pos_y == machine.y:
                    cost = i * 3 + j
                    d.add(cost)
                    count += 1
        print(count)
        try:
            som += min(d)
        except:
            print("not possible \n")

    print(som)
