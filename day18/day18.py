droplets = []
with open("input.txt") as f:
    for line in f.read().split("\n"):
        droplets += [tuple(int(i) for i in line.split(","))]


def neighbors(cube):
    return [(cube[0] + 1, cube[1], cube[2]),
            (cube[0], cube[1] + 1, cube[2]),
            (cube[0], cube[1], cube[2] + 1),
            (cube[0] - 1, cube[1], cube[2]),
            (cube[0], cube[1] - 1, cube[2]),
            (cube[0], cube[1], cube[2] - 1)]


sides = 0
for droplet in droplets:
    for adjacent in neighbors(droplet):
        if adjacent not in droplets:
            sides += 1
print(sides)
cube_size = max(max(d[0] for d in droplets), max(d[1] for d in droplets), max(d[2] for d in droplets)) + 1


def bfs(start):
    seen = set()
    queue = []
    seen.add(start)
    queue.append(start)
    while queue:
        position = queue.pop()
        for neighbor in neighbors(position):
            if all(-1 <= p <= cube_size for p in neighbor) and neighbor not in seen and neighbor not in droplets:
                seen.add(neighbor)
                queue.append(neighbor)
    return seen


found = bfs((0, 0, 0))
sides = 0
for droplet in droplets:
    for adjacent in neighbors(droplet):
        if adjacent in found:
            sides += 1
print(sides)
