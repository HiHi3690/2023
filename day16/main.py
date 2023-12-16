import collections

input = [list(x) for x in open("data.txt").read().split("\n")]
m, n = len(input), len(input[0])


directions = {'u': (-1, 0),'d': (1, 0),'r': (0, 1),'l': (0, -1)}
reflections = {'r': {'/': 'u', '\\': 'd'},'l': {'/': 'd', '\\': 'u'},'u': {'/': 'r', '\\': 'l'},'d': {'/': 'l', '\\': 'r'},}

def reflectbeam(beam, i, j, char):
    if char == "-":
        return beam[2] if beam[2] in "rl" else "rl"
    if char == "|":
        return beam[2] if beam[2] in "ud" else "ud"
    return reflections[beam[2]][char]

def countenergy(ii, ji, di):
    beams = [(ii,ji, di)]
    visited = set()
    energized = set()  
    while len(beams) > 0:
        beam = beams.pop()

        i,j = beam[0] + directions[beam[2]][0], beam[1] + directions[beam[2]][1]

        if i>= m or j >= n or i < 0 or j < 0 or beam in visited:
            continue
        visited.add(beam)
        energized.add((i,j))
        if input[i][j] == ".":
            beam = (i, j, beam[2])
            beams.append(beam)
            continue

        for d in reflectbeam(beam, i, j, input[i][j]):
            beam = (i, j, d)
            beams.append(beam)

    return len(energized)

print("s1", countenergy(0, -1, "r"))

max = 0
for ti in range(m):
    d = countenergy(-1, ti, "d")
    max = d if d > max else max
for tj in range(n):
    d = countenergy(tj, -1, "r")
    max = d if d > max else max
    d = countenergy(tj, n, "l")
    max = d if d > max else max

print("s2", max)