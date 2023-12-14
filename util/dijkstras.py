import sys #used for int_max
import heapq #used for adj. list interp of graph

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


# Adj. Matrix representation of graph
g1 = AdjMatGraph(9)
g1.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0]
            ]

g1.dijkstra(0)


#Adj List representation of Graph
V = 9
g1 = AdjListGraph(V)

#Init graph
g1.addEdge(0, 1, 4)
g1.addEdge(0, 7, 8)
g1.addEdge(1, 2, 8)
g1.addEdge(1, 7, 11)
g1.addEdge(2, 3, 7)
g1.addEdge(2, 8, 2)
g1.addEdge(2, 5, 4)
g1.addEdge(3, 4, 9)
g1.addEdge(3, 5, 14)
g1.addEdge(4, 5, 10)
g1.addEdge(5, 6, 2)
g1.addEdge(6, 7, 1)
g1.addEdge(6, 8, 6)
g1.addEdge(7, 8, 7)

g1.shortestPath(5)
