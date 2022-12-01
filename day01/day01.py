with open("input.txt") as f:
    elves = f.read().split("\n\n")

calories = []
for elf in elves:
    calories.append(sum([int(i) for i in elf.split("\n")]))

calories.sort()
print(calories[-1])
print(sum(calories[-3:]))
