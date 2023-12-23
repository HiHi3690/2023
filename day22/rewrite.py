from heapq import *
from timeit import default_timer
start = default_timer()

bricks = [[[int(z) for z in y.split(',')] for y in x.split("~")] for x in open("data.txt").read().split("\n")]

class Brick():
    def __init__(self, start: list[int], end: list[int], id: int):
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
        self.update_bounds()

    def get_footprint(self):
        if len(self.z) == 1:
            if len(self.y) == 1:
                return len(self.x)
            return len(self.y)
        return 1
    
    def update_bounds(self):
        xr = [100000,0]
        yr = [100000,0]
        zr = [100000,0]
        xb, yb, zb = self.get_pos_info()
        for x in xb:
            xr = [x if x<xr[0] else xr[0], x if x > xr[1] else xr[1]]
        for y in yb:
            yr = [y if y<yr[0] else yr[0], y if y > yr[1] else yr[1]]
        for z in zb:
            zr = [z if z<zr[0] else zr[0], z if z > zr[1] else zr[1]]
        bounds = [x for x in zip(xr, yr, zr)]
        self.start = bounds[0]
        self.end = bounds[1]


class Graph():
    def __init__(self, input):
        if isinstance(input, dict):
            self.bricks: dict = input
            self.update_size(self.bricks)
            self.graph: list[list[list]] = [[[0 for x in range(self.xm+1)] for y in range(self.ym+1)] for z in range(self.zm+1)]
            for y,line in enumerate(self.graph[0]):
                for x,ch in enumerate(line):
                    self.graph[0][y][x] = -1
            for b in bricks.values():
                self.add_brick(b)
        else:
            self.bricks = {}
            self.xm = input[0]
            self.ym = input[1]
            self.zm = input[2]
            self.graph = [[[0 for x in range(self.xm+1)] for y in range(self.ym+1)] for z in range(self.zm+1)]
            for y,line in enumerate(self.graph[0]):
                for x,ch in enumerate(line):
                    self.graph[0][y][x] = -1
    
    #get min/max size of graph
    def update_size(self, bricks: dict[id: Brick]):
        xm = 0
        ym = 0
        zm = 0
        for b in bricks.values():
            xb, yb, zb = b.get_pos_info()
            for x in xb:
                xm = x if x > xm else xm
            for y in yb:
                ym = y if y > ym else ym
            for z in zb:
                zm = z if z > zm else zm
        self.xm = xm
        self.ym = ym
        self.zm = zm
    
    def get_size(self):
        return self.xm, self.ym, self.zm

    def get_item_at_point(self, x: int, y: int, z: int):
        return self.graph[z][y][x]

    def print_graph(self):
        for z,layer in enumerate(self.graph):
            print("z = ", z)
            for y in layer:
                print(y)

    def write_bricks(self, fname: str):
        fout = open(fname, "w")
        for b in self.bricks.values():
            fout.write(str(b.get_info()))
            fout.write("\n")
        fout.close()

    def write_graph(self, fname: str):
        fout = open(fname, "w")
        for z,layer in enumerate(self.graph):
            fout.write("z = "+ str(z) + "\n")
            for y in layer:
                fout.write(str(y) + "\n")
        fout.close

    def add_brick(self, brick: Brick):
        xl, yl, zl, id = brick.get_info()
        for x in xl:
            for y in yl:
                for z in zl:
                    self.graph[z][y][x] = id
                    self.bricks.update({id: brick})

    def gravity(self):
        # print(self.get_size())
        gout = Graph(self.get_size())
        seen = set()
        seen.add(0)
        count = 0
        for z,layer in enumerate(self.graph[1:]):
            for y,line in enumerate(layer):
                for x,id in enumerate(line):
                    if id in seen:
                        continue
                    seen.add(id)

                    s, e = self.bricks[id].get_bounds()
                    brick = Brick(s, e, id)
                    # brick = self.bricks[id]
                    under = brick.get_under()
                    checker = [1 for i in under if gout.get_item_at_point(*i) == 0]
                    if len(checker) != brick.get_footprint():
                        gout.add_brick(brick)
                        continue
                    
                    while len(checker) == brick.get_footprint():
                        brick.fall()
                        under = brick.get_under()
                        checker = [1 for i in under if gout.get_item_at_point(*i) == 0]
                    gout.add_brick(brick)
                    count += 1
        return gout, count

    def zap_brick(self, bid: int):
        gout = Graph(self.get_size())
        for id in self.bricks.keys():
            if id != bid:
                s, e = self.bricks[id].get_bounds()
                brick = Brick(s, e, id)
                gout.add_brick(brick)
        return gout

    def prune(self):
        self.update_size(self.bricks)
        gout = Graph(self.get_size())
        for z,layer in enumerate(gout.graph):
            for y,line in enumerate(layer):
                for x,id in enumerate(line):
                    gout.graph[z][y][x] = self.graph[z][y][x]
        self.graph = gout.graph

    def equals(self, other):
        return self.graph == other.graph

#turn bricks from lists to dict of brick objects
for pos,i in enumerate(bricks):
    bricks[pos] = Brick(i[0], i[1], pos+1)
bricks = {b.get_id():b for b in bricks}


mgraph = Graph(bricks)
tgraph, _ = mgraph.gravity()

tgraph.prune()
tgraph.write_graph("graph.txt")
tgraph.write_bricks("bricks.txt")

nsafe = 0
mtot = 0

for id in tgraph.bricks.keys():
    zgraph = tgraph.zap_brick(id)
    gzgraph, count = zgraph.gravity()

    # tgraph.write_bricks(str(id) + "base.txt")
    # zgraph.write_graph(str(id) + "zap.txt")
    # gzgraph.write_graph(str(id) + "grav.txt")

    if zgraph.equals(gzgraph):
        nsafe += 1
    else:
        mtot += count
print("s1", nsafe, "\ns2", mtot) #416, 60963
print(default_timer() - start) #approx 10.5 s after optimization!!!
