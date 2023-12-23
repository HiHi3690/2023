from collections import deque
from timeit import default_timer
from queue import PriorityQueue
start = default_timer()

input = [list(x) for x in open("data.txt").read().split("\n")]
height, width = len(input), len(input[0])
# print(height, width)

def neighbors(x: int,y: int, graph):
    if graph[y][x] == 'v':
        yield (x, y+1)
        return

    if graph[y][x] == '^':
        yield (x, y-1)
        return

    if graph[y][x] == '>':
        yield (x+1, y)
        return

    if graph[y][x] == 'v':
        yield (x-1, y)
        return

    for dx, dy in ((0, -1), (1, 0), (-1, 0), (0, 1)):
        nx, ny = x+dx, y+dy
        if graph[y][x] == "#":
            continue
        if nx >= width or ny >= height or nx < 0 or ny < 0:
            continue
        yield (nx, ny)

def p1(graph, start, end):
    dq = deque([(*start, set())])
    visited = dict()
    visited[start] = 0

    while dq:
        x, y, path = dq.pop()

        if (x, y) == end:
            continue

        for nbr in neighbors(x, y, graph):
            ncost = visited[x,y] + 1
            if nbr in path:
                continue
            if nbr not in visited or ncost > visited[nbr]:
                visited[nbr] = ncost
                npath = path.copy()
                npath.add(nbr)

                dq.appendleft((*nbr, npath))
    return visited

used = p1(input, (1,0), (height-2, width-1))
print("s1", used[(height-2, width-1)]) #2190
print(default_timer()-start) #approx 7.6s

#Day 2

start_t = default_timer()

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

def dfs(trails, start, end):
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

start = (1,0)
end = (width-2, height-1)
print("s2", dfs(trails(input), start, end))
print(default_timer()-start_t)