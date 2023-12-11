import math
data = [x for x in open("data.txt").read().split("\n")]

erow = []
ecol = []

for i in range(len(data)):
    if [x for x in data[i] if x == "#"] == []:
        erow.append(i)
    
for j in range(len(data[0])):
    if [x for x in range(len(data)) if data[x][j] == "#"] == []:
        ecol.append(j)

print(erow,ecol)

# abs(dx) + abs(dy) = dist

points = [[x,y] for x in range(len(data)) for y in range(len(data[0])) if data[x][y] == "#"]

# print([[x,y] for x in points for y in points])

tots2 = 0
tots1 = 0

for i,j in [[x,y] for x in points for y in points]:
    numy = len([x for x in range(i[0], j[0]) if x in erow]) + len([x for x in range(j[0], i[0]) if x in erow])
    numx = len([x for x in range(i[1], j[1]) if x in ecol]) + len([x for x in range(j[1], i[1]) if x in ecol])
    
    # print(numy,numx, [i,j])
    tots1 += math.fabs(i[1] - j[1]) + math.fabs(i[0] - j[0]) + numx + numy
    tots2 += math.fabs(i[1] - j[1]) + 999999 * numx +  math.fabs(i[0] - j[0]) + 999999 * numy 
    # print(dx, dy, i, j)

print("s1", tots1/2, "s2", tots2/2)