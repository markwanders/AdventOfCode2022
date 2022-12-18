shapes = [[0, 1, 2, 3],
          [0 + 1j, 1 + 1j, 2 + 1j, 1, 1 + 2j],
          [0, 1, 2, 2 + 1j, 2 + 2j],
          [0, 1j, 2j, 3j],
          [0, 1, 1j, 1 + 1j]]

with open("input.txt") as f:
    pattern = f.readline()

i = 1
j = 0
blocked = [x for x in range(0, 8)]


def disp(grid):
    for y in range(3 + int(max(b.imag for b in grid)), -1, -1):
        line = ""
        for x in range(0, 7):
            if complex(x, y) in grid:
                line += "#"
            else:
                line += "."
        print(line)


seen = {}
additional = 0
while i < 1000000000000:
    p = (i % len(shapes)) - 1
    height = max(b.imag for b in blocked)
    shape = [s + complex(2, 4 + height) for s in shapes[p]]
    rest = False
    while all(s not in blocked for s in shape) and not rest:
        j += 1
        w = (j % len(pattern)) - 1
        jet = pattern[w]
        if jet == '>' and max(s.real for s in shape) < 6:
            right = [s + 1 for s in shape]
            if all(r not in blocked for r in right):
                shape = right
        elif jet == '<' and min(s.real for s in shape) > 0:
            left = [s - 1 for s in shape]
            if all(r not in blocked for r in left):
                shape = left
        down = [s - 1j for s in shape]
        if all(d not in blocked for d in down):
            shape = down
        else:
            rest = True
    blocked += shape
    state = (str([complex(b.real, height - b.imag) for b in blocked[-10:]]), p, w)
    if state in seen:
        old_i, old_height = seen[state]
        repeat = (1000000000000 - i) // (i - old_i)
        i += (i - old_i) * repeat
        additional += repeat * (height - old_height)
    else:
        seen[state] = (i, height)
    i += 1
print(max(b.imag for b in blocked) + additional + 2)
