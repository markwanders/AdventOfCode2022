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


def solve(part2=False):
    modulo = 1
    monkeys = []
    for i in input:
        lines = i.split("\n")
        test = int(re.findall(r'\d+', lines[3])[0])
        modulo *= test
        monkey = Monkey(list(map(int, re.findall(r'\d+', lines[1]))),
                        lines[2][19:],
                        test,
                        int(re.findall(r'\d+', lines[4])[0]),
                        int(re.findall(r'\d+', lines[5])[0]))
        monkeys.append(monkey)

    if part2:
        rounds = 10000
    else:
        rounds = 20
    for _ in range(0, rounds):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                level = monkey.items.pop(0)
                monkey.inspections += 1
                level = monkey.do_operation(level)
                if part2:
                    level = level % modulo
                else:
                    level = math.floor(level / 3)
                if level % monkey.test == 0:
                    monkeys[monkey.true].items += [level]
                else:
                    monkeys[monkey.false].items += [level]
    inspections = [m.inspections for m in monkeys]
    inspections.sort()
    print(inspections[-1] * inspections[-2])


solve()
solve(part2=True)
