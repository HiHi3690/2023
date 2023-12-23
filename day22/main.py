from heapq import *
from timeit import default_timer
start = default_timer()

bricks = [[[int(z) for z in y.split(',')] for y in x.split("~")] for x in open("data.txt").read().split("\n")]

class Brick():
    def __init__(self, start, end, id):
        self.start = start
        self.end = end
        self.x = [x for x in range(start[0], end[0]+1)]
        self.y = [y for y in range(start[1], end[1]+1)]
        self.z = [z for z in range(start[2], end[2]+1)]
        self.id = id

    def equals(self, other):
        return self.z == other.z and self.y == other.y and self.x == other.x

    def get_pos_info(self):
        return self.x, self.y, self.z
    
    def get_info(self):
        return self.x, self.y, self.z, self.id

    def get_bounds(self):
        return self.start, self.end

    def get_id(self):
        return self.id
    
    def get_under(self):
        if len(self.z) == 1:
            if len(self.y) == 1:
                return [(xi, self.y[0], self.z[0] - 1) for xi in self.x]
            return [(self.x[0], yi, self.z[0] - 1) for yi in self.y]
        return [(self.x[0], self.y[0], self.z[0] - 1)]

    def fall(self):
        self.z = [zi-1 for zi in self.z]

    def get_footprint(self):
        if len(self.z) == 1:
            if len(self.y) == 1:
                return len(self.x)
            return len(self.y)
        return 1

#get min/max size of graph
def get_graph_size(blist):
    xr = [100000,0]
    yr = [100000,0]
    zr = [100000,0]
    for i in blist:
        xb, yb, zb = i.get_pos_info()
        for x in xb:
            xr = [x if x<xr[0] else xr[0], x if x > xr[1] else xr[1]]
        for y in yb:
            yr = [y if y<yr[0] else yr[0], y if y > yr[1] else yr[1]]
        for z in zb:
            zr = [z if z<zr[0] else zr[0], z if z > zr[1] else zr[1]]
    return xr, yr, zr

#print graph in z slices
def print_graph(g):
    for z,layer in enumerate(g):
        print("z = ", z)
        for y in layer:
            print(y)

def write_bricks(bs):
    fout = open("bricks.txt", "w")
    for b in bs.values():
        fout.write(str(b.get_info()))
        fout.write("\n")
    fout.close()

def write_graph(g):
    fout = open("graph.txt", "w")
    for z,layer in enumerate(g):
        fout.write("z = "+ str(z) + "\n")
        for y in layer:
            fout.write(str(y) + "\n")
    fout.close

#guess.
def add_brick_to_graph(brick, graph):
    xl, yl, zl, id = brick.get_info()
    for x in xl:
        for y in yl:
            for z in zl:
                graph[z][y][x] = id

#simulates gravity on input graph, returns the output graph and how many bricks moved
def gravity(gin):
    #init output graph
    gout = [[[0 for x in range(len(gin[0][0]))] for y in range(len(gin[0]))] for z in range(len(gin))]
    for y,line in enumerate(gout[0]):
        for x,ch in enumerate(line):
            gout[0][y][x] = -1
    seen = set()
    seen.add(0)
    tbricks = {}
    for z,layer in enumerate(gin[1:]):
        for y,line in enumerate(layer):
            for x, id in enumerate(line):
                if id in seen:
                    continue
                seen.add(id)
               
                s, e = bricks[id].get_bounds()
                tbrick = Brick(s, e, id)
                tbricks.update({id: tbrick})

                under = tbrick.get_under()
                checker = [1 for i in under if gout[i[2]][i[1]][i[0]] == 0]
                if len(checker) != tbrick.get_footprint():
                    add_brick_to_graph(tbrick, gout)
                    continue

                while len(checker) == tbrick.get_footprint():
                    tbrick.fall()
                    tbricks.update({id: tbrick})
                    under = tbrick.get_under()
                    checker = [1 for i in under if gout[i[2]][i[1]][i[0]] == 0]
      
                add_brick_to_graph(tbrick, gout)
    count = []
    for id in tbricks.keys():
        if not bricks[id].equals(tbricks[id]):
            count.append(id)
    return gout, count, tbricks

#yeet a brick from the graph
def zap_brick(gin, pid):
    gout = [[[int(gin[z][y][x]) for x in range(len(gin[0][0]))] for y in range(len(gin[0]))] for z in range(len(gin))]
    xl, yl, zl, id = bricks[pid].get_info()
    for x in xl:
        for y in yl:
            for z in zl:
                gout[z][y][x] = 0
    return gout

#turn bricks from lists to brick objects
for pos,i in enumerate(bricks):
    bricks[pos] = Brick(i[0], i[1], pos+1)

xr, yr, zr = get_graph_size(bricks)

#init graph
graph = [[[0 for x in range(xr[1]+1)] for y in range(yr[1]+1)] for z in range(zr[1]+1)]
for y,line in enumerate(graph[0]):
    for x,ch in enumerate(line):
        graph[0][y][x] = -1

#init brick dict
bricks = {b.get_id():b for b in bricks}

#add bricks to graph
for id in bricks.keys():
    add_brick_to_graph(bricks[id], graph)

# main s1/2 logic
safe = []
mtot = 0
graph, _, outbricks = gravity(graph)
bricks = outbricks

for id in bricks.keys():
    # print(bricks[id].get_info())
    zgraph = zap_brick(graph, id)
    gzgraph, bmoved, _ = gravity(zgraph)
    if zgraph == gzgraph: #s1
        safe.append(id)
    else: #s2
        mtot += len(bmoved)

print(default_timer() - start) #approx 2 mins because I did an unoptimal solution, sorry!
print(len(safe)) #416
print(mtot) #60963
