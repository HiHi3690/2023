#Note: very slow/unoptimal, I don't care

input = [list(x) for x in open("data.txt").read().split("\n")]

def north(data):
    for _ in range(len(data)):
        for i,line in enumerate(data[1:]):
            for j,char in enumerate(line):
                # print(i,j)
                if data[i+1][j] == "O" and data[i][j] == ".":
                    data[i+1][j] = "."
                    data[i][j] = "O"
    return data

def west(data):
    for _ in range(len(data)):
        for i,line in enumerate(data):
            for j,char in enumerate(line[1:]):
                # print(i,j)
                if data[i][j+1] == "O" and data[i][j] == ".":
                    data[i][j+1] = "."
                    data[i][j] = "O"
    return data

def south(data):
    for _ in range(len(data)):
        for i,line in enumerate(data[:len(data)-1]):
            for j,char in enumerate(line):
                # print(i,j)
                if data[i][j] == "O" and data[i+1][j] == ".":
                    data[i][j] = "."
                    data[i+1][j] = "O"
    return data

def east(data):
    for _ in range(len(data)):
        for i,line in enumerate(data):
            for j,char in enumerate(line[:len(line)-1]):
                # print(i,j)
                if data[i][j] == "O" and data[i][j+1] == ".":
                    data[i][j] = "."
                    data[i][j+1] = "O"
    return data

input = north(input)

total = 0
for i,line in enumerate(input):
    for c in line:
        if c == "O":
            total += len(input) - i

print("s2:", total)

DP = {}

count = 1000000000
for i in range(count):
    input = east(south(west(north(input))))
    key = ""
    for row in input: key += "".join(row)
    if key in DP:
        diff = i-DP[key]
        count = (count-i)%diff - 1
        for i in range(count):
            input = east(south(west(north(input))))
        break
    # print(i)
    DP[key] = i


total = 0
for i,line in enumerate(input):
    for c in line:
        if c == "O":
            total += len(input) - i

print("s2:", total)
