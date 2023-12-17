##WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO

from enum import Enum
from queue import PriorityQueue

input = [[int(y) for y in x] for x in open("data.txt").read().split("\n")]
m, n = len(input), len(input[0])

# print(m,n)
# for l in input:
#     print(l)


stepper = {'u': (-1, 0),'d': (1, 0),'r': (0, 1),'l': (0, -1)}
inv = {"u": "d", 'd':'u', 'r':'l', 'l':'r'}

class Direction(Enum):
    u = (-1,0)
    r = (0, 1)
    d = (1,0)
    l = (0, -1)

"""
# NODE CLASS
init : cost(HL), x, y, dir, step counter
def less than
    cost, x, y, dir, step counter priority order
def get info (for memoization list)
    x, y, dir, stepcounter
"""

class Node():
    def __init__(self, cost: int, x: int, y: int, dir: Direction, stepcounter: int):
        self.cost = cost
        self.x = x
        self.y = y
        self.dir = dir
        self.stepcounter = stepcounter

    def __lt__(self, other):
        if self.cost == other.cost:
            if self.x == other.x:
                if self.y == other.y:
                    if self.dir == other.dir:
                        return self.stepcounter < other.stepcounter
                    return self.dir.value < other.dir.value
                return self.y < other.y
            return self.x < other.x
        return self.cost < other.cost
    
    def get_info(self):
        return(self.x, self.y, self.dir, self.stepcounter)


"""

dijkstra fxn:
in: graph, max_steps
out: cost

pq: set of walkInfo

put init vals, r/d, 1 in pq

visited: set of tuples, (x, y, dir, step counter)

while queue:
    curr = queue.get() 

    if curr info in visited, continue, else add it to visited

    calc next position in direction based on node class.direction
    if new pos OOB, skip
    calc new cost
    if at end and stepcounter + 1 isn't over max steps, return curr cost + final tile cost

    for each dir:
        if opposite, skip
        if same, increment new step counter, else, set to 1
        if new step counter too high, skip
        add point to queue (new cost, x, y, new dir, new sc)
if breaks out of loop before returning, ret -1

"""

def dijkstra(graph: list[list[int]],min_steps: int, max_steps: int):
    
    pq: PriorityQueue[Node] = PriorityQueue()
    pq.put(Node(0, 0, 0, Direction.r, 1))
    pq.put(Node(0, 0, 0, Direction.d, 1))

    visited: set[tuple[int, int, Direction, int]] = set()

    while pq:
        curr = pq.get()

        if curr.get_info() in visited:
            continue
        visited.add(curr.get_info())

        newX = curr.x + curr.dir.value[1]
        newY = curr.y + curr.dir.value[0]

        if newX >= len(graph[0]) or newY >= len(graph) or newX < 0 or newY < 0:
            continue 

        newCost = curr.cost + graph[newY][newX]

        if newX == len(graph[0]) - 1 and newY == len(graph) - 1 and curr.stepcounter + 1 <= max_steps:
            return newCost
    
        for newDir in Direction:
            #if opp dir
            if newDir.value[0] + curr.dir.value[0] == 0 and newDir.value[1] + curr.dir.value[1] == 0:
                continue
            #if same dir
            if newDir.value[0] == curr.dir.value[0] and newDir.value[1] == curr.dir.value[1]:
                newStepCounter = curr.stepcounter + 1
            #if other dir and hasn't done minimum
            elif curr.stepcounter < min_steps:
                continue
            #if other dir and has done minimum
            else:
                newStepCounter = 1
            if newStepCounter > max_steps:
                continue
            pq.put(Node(newCost, newX, newY, newDir, newStepCounter))
    return -1

print("s1:", dijkstra(input, 0, 3))

print("s2:", dijkstra(input, 4, 10))