from enum import Enum
import sys
import heapq
from queue import PriorityQueue
from collections import deque

class Direction(Enum):
    u = (-1,0)
    r = (0, 1)
    d = (1,0)
    l = (0, -1)

class Node():
    def __init__(self, cost: int, x: int, y: int, dir: Direction):
        self.cost = cost
        self.x = x
        self.y = y
        self.dir = dir

    def __lt__(self, other):
        if self.cost == other.cost:
            if self.x == other.x:
                if self.y == other.y:
                    return self.dir.value < other.dir.value
                return self.y < other.y
            return self.x < other.x
        return self.cost < other.cost
    
    def get_info(self):
        return(self.x, self.y, self.dir)

def rawneighbors(x, y, graph):
    for dx, dy in ((0, -1), (1, 0), (-1, 0), (0, 1)):
        nx, ny = x+dx, y+dy
        if 0 <= nx < width and 0 <= ny < height:
            if graph[ny][nx] in '.<>^v':
                yield (nx,ny)

def measure(edges, start, head):
    count = 1
    while len(edges[head]) == 2:
        count += 1
        next = [n for _,n in edges[head] if n != start][0]
        start, head = (head, next)
    return (count, head)

def trails(graph):
    edges = {}
    for y in range(len(graph)):
        for x in range(len(graph[0])):
            if graph[y][x] in ".<>^v":
                edges[(x,y)] = [(1,n) for n in rawneighbors(x, y, graph)]
    
    nedges = {}
    for start,v in edges.items():
        if len(v) != 2:
            nedges[start] = [measure(edges, start, n[1]) for n in v]

    return nedges

def max_dfs(trails, start, end):
    mx = 0
    seen = set([start])
    stack = [(start, 0, seen)]

    while stack:
        pos, dist, seen = stack.pop()
        if pos == end and mx < dist:
            mx = dist
        for d,next in trails[pos]:
            if next not in seen:
                stack.append((next, dist+d, seen | set([next])))
    return mx

def grid_dijkstra(graph: list[list[int]]):
    
    pq: PriorityQueue[Node] = PriorityQueue()
    pq.put(Node(0, 0, 0, Direction.r))
    pq.put(Node(0, 0, 0, Direction.d))

    visited: set[tuple[int, int, Direction]] = set()

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
            pq.put(Node(newCost, newX, newY, newDir))
    return -1

class AdjMatGraph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[[0 for _ in range(vertices)] for _ in range(vertices)]]

    def printSolution(self, dist, src):
        for node in range(self.V):
            print("Vertex", node, "is dist", dist[node], "from source", src)

    # find and return node not in current checking tree (sptSet) with smallest distance value
    def minDistance(self, dist, sptSet):
        #set default max dist
        min = sys.maxsize

        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
        
        return min_index

    #Implements dijkstra's alg, starting at source src, using adj. matrix representation
    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for _ in range(self.V):

            # remove min dist vertex to source from set of vertices to be processed
            # x is always equal to src in iter 1
            x = self.minDistance(dist, sptSet)

            # put min dist vert in SPT
            sptSet[x] = True

            # update dist val of adj vertices to new vertex if current distance > new distance and the adj vertex y is not already in SPT
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
        
        self.printSolution(dist, src)

class AdjListGraph():
    def __init__(self, V):
        self.V = V
        self.adj = [[]] * V
    
    def addEdge(self, n1, n2, d):
        self.adj[n1].append((n2,d))
        self.adj[n2].append((n1,d))

    # Prints shortest dist from src to all vertices
    def shortestPath(self, src):

        # Create priority queue pq to store processing vertices
        pq = []
        heapq.heappush(pq, (0, src))

        # Create array for distances from src to vertex V, init all distances to INF
        dist = [float('inf')] * self.V
        dist[src] = 0
    
        while pq: #while list not empty
            # first var in pair is min distance of V, pop it from queue, storing label of V in second var
            d, u = heapq.heappop(pq) #remove min distance, V from PQ

            for v, weight in self.adj[u]: #loop through all Vs connected to above V
                if dist[v] > dist[u] + weight:
                    # update distance of v
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v)) #push OP onto PQ

        for node in range(self.V):
            print("Vertex", node, "is dist", dist[node], "from source", src)

