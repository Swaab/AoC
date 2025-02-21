file_name = "C:/Users/danie/Documents/repos/2024/day24/input.txt"


class Line:

    def __init__(self, id, state):
        self.id = id
        # self.ins = ins
        # self.outs = outs
        self.state = state

    def __str__(self):
        return f"{self.id}: {self.state}"


class Gate:

    def __init__(self, op, l1: Line, l2: Line, out: Line):
        self.op = op
        self.l1 = l1
        self.l2 = l2
        self.out = out
        self.state = None

    def ready(self):
        return self.l1.state is not None and self.l2.state is not None

    def AND(self):
        print(
            f"AND compare: {self.l1.state} and {self.l2.state} -> {self.l1.state and self.l2.state}"
        )
        return self.l1.state and self.l2.state

    def XOR(self):
        print(
            f"XOR compare: {self.l1.state} and {self.l2.state} -> {self.l1.state != self.l2.state}"
        )
        return self.l1.state != self.l2.state

    def OR(self):
        print(
            f"OR compare: {self.l1.state} and {self.l2.state} -> {self.l1.state or self.l2.state}"
        )
        return self.l1.state or self.l2.state

    def activate(self):
        if self.out.state is None and self.ready():
            output = None
            if self.op == "AND":
                output = self.AND()
            elif self.op == "OR":
                output = self.OR()
            elif self.op == "XOR":
                output = self.XOR()
            else:
                print("shouldnt come here")
            self.out.state = bool(output)

    def __str__(self):
        return f"[{self.l1}] {self.op} [{self.l2}] -> {self.out}"


class Grid:

    def __init__(self):
        self.wires = {}
        self.gates = []
        self.z_lines = []

    def get_wire(self, info):
        if ":" in info:
            id, state = info.split(": ")
            state = bool(int(state))
        else:
            id = info
            state = None

        if id in self.wires:
            return self.wires[id]
        else:
            wire = Line(id, state)
            self.wires[id] = wire
            if id[0] == "z":
                self.z_lines.append(wire)
            return wire

    def add_gate(self, oper, wire1, wire2, out):
        self.gates.append(Gate(oper, wire1, wire2, out))

    def finished(self):
        return all([True if wire.state is not None else False for wire in self.z_lines])

    def run(self):
        while not self.finished():
            for gate in self.gates:
                gate.activate()

    def binairy(self):
        self.z_lines.sort(key=lambda x: x.id, reverse=True)

        for wire in self.z_lines:
            print(wire)
        return [1 if wire.state else 0 for wire in self.z_lines]


with open(file_name) as f:
    lines = f.readlines()
    grid = Grid()
    init = True
    for line in lines:
        line = line.strip()
        if init:
            if line == "":
                init = False
            else:
                grid.get_wire(line)
        else:
            gate_info = line.split("->")
            ins = gate_info[0].strip().split(" ")

            wire1 = grid.get_wire(ins[0])
            wire2 = grid.get_wire(ins[2])
            operation = ins[1]

            out = grid.get_wire(gate_info[1].strip())
            grid.add_gate(operation, wire1, wire2, out)

    grid.run()
    b = grid.binairy()

    res = int("".join(str(x) for x in b), 2)
    print(res)
