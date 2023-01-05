import re

with open("input.txt") as f:
    maze_input, route = f.read().split("\n\n")

maze = {}
for y, line in enumerate(maze_input.split("\n")):
    for x, char in enumerate(line):
        if char != " ":
            maze[(complex(x + 1, y + 1))] = char

direction_value = {1: 0, 1j: 1, -1: 2, -1j: 3}

position = complex(min([x.real for x in [k for (k, v) in maze.items() if v == "."] if x.imag == 1]), 1)
direction = 1

for move in re.split('([RL])', route):
    if move == "R":
        if direction == 1j:
            direction = -1
        elif direction == -1j:
            direction = 1
        elif direction == -1:
            direction = -1j
        elif direction == 1:
            direction = 1j
    elif move == "L":
        if direction == 1j:
            direction = 1
        elif direction == -1j:
            direction = -1
        elif direction == -1:
            direction = 1j
        elif direction == 1:
            direction = -1j
    else:
        for i in range(0, int(move)):
            next = position + direction
            if next not in maze.keys():
                if direction == 1:
                    next = complex(min([p.real for p in maze.keys() if p.imag == next.imag]), next.imag)
                elif direction == -1:
                    next = complex(max([p.real for p in maze.keys() if p.imag == next.imag]), next.imag)
                elif direction == -1j:
                    next = complex(next.real, max([p.imag for p in maze.keys() if p.real == next.real]))
                elif direction == 1j:
                    next = complex(next.real, min([p.imag for p in maze.keys() if p.real == next.real]))
            if maze[next] == "#":
                break
            else:
                position = next
print(int(1000 * position.imag + 4 * position.real + direction_value[direction]))

position = complex(min([x.real for x in [k for (k, v) in maze.items() if v == "."] if x.imag == 1]), 1)
direction = 1

for move in re.split('([RL])', route):
    if move == "R":
        if direction == 1j:
            direction = -1
        elif direction == -1j:
            direction = 1
        elif direction == -1:
            direction = -1j
        elif direction == 1:
            direction = 1j
    elif move == "L":
        if direction == 1j:
            direction = 1
        elif direction == -1j:
            direction = -1
        elif direction == -1:
            direction = 1j
        elif direction == 1:
            direction = -1j
    else:
        for i in range(0, int(move)):
            next = position + direction
            new_direction = direction
            if next not in maze.keys():
                if direction == 1:
                    if 1 <= position.imag <= 50:  # B -> E
                        new_direction = -1
                        next = complex(100, 151 - position.imag)
                    elif 100 >= position.imag >= 51:  # C -> B
                        new_direction = -1j
                        next = complex(50 + position.imag, 50)
                    elif 150 >= position.imag >= 101:  # E -> B
                        new_direction = -1
                        next = complex(150, 151 - position.imag)
                    elif 200 >= position.imag >= 150:  # F -> E
                        new_direction = -1j
                        next = complex(position.imag - 100, 150)
                elif direction == -1:
                    if 1 <= position.imag <= 50:  # A -> D
                        new_direction = 1
                        next = complex(1, 151 - position.imag)
                    elif 100 >= position.imag >= 51:  # C -> D
                        new_direction = 1j
                        next = complex(position.imag - 50, 151)
                    elif 150 >= position.imag >= 101:  # D -> A
                        new_direction = 1
                        next = complex(51, 151 - position.imag)
                    elif 200 >= position.imag >= 151:  # F -> A
                        new_direction = 1j
                        next = complex(position.imag - 100, 1)
                elif direction == -1j:
                    if 1 <= position.real <= 50:  # D -> C
                        new_direction = 1
                        next = complex(51, 50 + position.real)
                    elif 100 >= position.real >= 51:  # A -> F
                        new_direction = 1
                        next = complex(1, position.real + 100)
                    elif 150 >= position.real >= 101:  # B -> F
                        next = complex(position.real - 100, 200)
                elif direction == 1j:
                    if 1 <= position.real <= 50:  # F -> B
                        next = complex(position.real + 100, 1)
                    elif 100 >= position.real >= 51:  # E -> F
                        new_direction = -1
                        next = complex(50, position.real + 100)
                    elif 150 >= position.real >= 101:  # B -> C
                        new_direction = -1
                        next = complex(100, position.real - 50)
            if maze[next] == "#":
                break
            else:
                position = next
                direction = new_direction
print(int(1000 * position.imag + 4 * position.real + direction_value[direction]))
