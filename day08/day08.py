with open("input.txt") as f:
    grid = f.read().split("\n")
visible = 0
for y, row in enumerate(grid):
    for x, height in enumerate(row):
        if x == 0 or y == 0 or x == len(grid) - 1 or y == len(grid) - 1:
            visible = visible + 1
            continue
        if all(i < int(height) for i in [int(grid[yy][x]) for yy in range(0, y)]) \
                or all(i < int(height) for i in [int(grid[y][xx]) for xx in range(0, x)]) \
                or all(i < int(height) for i in [int(grid[yy][x]) for yy in range(y + 1, len(grid))]) \
                or all(i < int(height) for i in [int(grid[y][xx]) for xx in range(x + 1, len(grid))]):
            visible = visible + 1
print(visible)
