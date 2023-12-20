from math import lcm 
from collections import deque
input = open("data.txt").read().strip().split("\n")


def main(data):
    conjstates = {}
    ffs = {}
    map = {}
    #parse
    for line in data:
        src, dests = line.split(" -> ")
        dests = dests.split(", ")
        match src[0]:
            case "%":
                src = src[1:]
                ffs[src] = False
            case "&":
                src = src[1:]
                conjstates[src] = {}
        map[src] = dests
    for src, dests in map.items():
        for dest in dests:
            if dest in conjstates:
                conjstates[dest][src] = False   
    #part2 var init
    scroots = {'zf': None, 'qx': None, 'cd': None, 'rk': None}
    lengths = []
    lowp = 0
    highp = 0
    for t in range(1,1000000):
        dq = deque([("button", "broadcaster", False)])
        while dq:
            sender, node, pt = dq.popleft()
            #part 1 totals:
            if t <= 1000:
                if pt:
                    highp += 1
                else:
                    lowp += 1
            #part 2 logic
            if not pt and node in scroots:
                prev_t = scroots[node]
                if prev_t is not None:
                    lengths.append(t - prev_t)
                    del scroots[node]
                    if not scroots:
                        return lowp * highp, lcm(*lengths)
                else:
                    scroots[node] = t
            if node == 'rx' and not pt:
                #realllyyy niche, defo not happening
                return t

            if node in ffs:
                if not pt:
                    #update node, ready pulse type
                    pt = ffs[node] = not ffs[node]
                else:
                    continue
            elif node in conjstates:
                #update most recent pulse
                conjstates[node][sender] = pt
                #ready pulse type
                pt = not all(conjstates[node].values())
            for adj in map.get(node, []):
                dq.append((node, adj, pt))
        if t % 10000 == 0:
            print(t)


print(main(input))