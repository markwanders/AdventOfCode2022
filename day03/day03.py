with open("input.txt") as f:
    rucksacks = f.read().splitlines()

priority = 0
for rucksack in rucksacks:
    c1, c2 = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]
    shared = "".join(set(c1) & set(c2))
    if shared.islower():
        priority += ord(shared) - ord('a') + 1
    else:
        priority += ord(shared) - ord('A') + 27
print(priority)
priority = 0
for i in range(0, len(rucksacks), 3):
    group = rucksacks[i:i+3]
    shared = "".join(set(group[0]) & set(group[1]) & set(group[2]))
    if shared.islower():
        priority += ord(shared) - ord('a') + 1
    else:
        priority += ord(shared) - ord('A') + 27
print(priority)
