import re

with open("input.txt") as f:
    maze_input, route = f.read().split("\n\n")

maze = {}
for y, line in enumerate(maze_input.split("\n")):
    for x, char in enumerate(line):
        if char in '.#':
            maze[(x + y * 1j)] = char

direction_value = {1: 0, 1j: 1, -1: 2, -1j: 3}

position = complex(min([x.real for x in [k for (k, v) in maze.items() if v == "."] if x.imag == 0]), 0)
direction = 1

for move in re.split('([RL])', route):
    if move == "R":
        direction *= 1j
    elif move == "L":
        direction *= -1j
    else:
        for _ in range(0, int(move)):
            next = position + direction
            if next not in maze:
                if direction == 1:
                    next = complex(min([p.real for p in maze.keys() if p.imag == next.imag]), next.imag)
                elif direction == -1:
                    next = complex(max([p.real for p in maze.keys() if p.imag == next.imag]), next.imag)
                elif direction == -1j:
                    next = complex(next.real, max([p.imag for p in maze.keys() if p.real == next.real]))
                elif direction == 1j:
                    next = complex(next.real, min([p.imag for p in maze.keys() if p.real == next.real]))
            if maze[next] == ".":
                position = next
print(int(1000 * position.imag + 4 * position.real + direction_value[direction]))

position = complex(min([x.real for x in [k for (k, v) in maze.items() if v == "."] if x.imag == 0]), 0)
direction = 1


def wrap(p, d):
    x, y = p.real, p.imag
    if d == 1:
        if y//50 == 0:  # B -> E
            return complex(99, 149 - y), -1
        elif y//50 == 1:  # C -> B
            return complex(50 + y, 49), -1j
        elif y//50 == 2:  # E -> B
            return complex(149, 149 - y), -1
        elif y//50 == 3:  # F -> E
            return complex(y - 100, 149), -1j
    elif d == -1:
        if y//50 == 0:  # A -> D
            return complex(0, 149 - y), 1
        elif y//50 == 1:  # C -> D
            return complex(y - 50, 100), 1j
        elif y//50 == 2:  # D -> A
            return complex(50, 149 - y), 1
        elif y//50 == 3:  # F -> A
            return complex(y - 100, 0), 1j
    elif d == -1j:
        if x//50 == 0:  # D -> C
            return complex(50, 50 + x), 1
        elif x//50 == 1:  # A -> F
            return complex(0, x + 100), 1
        elif x//50 == 2:  # B -> F
            return complex(x - 100, 199), -1j
    elif d == 1j:
        if x//50 == 0:  # F -> B
            return complex(x + 100, 0), 1j
        elif x//50 == 1:  # E -> F
            return complex(49, x + 100), -1
        elif x//50 == 2:  # B -> C
            return complex(99, x - 50), -1


for move in re.split('([RL])', route):
    if move == "R":
        direction *= 1j
    elif move == "L":
        direction *= -1j
    else:
        for _ in range(0, int(move)):
            next, new_direction = position + direction, direction
            if next not in maze:
                next, new_direction = wrap(next, direction)
            if maze[next] == ".":
                position, direction = next, new_direction
print(int(1000 * position.imag + 4 * position.real + direction_value[direction]))
