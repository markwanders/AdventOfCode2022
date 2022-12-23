elves = set()
with open("input.txt") as f:
    for y, line in enumerate(f.read().split("\n")):
        for x, char in enumerate(line):
            if char == "#":
                elves.add(complex(x, y))
directions = ['N', 'S', 'W', 'E']


def need_to_move(p):
    surrounding = {p + 1, p + 1 + 1j, p + 1j, p - 1, p - 1 - 1j, p - 1j, p + 1 - 1j, p - 1 + 1j}
    return len(surrounding.intersection(elves)) > 0


def propose_move(d, p):
    if d == 'N':
        if len(elves.intersection({p - 1j, p + 1 - 1j, p - 1 - 1j})) == 0:
            return p - 1j
    elif d == 'S':
        if len(elves.intersection({p + 1j, p + 1 + 1j, p - 1 + 1j})) == 0:
            return p + 1j
    elif d == 'W':
        if len(elves.intersection({p - 1, p - 1 - 1j, p - 1 + 1j})) == 0:
            return p - 1
    elif d == 'E':
        if len(elves.intersection({p + 1, p + 1 - 1j, p + 1 + 1j})) == 0:
            return p + 1


def answer():
    min_y = min(e.imag for e in elves)
    max_y = max(e.imag for e in elves)
    min_x = min(e.real for e in elves)
    max_x = max(e.real for e in elves)
    print((1 + max_x - min_x) * (1 + max_y - min_y) - len(elves))


k = 1
while True:
    proposals = {}
    counter = {}
    for elf in elves:
        if need_to_move(elf):
            for direction in directions:
                proposal = propose_move(direction, elf)
                if proposal:
                    proposals[elf] = proposal
                    if proposal in counter:
                        counter[proposal] += 1
                    else:
                        counter[proposal] = 1
                    break
    directions.append(directions.pop(0))
    can_move = {elf for elf in proposals if counter[proposals[elf]] == 1}
    cant_move = elves - can_move
    elves = cant_move | {proposals[elf] for elf in can_move}
    if not can_move:
        print(k)
        break
    if k == 10:
        answer()
    k += 1
