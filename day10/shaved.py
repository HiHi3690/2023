data = [x for x in open("test.txt").read().split("\n")]
p = [[x,y] for x in range(len(data)) for y in range(len(data[0])) if data[x][y] == "S"][0]
minmaxcp = [10000,100000, 0, 0, 0]
while p != [[x,y] for x in range(len(data)) for y in range(len(data[0])) if data[x][y] == "S"][0] or minmaxcp[-1] == 0:
    dir = ("u" if data[p[0]-1][p[1]] in ["|", "F", "7"] else "d" if data[p[0]+1][p[1]] in ["|", "L", "J"] else "r" if data[p[0]][p[1]+1] in ["-", "J", "7"] else "l" if data[p[0]][p[1]-1] in ["-", "F", "L"] else "") if p == [[x,y] for x in range(len(data)) for y in range(len(data[0])) if data[x][y] == "S"][0]  else (("u" if dir == "l" else "r") if data[p[0]][p[1]] == "L" else ("u" if dir == "r" else "l") if data[p[0]][p[1]] == "J" else ("d" if dir == "r" else "l") if data[p[0]][p[1]] == "7" else ("d" if dir == "l" else "r") if data[p[0]][p[1]] == "F" else dir) 
    p = [p[0]-1,p[1]] if dir == "u" else [p[0]+1,p[1]] if dir == "d" else [p[0],p[1]+1] if dir == "r" else [p[0],p[1]-1] if dir == "l" else p 
    minmaxcp = [p[0] if p[0] < minmaxcp[0] else minmaxcp[0], p[1] if p[1] < minmaxcp[1] else minmaxcp[1], p[0] if p[0] > minmaxcp[2] else minmaxcp[2], p[1] if p[1] > minmaxcp[3] else minmaxcp[3], minmaxcp[4] + 1] + minmaxcp[5:] + [p[0:2]]
print("s1", minmaxcp[4], "s2", len([[i,j] for j in range(minmaxcp[1],minmaxcp[3]) for i in range(minmaxcp[0],minmaxcp[2]) if len([x for x in range(j) if data[i][x] in ["|", 'J', 'L', 'S'] and [i,x] in minmaxcp[5:]]) % 2 and [i,j] not in minmaxcp[5:]]))
