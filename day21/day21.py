from sympy import sympify, solve
monkeys = [line.split(": ") for line in open("input.txt").read().split("\n")]

monkey_nums = {m[0]: int(m[-1]) for m in monkeys if " " not in m[-1]}

while len(monkey_nums.keys()) < len(monkeys):
    for monkey, job in [m for m in monkeys if m[0] not in monkey_nums.keys()]:
        m1, op, m2 = job.split(" ")
        if m1 in monkey_nums.keys() and m2 in monkey_nums.keys():
            if op == "+":
                monkey_nums[monkey] = int(monkey_nums[m1] + monkey_nums[m2])
            elif op == "-":
                monkey_nums[monkey] = monkey_nums[m1] - monkey_nums[m2]
            elif op == "/":
                monkey_nums[monkey] = monkey_nums[m1] // monkey_nums[m2]
            elif op == "*":
                monkey_nums[monkey] = monkey_nums[m1] * monkey_nums[m2]
print(monkey_nums["root"])


def reduce(monkey):
    job = [m for m in monkeys if m[0] == monkey][-1][-1]
    if " " in job:
        m1, op, m2 = job.split(" ")
        if monkey == "root":
            op = "=="
        eq = "(" + str(reduce(m1)) + op + str(reduce(m2)) + ")"
        if "x" not in eq:
            return int(eval(eq))
        else:
            return eq
    else:
        if monkey == "humn":
            return "x"
        return job


equation = reduce("root")
sympy_eq = sympify("Eq" + equation.replace("==", ","))
print(solve(sympy_eq))
