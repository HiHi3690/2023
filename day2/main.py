import re

with open("data.txt", "r+") as f:
    data = f.readlines()

data = [x.strip("\n") for x in data]

fullout = 0

for i in range(len(data)):
    data[i] = re.sub("Game " + str(i+1) + ": ","",data[i])
    
    data[i] = data[i].split(";")
    for j in range(len(data[i])):
        data[i][j] = data[i][j].split(",")
        for k in range(len(data[i][j])):
            data[i][j][k] = data[i][j][k].split(" ")
            try:
                data[i][j][k].remove("")
            except:
                pass
    print(data[i])

for i in range(len(data)):
    minr=0
    ming=0
    minb=0
    for j in data[i]:
        for k in j:
            if int(k[0]) > minr and k[1] == "red":
                minr = int(k[0])
            if int(k[0]) > ming and k[1] == "green":
                ming = int(k[0])
            if int(k[0]) > minb and k[1] == "blue":
                minb = int(k[0])
    print(str(minr) + " " + str(ming) + " " + str(minb))
    power = minr * ming * minb
    fullout += power

print(fullout)