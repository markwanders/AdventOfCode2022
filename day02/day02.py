with open("input.txt") as f:
    guide = f.readlines()

score = 0
for game in guide:
    p1, p2 = game[0], game[2]
    if p2 == 'X':
        score += 1
        if p1 == 'A':
            score += 3
        if p1 == 'C':
            score += 6
    if p2 == 'Y':
        score += 2
        if p1 == 'A':
            score += 6
        if p1 == 'B':
            score += 3
    if p2 == 'Z':
        score += 3
        if p1 == 'B':
            score += 6
        if p1 == 'C':
            score += 3

print(score)

score = 0
for game in guide:
    p1, p2 = game[0], game[2]
    if p2 == 'X':
        if p1 == 'A':
            score += 3
        if p1 == 'B':
            score += 1
        if p1 == 'C':
            score += 2
    if p2 == 'Y':
        score += 3
        if p1 == 'A':
            score += 1
        if p1 == 'B':
            score += 2
        if p1 == 'C':
            score += 3
    if p2 == 'Z':
        score += 6
        if p1 == 'A':
            score += 2
        if p1 == 'B':
            score += 3
        if p1 == 'C':
            score += 1

print(score)
