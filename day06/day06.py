with open("input.txt") as f:
    stream = f.readline()


def solve(size):
    for i in range(size, len(stream)):
        buffer = stream[i - size:i]
        if len(set(buffer)) == size:
            return i


print(solve(4))
print(solve(14))
