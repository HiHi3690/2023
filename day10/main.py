import re
data = [x for x in open("test.txt").read().split("\n")]
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "S":
            s = [i,j]

up = ["|", "F", "7"]
down = ["|", "L", "J"]
left = ["-", "F", "L"]
right = ["-", "J", "7"]

path = []
min = [10000,100000]
max = [0,0]

p = [s[0], s[1]]
count = 0

while p != s or count == 0:
    if p == s:
        if data[p[0]-1][p[1]] in up:
            dir = "u"
        elif data[p[0]+1][p[1]] in down:
            dir = "d"
        elif data[p[0]][p[1]+1] in right:
            dir = "r"
        elif data[p[0]][p[1]-1] in left:
            dir = "l"
    else:
        if data[p[0]][p[1]] == "L":
            dir = "u" if dir == "l" else "r"
        elif data[p[0]][p[1]] == "J":
            dir = "u" if dir == "r" else "l"
        elif data[p[0]][p[1]] == "7":
            dir = "d" if dir == "r" else "l"
        elif data[p[0]][p[1]] == "F":
            dir = "d" if dir == "l" else "r"
        
    if dir == "u":
        p[0] -= 1
    elif dir == "d":
        p[0] += 1
    elif dir == "r":
        p[1] += 1
    elif dir == "l":
        p[1] -= 1
    
    min[0] = p[0] if p[0] < min[0] else min[0]
    min[1] = p[1] if p[1] < min[1] else min[1]
    max[0] = p[0] if p[0] > max[0] else max[0]
    max[1] = p[1] if p[1] > max[1] else max[1]

    count += 1
    path.append(p[0:2])

print("s1", count)

area = 0
# print(path)
for i in range(min[0],max[0]):
    for j in range(min[1],max[1]): 
        par = [x for x in range(j) if data[i][x] in ["|", 'J', 'L', 'S'] and [i,x] in path]
        if len(par) % 2 == 1 and [i,j] not in path:
            area += 1
            print(i,j)

print("s2", area)