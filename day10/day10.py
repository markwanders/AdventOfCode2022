with open("input.txt") as f:
    instructions = f.read().split("\n")

x = 1
i = 0
queued = 0
busy = False
signalStrength = 0
for c in range(1, 221):
    if c in [20, 60, 100, 140, 180, 220]:
        signalStrength += c * x
    if not busy:
        instruction = instructions[i].split(" ")
        if instruction[0] == "addx":
            queued = int(instruction[-1])
            busy = True
        i += 1
    else:
        x += queued
        queued = 0
        busy = False
print(signalStrength)
