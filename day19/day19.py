import re


class State:
    def __init__(self, t, ore, ore_bots, clay=0, clay_bots=0, obsidian=0, obsidian_bots=0, geode=0, geode_bots=0):
        self.t = t
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode
        self.ore_bots = ore_bots
        self.clay_bots = clay_bots
        self.obsidian_bots = obsidian_bots
        self.geode_bots = geode_bots

    def __repr__(self):
        return "t: {t}, ore: {ore}, clay: {clay}, obsidian: {obsidian}, geode: {geode}, ore bots: {ore_bots}, " \
               "clay bots: {clay_bots}, obsidian bots: {obsidian_bots}, geode bots: {geode_bots}" \
            .format(t=self.t, ore=self.ore, clay=self.clay, obsidian=self.obsidian, geode=self.geode,
                    ore_bots=self.ore_bots, clay_bots=self.clay_bots, obsidian_bots=self.obsidian_bots,
                    geode_bots=self.geode_bots)

    def key(self):
        return self.t, self.ore, self.ore_bots, self.clay, self.clay_bots, self.obsidian, self.obsidian_bots, self.geode_bots


class Blueprint:
    def __init__(self, id, ore, clay, obsidian, geode):
        self.id = id
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode
        self.cache = {}

    def __repr__(self):
        return "id: {id}, ore cost: {ore}, clay cost: {clay}, obsidian cost: {obsidian}, geode cost: {geode}" \
            .format(id=self.id, ore=self.ore, clay=self.clay, obsidian=self.obsidian, geode=self.geode)

    def max_ore_cost(self):
        return max(self.ore, self.clay, self.obsidian[0], self.geode[0])

    def max_clay_cost(self):
        return self.obsidian[1]

    def max_obsidian_cost(self):
        return self.geode[1]


blueprints = []

with open("input.txt") as f:
    for line in f.read().split("\n"):
        nums = [int(i) for i in re.findall(r'\d+', line)]
        blueprints.append(Blueprint(nums[0], nums[1], nums[2], nums[3:5], nums[5:]))


def build_nothing(s):
    return State(s.t - 1,
                 s.ore + s.ore_bots,
                 s.ore_bots,
                 s.clay + s.clay_bots,
                 s.clay_bots,
                 s.obsidian + s.obsidian_bots,
                 s.obsidian_bots,
                 s.geode + s.geode_bots,
                 s.geode_bots)


def build_ore_bot(s, b):
    return State(s.t - 1,
                 s.ore + s.ore_bots - b.ore,
                 s.ore_bots + 1,
                 s.clay + s.clay_bots,
                 s.clay_bots,
                 s.obsidian + s.obsidian_bots,
                 s.obsidian_bots,
                 s.geode + s.geode_bots,
                 s.geode_bots)


def build_clay_bot(s, b):
    return State(s.t - 1,
                 s.ore + s.ore_bots - b.clay,
                 s.ore_bots,
                 s.clay + s.clay_bots,
                 s.clay_bots + 1,
                 s.obsidian + s.obsidian_bots,
                 s.obsidian_bots,
                 s.geode + s.geode_bots,
                 s.geode_bots)


def build_obsidian_bot(s, b):
    return State(s.t - 1,
                 s.ore + s.ore_bots - b.obsidian[0],
                 s.ore_bots,
                 s.clay + s.clay_bots - b.obsidian[1],
                 s.clay_bots,
                 s.obsidian + s.obsidian_bots,
                 s.obsidian_bots + 1,
                 s.geode + s.geode_bots,
                 s.geode_bots)


def build_geode_bot(s, b):
    return State(s.t - 1,
                 s.ore + s.ore_bots - b.geode[0],
                 s.ore_bots,
                 s.clay + s.clay_bots,
                 s.clay_bots,
                 s.obsidian + s.obsidian_bots - b.geode[1],
                 s.obsidian_bots,
                 s.geode + s.geode_bots,
                 s.geode_bots + 1)


def dfs(state, blueprint):
    if state.t == 0:
        return state.geode
    if state.key() in blueprint.cache.keys():
        return blueprint.cache[state.key()]
    geodes = 0
    if state.t > 1:
        # always build geode bot if possible
        if state.ore >= blueprint.geode[0] and state.obsidian >= blueprint.geode[1]:
            new_state = build_geode_bot(state, blueprint)
            return dfs(new_state, blueprint)
        # build obsidian bot if obsidian/turn < max obsidian cost
        if state.ore >= blueprint.obsidian[0] and state.clay >= blueprint.obsidian[1] \
                and state.obsidian_bots < blueprint.max_obsidian_cost():
            new_state = build_obsidian_bot(state, blueprint)
            geodes = max(geodes, dfs(new_state, blueprint))
        # build clay bot if clay/turn < max clay cost
        if state.ore >= blueprint.clay and state.clay_bots < blueprint.max_clay_cost():
            new_state = build_clay_bot(state, blueprint)
            geodes = max(geodes, dfs(new_state, blueprint))
        # build ore bot if ore/turn < max ore cost
        if state.ore >= blueprint.ore and state.ore_bots < blueprint.max_ore_cost():
            new_state = build_ore_bot(state, blueprint)
            geodes = max(geodes, dfs(new_state, blueprint))
    new_state = build_nothing(state)
    geodes = max(geodes, dfs(new_state, blueprint))
    blueprint.cache[state.key()] = geodes
    return geodes


ans = 0
for bp in blueprints:
    max_geodes = dfs(State(24, 0, 1), bp)
    ans += bp.id * max_geodes
print(ans)

ans = 1
for bp in blueprints[:3]:
    max_geodes = dfs(State(32, 0, 1), bp)
    ans *= max_geodes
print(ans)
