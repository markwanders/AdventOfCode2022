import re


class State:
    def __init__(self, blueprint, t, ore, ore_robots=0, clay=0, clay_robots=0, obsidian=0, obsidian_robots=0, geode=0,
                 geode_robots=0):
        self.blueprint = blueprint
        self.t = t
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode
        self.ore_robots = ore_robots
        self.clay_robots = clay_robots
        self.obsidian_robots = obsidian_robots
        self.geode_robots = geode_robots

    def __repr__(self):
        return "t: {t}, ore: {ore}, clay: {clay}, obsidian: {obsidian}, geode: {geode}" \
                .format(t=self.t, ore=self.ore, clay=self.clay, obsidian=self.obsidian, geode=self.geode)


class Blueprint:
    def __init__(self, id, ore, clay, obsidian, geode):
        self.id = id
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode

    def __repr__(self):
        return "id: {id}, ore cost: {ore}, clay cost: {clay}, obsidian cost: {obsidian}, geode cost: {geode}" \
            .format(id=self.id, ore=self.ore, clay=self.clay, obsidian=self.obsidian, geode=self.geode)


blueprints = []

with open("input.txt") as f:
    for line in f.read().split("\n"):
        nums = [int(i) for i in re.findall(r'\d+', line)]
        blueprints.append(Blueprint(nums[0], nums[1], nums[2], nums[3:5], nums[5:]))

print(blueprints)
cache = {}


def dfs(state):
    print(state)
    if state.t == 24:
        return 0
    if state in cache.keys():
        return cache[state]
    geodes = state.geode
    if state.ore >= state.blueprint.ore:
        new_state = State(state.blueprint,
                          state.t + 1,
                          state.ore + state.ore_robots - state.blueprint.ore,
                          state.ore_robots + 1,
                          state.clay + state.clay_robots,
                          state.clay_robots,
                          state.obsidian + state.obsidian_robots,
                          state.obsidian_robots,
                          state.geode + state.geode_robots,
                          state.geode_robots)
        geodes = max(geodes, dfs(new_state))
    else:
        new_state = State(state.blueprint,
                          state.t + 1,
                          state.ore + state.ore_robots,
                          state.ore_robots,
                          state.clay + state.clay_robots,
                          state.clay_robots,
                          state.obsidian + state.obsidian_robots,
                          state.obsidian_robots,
                          state.geode + state.geode_robots,
                          state.geode_robots)
        geodes = max(geodes, dfs(new_state))
        cache[new_state] = geodes
    return geodes


begin_state = State(blueprints[0], 0, 0, 1)

print(dfs(begin_state))
