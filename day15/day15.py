import re


def manhattan(a, b):
    return abs(a.real - b.real) + abs(a.imag - b.imag)


sensors = {}
with open('input.txt') as f:
    lines = f.read().split("\n")
    for line in lines:
        parts = [[int(j) for j in i] for i in re.findall(r'x=(-?\d+), y=(-?\d+)', line)]
        sensors[complex(parts[0][0], parts[0][1])] = complex(parts[1][0], parts[1][1])
counter = 0
for x in range(-10000000, 10000000):
    t = complex(x, 2000000)
    if t in sensors.keys() or t in sensors.values():
        continue
    if any([manhattan(s, t) <= manhattan(b, s) for s, b in sensors.items()]):
        counter += 1
print(counter)
