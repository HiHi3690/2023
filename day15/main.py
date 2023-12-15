input = [[c for c in list(x)] for x in open("data.txt").read().split(",")]
# m, n = len(input), len(input[0])


s1total = 0
s2total = 0

for i in input:
    hash = 0
    for j in i:
        hash += ord(j)
        hash *= 17
        hash = hash % 256
    s1total += hash

boxArr = [[] for _ in range(256)]
# print(len(boxArr))

for i in input:
    hash = 0
    len = 0
    for j in i:
        if j in ["=", "-"]:
            break
        hash += ord(j)
        hash *= 17
        hash = hash % 256
        len += 1
    # print(i, hash)
    if i[len] == "=":
        replaced = False
        for lens in boxArr[hash]:
            if lens[0] == i[0:len]:
                lens[1] = i[-1]
                replaced = True
                break
        if not replaced:
            boxArr[hash].append([i[0:len], i[-1]])
    elif i[len] == "-":
        for j,lens in enumerate(boxArr[hash]):
            if lens[0] == i[0:len]:
                boxArr[hash].pop(j)
                break

for i,box in enumerate(boxArr):
    # print(i)
    for j,lens in enumerate(box):
        hash = int(i+1) * int(j+1) * int(lens[-1])
        # print(i, j, lens, hash)
        s2total += hash

print("s1", s1total, "s2", s2total)