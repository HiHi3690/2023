import re
with open("data.txt", "r+") as f:
    data = f.readlines()
data = [x.strip("\n") for x in data]
#day1
# for i in range(1,len(data)): #parse data
#     temp = data[i].split(" = ")
#     temp[1] = re.sub("[()]", "", temp[1])
#     temp2 = temp[1].split(", ")
#     map[temp[0]+"L"] = temp2[0]
#     map[temp[0]+ "R"] = temp2[1]
# count = 1
# point = "AAA" + data[0][0] #initalize seed
# while point != "ZZZL" and point != "ZZZR": #compute count
#     point = map[point] + data[0][count%len(data[0])]
#     count += 1
# print(count-1)
#day2
for i in range(1,len(data)): #parse data
    temp = data[i].split(" = ")
    temp[1] = re.sub("[()]", "", temp[1])
    temp2 = temp[1].split(", ")
    data[i] = [temp[0], temp2]
stor = [data[x][0]+data[0][0] for x in range(1, len(data)) if data[x][0][-1] == "A"] #find all seeds that end in A then append L/R
keys = {} 
for i in data[1:]: #generate map
    keys[i[0] + "L"] = i[1][0]
    keys[i[0] + "R"] = i[1][1]
counts = []
for i in range(len(stor)): #calc counts
    count = 1
    while stor[i][-2] != "Z":
        stor[i] = keys[stor[i]] + data[0][count%len(data[0])]
        count += 1
    counts.append(count-1)
print("s2: " + str(counts))