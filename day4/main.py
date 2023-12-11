import re
with open("test.txt", "r+") as f:
    data = f.readlines()
data = [x.strip("\n") for x in data]
count = [0 for x in range(len(data))]
fullout = 0
for i in range(len(data)):
    data[i] = data[i][8:].split(" |")
    for j in range(len(data[i])):
        data[i][j] = data[i][j].split(" ")
        print(data[i][j])
adder = 0
for i in range(len(data)):
    print(data[i])
    for j in data[i][0]:
        if j in data[i][1] and j != "":
            adder = 1 if (adder == 0) else adder*2
    fullout += adder
    adder = 0
print(fullout)

# day 2
# with open("test.txt", "r+") as f:
#     data = f.readlines()
# data = [x.strip("\n") for x in data]
# fullout = 0
# for i in range(len(data)):
#     data[i] = data[i][8:].split(" |")
#     for j in range(len(data[i])):
#         data[i][j] = data[i][j].split(" ")
# print(data)
# def scoreCard(i):
#     count = 0
#     for j in data[i][0]:
#         if j in data[i][1] and j != "":
#             count += 1
#     return count
# count = [[1,scoreCard(x)] for x in range(len(data))]
# for i in range(len(count)):
#     for j in range(1,count[i][1]+1):
#         count[i+j][0] += count[i][0]
#         print(count)
#     fullout += count[i][0]
# print(fullout)