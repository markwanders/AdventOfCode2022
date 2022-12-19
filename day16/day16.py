import re

valves = {}
cache = {}


class Valve:
    def __init__(self, adjacent, flow):
        self.adjacent = adjacent
        self.flow = flow


with open("input.txt") as f:
    for line in f.read().split("\n"):
        parts = re.findall(r'[A-Z]{2}', line)
        flow = re.findall(r'\d+', line)[0]
        valve = Valve(parts[1:], int(flow))
        valves[parts[0]] = valve


def dfs(node, opened, rate, time):
    if time == 0:
        return 0
    if (rate, time, node) in cache.keys():
        return cache[(rate, time, node)]
    released = 0
    if node not in opened and valves[node].flow > 0:
        next_opened = opened + [node]
        next_rate = rate + valves[node].flow
        released = dfs(node, next_opened, next_rate, time - 1)
    for a in valves[node].adjacent:
        released = max(released, dfs(a, opened, rate, time - 1))
    released += rate
    cache[(rate, time, node)] = released
    return released


print(dfs("AA", [], 0, 30))
