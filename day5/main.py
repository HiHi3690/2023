import re

with open("data.txt", "r+") as f:
    data = f.readlines()

data = [x.strip("\n") for x in data]

fullout,k = 0,0

seeds = data[0].split(" ")
seeds = [[int(y) for y in x.split(",")] for x in seeds]

keywords = ["sts", "stf", "ftw", "wtl", "ltt", "tth", "htl"]
keys = [[],[],[],[], [],[],[],[]]

for i in range(1,len(data)):
    data[i] = [int(x) for x in data[i].split(" ")] if data[i] not in keywords else data[i]

counter = 0

keys[0] = seeds

for i in range(len(data)):
    if data[i] in keywords:
        counter += 1
    elif counter == 0:
        keys[0] = seeds
    else:
        keys[counter].append(data[i])

min = 100000000000
max = 0
for k in keys[0]:
    min = (k[0] if k[0] < min else min)
    max = (k[1]+k[0] if k[1]+k[0] > max else max)
#logic for s1
# for k in keys[0]:
#     for seed in range(min,max):
#         out = seed
#         for i in range(1,len(keys)):
#             for j in range(len(keys[i])):
#                 if (out >= keys[i][j][1]) and (out <= keys[i][j][1] + keys[i][j][2]):
#                     out = out - (keys[i][j][1] - keys[i][j][0])
#                     break
#                 # print(k, out, keys[i][j])

#         if out < fullout or fullout == 0:
#             fullout = out
#         # print(fullout, out, seed)

#logic for s2
seed = 1
loop = True

while loop:
    check = seed
    for i in range(len(keys)-1,0, -1):
        for j in range(len(keys[i])):
            if check >= keys[i][j][0] and check <= keys[i][j][2] + keys[i][j][0]:
                check = check - keys[i][j][0] + keys[i][j][1]
                break
        # print(check, seed, keys[i][j])
    for i in keys[0]:
        if (check >= i[0]) and (check <= i[0] + i[1]):
            loop = False
    seed += 1

print(keys[0])
print(check,seed-1)