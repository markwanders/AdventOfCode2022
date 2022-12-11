import math
import re

with open("input.txt") as f:
    input = f.read().split("\n\n")


class Monkey:
    def __init__(self, items, operation, test, true, false):
        self.items = items
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false
        self.inspections = 0

    def __repr__(self):
        return str(self.items)

    def do_operation(self, level):
        parts = self.operation.split(" ")
        if parts[0] == "old":
            a = level
        else:
            a = int(parts[0])
        if parts[-1] == "old":
            b = level
        else:
            b = int(parts[-1])
        if parts[1] == "+":
            return a + b
        elif parts[1] == "*":
            return a * b


monkeys = []
for i in input:
    lines = i.split("\n")
    monkey = Monkey(list(map(int, re.findall(r'[0-9]+', lines[1]))),
                    lines[2][19:],
                    int(re.findall(r'[0-9]+', lines[3])[0]),
                    int(re.findall(r'[0-9]+', lines[4])[0]),
                    int(re.findall(r'[0-9]+', lines[5])[0]))
    monkeys.append(monkey)

for _ in range(0, 20):
    for monkey in monkeys:
        while len(monkey.items) > 0:
            level = monkey.items.pop(0)
            monkey.inspections += 1
            level = monkey.do_operation(level)
            level = math.floor(level / 3)
            if level % monkey.test == 0:
                monkeys[monkey.true].items += [level]
            else:
                monkeys[monkey.false].items += [level]
inspections = [m.inspections for m in monkeys]
inspections.sort()
print(inspections[-1] * inspections[-2])
