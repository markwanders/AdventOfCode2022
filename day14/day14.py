import re

rock = []
with open("input.txt") as f:
    lines = f.read().split("\n")
    for line in lines:
        paths = [[int(j) for j in i.split(",")] for i in re.findall(r'\d+,\d+', line)]
        for (index, path) in enumerate(paths[:-1]):
            current, next_ = path, paths[index + 1]
            x0, y0 = current
            x1, y1 = next_
            if x0 == x1:
                for y in range(min(y0, y1), max(y0, y1) + 1):
                    rock += [complex(x0, y)]
            if y0 == y1:
                for x in range(min(x0, x1), max(x0, x1) + 1):
                    rock += [complex(x, y0)]
start = 500 + 0j
sand = []
bottom = int(max([r.imag for r in rock]))


def print_grid():
    for y in range(0, 1 + bottom):
        line = ""
        for x in range(int(min([r.real for r in rock])), 1 + int(max([r.real for r in rock]))):
            if complex(x, y) in rock:
                line += '#'
            elif complex(x,y) in sand:
                line += 'o'
            else:
                line += '.'
        print(line)
    print("\n")


def down(a):
    return complex(a.real, a.imag + 1)


def left(a):
    return complex(a.real - 1, a.imag + 1)


def right(a):
    return complex(a.real + 1, a.imag + 1)


limit = False
while not limit:
    next_sand = start
    moved = True
    while moved:
        while down(next_sand) not in rock and down(next_sand) not in sand and down(next_sand).imag < bottom:
            next_sand = down(next_sand)
        if left(next_sand) not in rock and left(next_sand) not in sand:
            if left(next_sand).imag > bottom:
                print("Part 1: %s" % len(sand))
                moved = False
                limit = True
                break
            else:
                next_sand = left(next_sand)
        elif right(next_sand) not in rock and right(next_sand) not in sand:
            if right(next_sand).imag > bottom:
                print("Part 1: %s" % len(sand))
                moved = False
                limit = True
                break
            else:
                next_sand = right(next_sand)
        else:
            moved = False
    if not limit:
        sand += [next_sand]
print_grid()
