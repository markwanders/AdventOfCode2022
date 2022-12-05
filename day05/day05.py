import re

with open("input.txt") as f:
    crates, moves, = f.read().split("\n\n")
    crates = crates.split("\n")
    moves = moves.split("\n")

stacks1 = [[]] * 9
stacks2 = [[]] * 9
for crate in crates:
    row = [crate[i:i+4] for i in range(0, len(crate), 4)]
    for i, c in enumerate(row):
        if '[' in c:
            stacks1[i] = [c[1]] + stacks1[i]
            stacks2[i] = [c[1]] + stacks2[i]
print(stacks1)
for move in moves:
    n, s, t = map(int, re.findall(r'\d+', move))
    print(n, s, t)
    for i in range(n):
        stacks1[t - 1] = stacks1[t - 1] + [stacks1[s - 1].pop()]
    stacks2[t - 1] = stacks2[t - 1] + stacks2[s - 1][-n:]
    stacks2[s - 1] = stacks2[s - 1][:-n]

print("".join([s for s in [(stack or [None])[-1] for stack in stacks1] if s is not None]))
print("".join([s for s in [(stack or [None])[-1] for stack in stacks2] if s is not None]))
print(stacks2)
