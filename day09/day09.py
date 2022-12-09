with open("input.txt") as f:
    moves = f.read().split("\n")
h, t = 0 + 0j, 0 + 0j
visited = {(t.real, t.imag)}
for move in moves:
    d, s = move.split(" ")
    if d == "L":
        m = (-1 + 0j)
    if d == "R":
        m = (1 + 0j)
    if d == "D":
        m = (0 + 1j)
    if d == "U":
        m = (0 - 1j)
    for _ in range(0, int(s)):
        h += m
        if round(abs(h - t)).imag > 1 or round(abs(h - t)).real > 1:
            t = h - m
            visited.add((t.real, t.imag))
print(len(visited))
