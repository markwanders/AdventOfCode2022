with open("input.txt") as f:
    lines = f.read().split("\n")

grid = set()


class Blizzard:
    def __init__(self, initial_position, direction):
        self.position = initial_position
        self.direction = direction

    def move(self):
        if self.direction == "<":
            self.position -= 1
            if self.position not in pos:
                self.position = complex(max(p.real for p in pos), self.position.imag)
        elif self.direction == ">":
            self.position += 1
            if self.position not in pos:
                self.position = complex(min(p.real for p in pos), self.position.imag)
        elif self.direction == "^":
            self.position -= 1j
            if self.position not in pos:
                self.position = complex(self.position.real, max(p.imag for p in pos))
        elif self.direction == "v":
            self.position += 1j
            if self.position not in pos:
                self.position = complex(self.position.real, min(p.imag for p in pos))
        return self


blizzards = []
start = 0
finish = 0

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char in ['<', '>', '^', 'v']:
            blizzards.append(Blizzard(complex(x, y), char))
            grid.add(complex(x, y))
        elif char == '.':
            if start == 0:
                start = complex(x, y)
            else:
                finish = complex(x, y)
            grid.add(complex(x, y))

pos = grid - {start, finish}
t = 0
queue = {start}
finished = 0
goal = finish
while finished < 3:
    t += 1
    blizzards = [b.move() for b in blizzards]
    neighbours = {n + d for d in (1, -1, 1j, -1j, 0) for n in queue if n in grid}
    queue = neighbours - {b.position for b in blizzards}
    if goal in queue:
        print(t)
        finished += 1
        queue = {goal}
        if goal == start:
            goal = finish
        else:
            goal = start
