##FAILED ATTEMPT 1

import sys
import heapq #used for adj. list interp of graph

input = [list(x) for x in open("test.txt").read().split("\n")]
m, n = len(input), len(input[0])

print(m,n)

class AdjListGraph():
    def __init__(self, V):
        self.V = V
        self.adj = [[()] * V] * V
    opposite = {"u": "d", 'd':'u', 'r':'l', 'l':'r'}
    def addPoint(self, x, y, weight, dir):
        dw = 0
        for dy in range(1,4):
            dw += input[y+dy][x]
            self.adj[y][x] = (x, y + dy, dw, "r")

            continue
        dw = 0
        for dx in range(1,4):
            continue

    # Prints shortest dist from src to all vertices
    def shortestPath(self, x, y, dir):

        # Create priority queue pq to store processing vertices
        pq = []
        heapq.heappush(pq, (0, x, y, dir))

        # Create array for distances from src to vertex V, init all distances to INF
        dist = [[float("inf")] * V] * V
        dist[y][x] = 0
    
        while pq: #while list not empty
            # first var in pair is min distance of V, pop it from queue, storing label of V in second var
            d, u, dir = heapq.heappop(pq) #remove min distance, V from PQ

            for v, weight in self.adj[u]: #loop through all Vs connected to above V
                if dist[v] > dist[u] + weight:
                    # update distance of v
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v, dir)) #push OP onto PQ

        return V, dist

V = m * n
g1 = AdjListGraph(V)

# for i in range(m):
#     for j in range(n):
#         g1.addEdge(i*m + j, 0, 0)

# out = sys.maxsize

# directions = {'u': (-1, 0),'d': (1, 0),'r': (0, 1),'l': (0, -1)}
# split = {"r" : "udr", "l" : "udl", "u" : "rlu", "d": "rld"}

# # print(splitnodeifneeded("d", 3))
# def countHeatLoss(ii, ji, di):
#     beams = [(ii,ji,di,0,0)]
#     visited = {}

#     minHeatLoss = sys.maxsize
#     while len(beams) > 0:
#         beam = beams.pop()

#         i,j = beam[0] + directions[beam[2]][0], beam[1] + directions[beam[2]][1]
        
#         #strengthen this breaking cond for if we have passed this point and dtot > visiteddist
#         if i>= m or j >= n or i < 0 or j < 0:
#             continue
        
#         dc = beam[-1] + int(input[i][j])

#         #remainder of quit cases
#         if i == m-1 and j == n-1:
#             minHeatLoss = dc if dc < minHeatLoss else minHeatLoss
#             continue
#         elif (i, j, beam[2]) in visited.keys():
#             if dc > visited[(i, j, beam[2])]:
#                 continue

#         visited.update({beam[0:3] : dc})

#         for d in split[beam[2]]:
#             if d == beam[2] and beam[3] < 4:
#                 bn = (i, j, d, beam[3] + 1, dc)
#                 beams.append(bn)
#             else:
#                 bn = (i, j, d, 0, dc)
#                 beams.append(bn)
#         # print(beams, visited)
#     return minHeatLoss



# print(countHeatLoss(0, -1, "r"))
