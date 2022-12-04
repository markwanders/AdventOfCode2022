import re

with open("input.txt") as f:
    pairs = f.read().splitlines()

counter1 = 0
counter2 = 0
for pair in pairs:
    a, b, c, d, = map(int, re.findall(r'\d+', pair))
    if (a >= c and b <= d) or (c >= a and d <= b):
        counter1 += 1
    if c <= a <= d or c <= b <= d or a <= c <= b or a <= d <= b:
        counter2 += 1
print(counter1)
print(counter2)
