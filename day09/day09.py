with open("input.txt") as f:
    moves = f.read().split("\n")
h, t = 0 + 0j, 0 + 0j
visited = {t}
for move in moves:
    d, s = move.split(" ")
    if d == "L":
        m = (-1 + 0j)
    if d == "R":
        m = (1 + 0j)
    if d == "D":
        m = (0 + 1j)
    if d == "U":
        m = (0 + -1j)
    for _ in range(0, int(s)):
        h += m
        if round(abs(h - t)).imag > 1 or round(abs(h - t)).real > 1:
            t = h - m
            visited.add(t)
print(len(visited))

knots = [0+0j] * 10
visited = {knots[-1]}
for move in moves:
    d, s = move.split(" ")
    if d == "L":
        m = (-1 + 0j)
    if d == "R":
        m = (1 + 0j)
    if d == "D":
        m = (0 + 1j)
    if d == "U":
        m = (0 + -1j)
    for _ in range(0, int(s)):
        knots[0] += m
        for i in range(1, len(knots)):
            t, h = knots[i], knots[i - 1]
            diff = h - t
            dx, dy = abs(diff.real), abs(diff.imag)
            if dx > 1 >= dy:
                knots[i] = complex((h.real + t.real) // 2, h.imag)
            elif dx <= 1 < dy:
                knots[i] = complex(h.real, (h.imag + t.imag) // 2)
            elif dx > 1 and dy > 1:
                knots[i] = complex((h.real + t.real) // 2, (h.imag + t.imag) // 2)
        visited.add(knots[-1])
print(len(visited))
