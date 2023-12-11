import re

with open("data.txt", "r+") as f:
    data = f.readlines()

data = [x.strip('\n') for x in data]

for i in data:
    i = [x for x in i]

# fullout = ""

# for i in data:
#     fullout += re.sub("[.0-9]","",i)

# fullout = list(set([x for x in fullout]))

# print(fullout)

relpos = [[1,1],[1,0],[0,1],[-1,0],[-1,1],[-1,-1], [1,-1], [0,-1]]

symbol = ["*"]

field = []

number = [str(x) for x in range(10)]

fullout = 0

for i in range(len(data)):
    for j in range(len(data)):
        if data[i][j] in symbol:
            field.append([i,j,0])
# print(field)
  
# num = ''
# valid = False
# hasnum = False
# for i in range(len(data)):
#     for j in range(len(data)):
#         if data[i][j] in number:
#             num += str(data[i][j])
#             # if isnear(i,j):
#                 # valid = True
#         if data[i][j] == '.' and num != '':
#             fullout += valid * int(num)
#             valid = False
#             num = ""


for i in range(len(data)):
    num = ''
    valid = False
    hasnum = False
    index = []
    for j in range(len(data[i])):
        if data[i][j] in number:
            hasnum = True
            num += data[i][j]
            for k in relpos:

                if j == 0:
                    if k[1] == -1:
                        # print("pain " + str(num))
                        # print(k)
                        break
                try:
                    for l in range(len(field)):
                        if field[l][0] == i+k[0] and field[l][1] == j+k[1]:
                            valid = True
                            index = l
                except:
                    pass
        # if j == len(data[i])-1 and hasnum and valid:
        #     # print("yay "+ str(num) + " " + str(fullout))
        #     num = ''
        #     valid = False
        #     hasnum = False
        #     # print(fullout)
        if (data[i][j] == '.' or data[i][j] not in number or j == len(data[i])-1) and hasnum and valid:
            # if fullout <= 100000:
            # print("yay "+ str(num) + " " + str(fullout))
            # fullout += int(num)
            field[index].append(int(num))
            field[index][2] += 1
            num = ''
            valid = False
            hasnum = False
            index = []
            # print(fullout)
        elif data[i][j] == ".":
            num = ''
            valid = False
            hasnum = False
        
for i in field:
    if i[2] == 2:
        fullout += i[3]*i[4]
        # print(fullout)

# print(field)

print(fullout)