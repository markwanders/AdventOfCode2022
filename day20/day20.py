class Number:

    def __init__(self, value, index):
        self.value = value
        self.index = index

    def __repr__(self):
        return str(self.value)


with open("input.txt") as f:
    nums = [Number(int(n), i) for i, n in enumerate(f.read().split("\n"))]

for num in nums:
    start, finish = num.index, (num.index + num.value) % (len(nums) - 1)
    if finish == 0:
        finish = len(nums) - 1
    # print("Should move %i to from position %i to %i" % (num.value, start, finish))
    nums_to_move = [n for n in nums if n.index in range(min(start, finish), max(start, finish) + 1) and n != num]
    # print(nums_to_move)
    for num_to_move in nums_to_move:
        if start < finish:
            num_to_move.index = num_to_move.index - 1
        else:
            num_to_move.index = num_to_move.index + 1
    num.index = finish
    # print(sorted(nums, key=lambda n: n.index))
    # print([n.index for n in sorted(nums, key=lambda n: n.index)])
index_zero = [n.index for n in nums if n.value == 0][0]
part_1 = 0
for c in range(1000, 4000, 1000):
    c_index = (index_zero + c) % len(nums)
    part_1 += [n.value for n in nums if n.index == c_index][0]
print(part_1)
