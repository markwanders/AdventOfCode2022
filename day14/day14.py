import re

rock = set()
bottom = 0
with open("input.txt") as f:
    for line in f.read().split("\n"):
        paths = [[int(j) for j in i.split(",")] for i in re.findall(r'\d+,\d+', line)]
        for (x1, y1), (x2, y2) in zip(paths, paths[1:]):
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    rock.add(x + y * 1j)
                    bottom = max(bottom, y + 1)


def print_grid():
    for y in range(0, 1 + bottom):
        line = ""
        for x in range(int(min([r.real for r in rock])), 1 + int(max([r.real for r in rock]))):
            if complex(x, y) in rock:
                line += '#'
            elif complex(x, y) in sand:
                line += 'o'
            else:
                line += '.'
        print(line)
    print("\n")


def down(a):
    return a + 1j


def left(a):
    return a + 1j - 1


def right(a):
    return a + 1 + 1j


start = 500 + 0j
sand = set()
limit = False
while not limit:
    next_sand = start
    moved = True
    while moved:
        if next_sand.imag >= bottom:
            print("Part 1: %s" % len(sand))
            moved = False
            limit = True
            break
        if down(next_sand) not in rock and down(next_sand) not in sand:
            next_sand = down(next_sand)
            continue
        if left(next_sand) not in rock and left(next_sand) not in sand:
            next_sand = left(next_sand)
            continue
        if right(next_sand) not in rock and right(next_sand) not in sand:
            next_sand = right(next_sand)
            continue
        else:
            moved = False
    if not limit:
        sand.add(next_sand)
print_grid()
