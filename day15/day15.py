import re


def manhattan(a, b):
    return abs(a.real - b.real) + abs(a.imag - b.imag)


sensors = {}
with open('input.txt') as f:
    lines = f.read().split("\n")
    for line in lines:
        parts = [[int(j) for j in i] for i in re.findall(r'x=(-?\d+), y=(-?\d+)', line)]
        sensors[complex(*parts[0])] = complex(*parts[1])

y = 2000000
excluded = set()
for s, b in sensors.items():
    d = abs(s.imag - y)
    r = manhattan(s, b)
    if d <= r:
        left = int(s.real - (r - d))
        right = int(s.real + (r - d))
        for x in range(left, right + 1):
            if complex(x, y) not in sensors.values():
                excluded.add(x)
print(len(excluded))

for y in range(4000000):
    ranges = []
    if y % 100_000 == 0: print(y)
    for s, b in sensors.items():
        d = abs(s.imag - y)
        r = manhattan(s, b)
        if d <= r:
            left = max(0, int(s.real - (r - d)))
            right = min(int(s.real + (r - d)), 4000000)
            if not ranges:
                ranges.append([left, right])
            else:
                current_range = [left, right]
                for i in range(len(ranges) - 1, -1, -1):
                    if current_range[0] <= ranges[i][1] and ranges[i][0] <= current_range[1]:
                        current_range = [min(current_range[0], ranges[i][0]), max(current_range[1], ranges[i][1])]
                        del ranges[i]
                ranges.append(current_range)
    if ranges[0] != [0, 4000000]:
        print((ranges[0][1] + 1) * 4000000 + y)
        break
