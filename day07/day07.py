with open("input.txt") as f:
    lines = f.read().split("\n")

dirs = {}
dir_path = []
for line in lines:
    parts = line.split(" ")
    if parts[0] == "$":
        if parts[1] == "cd":
            if parts[2] == "..":
                dir_path.pop()
            else:
                if parts[2] == "/":
                    pwd = parts[2]
                else:
                    pwd = dir_path[-1] + parts[2] + "/"
                dir_path.append(pwd)
                if pwd not in dirs.keys():
                    dirs[pwd] = 0
    elif parts[0] != "dir":
        size = int(parts[0])
        for d in dir_path:
            dirs[d] = dirs[d] + size
print(sum(v for v in dirs.values() if v <= 100000))
needed_space = 30000000 - (70000000 - max(dirs.values()))
print(min(v for v in dirs.values() if v >= needed_space))
