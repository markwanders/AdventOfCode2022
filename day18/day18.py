droplets = []
with open("input.txt") as f:
    for line in f.read().split("\n"):
        droplets += [[int(i) for i in line.split(",")]]


def neighbors(cube):
    return [[cube[0] + 1, cube[1], cube[2]],
            [cube[0], cube[1] + 1, cube[2]],
            [cube[0], cube[1], cube[2] + 1],
            [cube[0] - 1, cube[1], cube[2]],
            [cube[0], cube[1] - 1, cube[2]],
            [cube[0], cube[1], cube[2] - 1]]


sides = 0
for droplet in droplets:
    for adjacent in neighbors(droplet):
        if adjacent not in droplets:
            sides += 1
print(sides)
