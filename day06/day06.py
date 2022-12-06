with open("input.txt") as f:
    stream = f.readline()

for i in range(4, len(stream)):
    buffer = stream[i-4:i]
    if len(set(buffer)) == 4:
        print(i)
        break
for i in range(14, len(stream)):
    buffer = stream[i-14:i]
    if len(set(buffer)) == 14:
        print(i)
        break
