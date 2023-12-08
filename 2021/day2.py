file_name = 'input/input.txt'

from enum import Enum, unique

@unique
class Move(Enum):
    forward = 'forward'
    down = 'down'
    up = 'up'

class Route:

    depth = 0
    horizontal = 0
    aim = 0

    def move(self, movement):
        if movement.type == Move.up.value:
            self.aim -= movement.amount
        elif movement.type == Move.down.value:
            self.aim += movement.amount
        elif movement.type == Move.forward.value:
            self.horizontal += movement.amount
            self.depth += self.aim * movement.amount

class Movement:

    def __init__(self, type, amount):
        self.type = type
        self.amount = amount

    def __str__(self):
        return "{}-{}".format(self.type, self.amount)

def cleanup_input_line(i):
    type, amount = i.strip('\n').split(' ')
    return type, int(amount)

with open(file_name) as f:
    lines = f.readlines()
    moves = [Movement(*cleanup_input_line(i)) for i in lines]
    print(moves)
    print(moves[0].type)
    print(moves[0].amount)
    print(moves[0])

    r = Route()
    for move in moves:
        r.move(move)

    print("{}-{}".format(r.depth,r.horizontal))
    print(r.depth*r.horizontal)


print(Move.forward.value)