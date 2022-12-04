with open("input.txt") as f:
    pairs = f.read().splitlines()

counter1 = 0
counter2 = 0
for pair in pairs:
    pair1, pair2, = [[int(x.split("-")[0]), int(x.split("-")[-1])] for x in pair.split(",")]
    if (pair1[0] >= pair2[0] and pair1[-1] <= pair2[-1]) or (pair2[0] >= pair1[0] and pair2[-1] <= pair1[-1]):
        counter1 += 1
    if pair2[0] <= pair1[0] <= pair2[-1] or pair2[0] <= pair1[-1] <= pair2[-1] or pair1[0] <= pair2[0] <= pair1[-1] or pair1[0] <= pair2[-1] <= pair1[-1]:
        counter2 += 1
print(counter1)
print(counter2)
