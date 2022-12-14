class Node:
    def __init__(self, xy, d):
        self.xy = xy
        self.d = d


grid = {}
start, end = 0, 0


def adjacent_nodes(n):
    return [xy for xy in [n.xy + s for s in [1+0j, -1 + 0j, 1j, -1j]] if xy in grid.keys() and ord(grid[xy]) <= ord(grid[n.xy]) + 1]


with open("input.txt") as f:
    for y, line in enumerate(f.read().split("\n")):
        for x, c in enumerate(line):
            xy = complex(x, y)
            if c == 'S':
                start = xy
                grid[xy] = 'a'
            elif c == 'E':
                end = xy
                grid[xy] = 'z'
            else:
                grid[xy] = c

queue = [Node(start, 0)]
visited = set()
distances = {start: 0}
while queue:
    node = queue.pop(0)
    visited.add(node.xy)
    for adjacent in adjacent_nodes(node):
        print(adjacent)
        if adjacent in visited:
            continue
        newDistance = node.d + 1
        if adjacent not in distances.keys() or distances[adjacent] > newDistance:
            queue.append(Node(adjacent, newDistance))
            distances[adjacent] = newDistance
            queue.sort(key=lambda q: q.d)
print(distances[end])
