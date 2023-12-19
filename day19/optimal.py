import re

maps, parts = [x for x in open("data.txt").read().strip().split("\n\n")]

parts = [[int(y) for y in re.sub("[{}xmas=]", "", x).split(",")] for x in parts.split("\n")]
maps = {l.split("{")[0]: l.split("{")[1][:-1] for l in maps.split("\n")}

def evalPart(part, map):
    map = maps[map]
    x, m, a, s = part
    for cond in map.split(","):
        if cond == "R":
            return False
        if cond == "A":
            return True
        if ":" not in cond:
            return evalPart(part, cond)
        check = cond.split(":")[0] #get first cond
        if eval(check):
            if cond.split(":")[1] == "R":
                return False
            if cond.split(":")[1] == "A":
                return True
            return evalPart(part, cond.split(":")[1])

tot = 0
for p in parts:
    if evalPart(p, "in"):
        tot += sum(p)

print("s1", tot)

def both(character: str, greaterThan: bool, val: int, ranges):
	character = 'xmas'.index(character)
	ranges2 = []
	for rng in ranges:
		rng = list(rng)
		lo, hi = rng[character]
		if greaterThan:
			lo = max(lo, val + 1)
		else:
			hi = min(hi, val - 1)
		if lo > hi:
			continue
		rng[character] = (lo, hi)
		ranges2.append(tuple(rng))
	return ranges2


def acceptance_ranges_outer(map):
	return acceptance_ranges_inner(maps[map].split(","))

def acceptance_ranges_inner(map):
	rawCond = map[0]
	if rawCond == "R":
		return []
	if rawCond == "A":
		return [((1, 4000), (1, 4000), (1, 4000), (1, 4000))]
	if ":" not in rawCond:
		return acceptance_ranges_outer(rawCond)
	cond = rawCond.split(":")[0]
	greaterThan = ">" in cond
	character = cond[0]
	val = int(cond[2:])
	val_inverted = val + 1 if greaterThan else val - 1
	if_cond_is_true = both(character, greaterThan, val, acceptance_ranges_inner([rawCond.split(":")[1]]))
	if_cond_is_false = both(character, not greaterThan, val_inverted, acceptance_ranges_inner(map[1:]))
	return if_cond_is_true + if_cond_is_false

tot = 0
for rng in acceptance_ranges_outer('in'):
	v = 1
	for lo, hi in rng:
		v *= hi - lo + 1
	tot += v
print("s2", tot)