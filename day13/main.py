input = [x.split("\n") for x in open("data.txt").read().split("\n\n")]
for i in range(len(input)):
    for k in range(len(input[i])):
        input[i][k] = list(input[i][k])

def getCol(data, old):
    for i in range(1,len(data[0])):
        valid = True
        for row in data:
            if len([x for x in zip(row[:i][::-1], row[i:]) if x[0] != x[1]]) != 0:
                valid = False
        if valid and i != old:
            return i
    return 0

def getRow(data, old):
    for k in range(1,len(data)):
        if len([x for x in zip(data[:k][::-1], data[k:]) if x[0] != x[1]]) == 0 and k != old:
            return k
    return 0

#part1
total = 0
DP = {}
DP2 = {}
for i in range(len(input)):
    DP[i] = getCol(input[i], -1)
    DP2[i] = getRow(input[i],-1)
    total += DP[i] + 100 * DP2[i]
print("s1:", total)

#part2
total = 0
for i in range(len(input)):
    for x,y in [[x,y] for y in range(len(input[i])) for x in range(len(input[i][0]))]:
        dnew = [input[i][j].copy() for j in range(len(input[i]))]
        dnew[y][x] = "." if dnew[y][x] == "#" else "#"
        total += getCol(dnew, DP[i]) + 100 * getRow(dnew, DP2[i])
print("s2:", int(total/2))