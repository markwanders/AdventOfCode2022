with open("input.txt") as f:
    grid = f.read().split("\n")
visible = 0
max_scenic = 0
for y, row in enumerate(grid):
    for x, height in enumerate(row):
        if x == 0 or y == 0 or x == len(grid) - 1 or y == len(grid) - 1:
            visible += 1
            continue
        if all(i < int(height) for i in [int(grid[yy][x]) for yy in range(0, y)]) \
                or all(i < int(height) for i in [int(grid[y][xx]) for xx in range(0, x)]) \
                or all(i < int(height) for i in [int(grid[yy][x]) for yy in range(y + 1, len(grid))]) \
                or all(i < int(height) for i in [int(grid[y][xx]) for xx in range(x + 1, len(grid))]):
            visible += 1
        scenic_l, scenic_r, scenic_u, scenic_d = 0, 0, 0, 0
        left, right, up, down = x - 1, x + 1, y - 1, y + 1
        while left >= 0:
            scenic_l += 1
            if int(grid[y][left]) >= int(height):
                break
            left -= 1
        while right <= len(grid) - 1:
            scenic_r += 1
            if int(grid[y][right]) >= int(height):
                break
            right += 1
        while up >= 0:
            scenic_u += 1
            if int(grid[up][x]) >= int(height):
                break
            up -= 1
        while down <= len(grid) - 1:
            scenic_d += 1
            if int(grid[down][x]) >= int(height):
                break
            down += 1
        max_scenic = max(max_scenic, scenic_l * scenic_r * scenic_u * scenic_d)
print(visible)
print(max_scenic)
