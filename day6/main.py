import re
with open("data.txt", "r+") as f:
    data = f.readlines()
data = [[int(y) for y in x.strip("\n").split(" ")] for x in data]
fullout = 1
for i in data:
    count = 0
    for j in range(1,i[0]+1):
        if (i[0] - j)*j > i[1]:
            count += 1
    fullout *= (count if count != 0 else 1)
print(fullout)