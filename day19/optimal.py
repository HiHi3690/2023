import re

maps, parts = [x for x in open("test.txt").read().strip().split("\n\n")]

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

