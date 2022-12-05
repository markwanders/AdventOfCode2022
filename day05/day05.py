import re

with open("input.txt") as f:
    crates, moves, = f.read().split("\n\n")
    crates = crates.split("\n")
    moves = moves.split("\n")

stacks = [[]] * 9
for crate in crates:
    row = [crate[i:i+4] for i in range(0, len(crate), 4)]
    for i, c in enumerate(row):
        if '[' in c:
            stacks[i] = [c[1]] + stacks[i]
print(stacks)
for move in moves:
    n, s, t = map(int, re.findall(r'\d+', move))
    print(n, s, t)
    for i in range(n):
        stacks[t - 1] = stacks[t - 1] + [stacks[s - 1].pop()]
print("".join([s for s in [(stack or [None])[-1] for stack in stacks] if s is not None]))
