#Shortest path over grid of weights

from enum import Enum
from queue import PriorityQueue

class Direction(Enum):
    u = (-1,0)
    r = (0, 1)
    d = (1,0)
    l = (0, -1)

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