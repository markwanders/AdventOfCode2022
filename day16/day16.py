import re

valves = {}


class Node:
    def __init__(self, t, v, p, o):
        self.t = t
        self.v = v
        self.p = p
        self.o = o

    def __repr__(self):
        return "t:" + str(self.t) + "-v:" + str(self.v) + "-p:" + str(self.p) + "-o:" + str(self.o)

    def __eq__(self, other):
        return self.p == other.p and self.v == other.v and self.o == other.o

    def __hash__(self):
        return hash((self.p, str(self.o), self.v))

    def tick(self):
        self.t += 1
        self.p += sum([valves[v].flow for v in self.o])


class Valve:
    def __init__(self, label, adjacent, flow):
        self.label = label
        self.adjacent = adjacent
        self.flow = flow


with open("input.txt") as f:
    for line in f.read().split("\n"):
        parts = re.findall(r'[A-Z]{2}', line)
        flow = re.findall(r'\d+', line)[0]
        valve = Valve(parts[0], parts[1:], int(flow))
        valves[valve.label] = valve


def adjacent(node):
    adjacent_nodes = []
    if node.t <= 30:
        ad_n = Node(node.t, node.v, node.p, node.o.copy())
        ad_n.tick()
        if node.v not in node.o and valves[node.v].flow > 0:
            ad_n.o.update([node.v])
        adjacent_nodes.append(ad_n)
        for a in valves[node.v].adjacent:
            ad_n = Node(node.t, a, node.p, node.o.copy())
            ad_n.tick()
            adjacent_nodes.append(ad_n)
    return adjacent_nodes


queue = []
visited = set()
queue.append(Node(1, "AA", 0, set()))
while queue:
    queue.sort(key=lambda q: q.p)
    n = queue.pop()
    visited.add(n)
    for adjacent_node in adjacent(n):
        if adjacent_node in visited:
            continue
        queue.append(adjacent_node)
print(max([vis.p for vis in visited]))
