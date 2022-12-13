import functools

def compare(left, right):
    for L, R in zip(left, right):
        if isinstance(L, int) and isinstance(R, int):
            if L > R:
                return 1
            elif L == R:
                continue
            else:
                return -1
        if isinstance(L, int) and isinstance(R, list):
            L = [L]
        if isinstance(L, list) and isinstance(R, int):
            R = [R]
        nested = compare(L, R)
        if nested == 0:
            continue
        else:
            return nested
    if len(left) > len(right):
        return 1
    elif len(left) == len(right):
        return 0
    else:
        return -1


index = 1
sum = 0
dividers = [[[2]], [[6]]]
with open('input.txt') as f:
    lines = f.readlines()
    a, b = None, None
    for line in lines:
        if line.strip():
            e = eval(line)
            if a is not None:
                b = e
            else:
                a = e
            if a is not None and b is not None:
                dividers.append(a)
                dividers.append(b)
                if compare(a, b) == -1:
                    sum += index
        else:
            index += 1
            a, b = None, None
print(sum)
dividers.sort(key=functools.cmp_to_key(compare))
print((dividers.index([[6]]) + 1) * (1 + dividers.index([[2]])))
