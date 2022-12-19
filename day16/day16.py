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
cache = {}


def dfs2(node, elephant, opened, rate, time):
    if time == 0:
        return 0
    if (rate, time, node, elephant) in cache.keys():
        return cache[(rate, time, node, elephant)]
    released = 0

    node_open = node not in opened and valves[node].flow > 0
    elephant_open = elephant not in opened and valves[elephant].flow > 0 and node != elephant

    if node_open:
        if elephant_open:
            next_opened = opened + [node] + [elephant]
            next_rate = rate + valves[node].flow + valves[elephant].flow
            released = dfs2(node, elephant, next_opened, next_rate, time - 1)
        else:
            next_opened = opened + [node]
            next_rate = rate + valves[node].flow
            for a in valves[elephant].adjacent:
                released = max(released, dfs2(node, a, next_opened, next_rate, time - 1))
    else:
        if elephant_open:
            next_opened = opened + [elephant]
            next_rate = rate + valves[elephant].flow
            for a in valves[node].adjacent:
                released = max(released, dfs2(a, elephant, next_opened, next_rate, time - 1))
    for a in valves[node].adjacent:
        for b in valves[elephant].adjacent:
            released = max(released, dfs2(a, b, opened, rate, time - 1))
    released += rate
    cache[(rate, time, node, elephant)] = released
    return released


print(dfs2("AA", "AA", [], 0, 26))
