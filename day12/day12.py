class Node:
    def __init__(self, xy, d):
        self.xy = xy
        self.d = d


grid = {}
start, end = 0, 0
starts = []

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
            elif c == 'a':
                starts.append(xy)
                grid[xy] = c
            else:
                grid[xy] = c


def adjacent_nodes(n):
    return [xy for xy in [n.xy + s for s in [1+0j, -1 + 0j, 1j, -1j]] if xy in grid.keys() and ord(grid[xy]) <= ord(grid[n.xy]) + 1]


def path(starting_nodes):
    queue = []
    distances = {}
    visited = set()
    for starting_node in starting_nodes:
        queue.append(Node(starting_node, 0))
        distances[starting_node] = 0
    while queue:
        node = queue.pop(0)
        visited.add(node.xy)
        for adjacent in adjacent_nodes(node):
            if adjacent in visited:
                continue
            new_distance = node.d + 1
            if adjacent not in distances.keys() or distances[adjacent] > new_distance:
                queue.append(Node(adjacent, new_distance))
                distances[adjacent] = new_distance
                queue.sort(key=lambda q: q.d)
    return distances.get(end, float('inf'))


print(path([start]))
print(min([p for p in [path(starts)]]))
