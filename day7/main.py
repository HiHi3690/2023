import math
import re
with open("data.txt", "r+") as f:
    data = f.readlines()

# data = [x.strip("\n") for x in data]
data = [[y for y in x.strip("\n").split(" ")] for x in data]
data = [[data[x][0], int(data[x][1])] for x in range(len(data))]

value = {'2':20, "3":30, "4":40, "5":50, "6":60, "7":70, "8":80, '9':90, 'T':91, 'J':10, 'Q':92, 'K':93, 'A':94}
ranking = {}
numbers = []
stakes = {}

for i in data:
    #classify
    #card type count:
    cards = {"J":0}
    for c in i[0]:
        cards[c] = (cards[c] + 1 if c in cards.keys() else 1)
    '''scoring metric:
    A B C D E FF FF FF FF FF
    A: 5 of kind, 1 or 0
    B: 4 of kind, 1 or 0
    C: full house, 1 or 0
    D: THoK: 1 or 0
    E: TP/OP: 2 or 1 or 0
    FF x5: HC: 1-13
    '''
    out = [0 for x in range(11)]
    fh3 = False
    fh2 = False
    cc = 0
    for k in cards:
        if cards[k] + cards["J"] == 5:
            out[0] = 1
            # print("FoK")
        if cards[k] + cards["J"] == 4:
            out[1] = 1
            # print("FooK")
        if (fh3 and cards[k] + cards["J"] == 2) or (fh2 and cards[k] + cards["J"] == 3):
            out[2] = 1
            # print("FH")
        if cards[k] + cards["J"] == 3:
            out[3] = 1
            fh3 = True
            # print("ToK")
        if cards[k] + cards["J"] == 2:
            out[4] = out[4] + 1 #if out[4] <=1 else out[4]
            # print("TP/OP")
            fh2 = True
    for j in i[0]:
        out[cc+5] = value[j]
        cc += 1

    print(out, i[0])

    holder = ""
    for x in out[0:5]:
        holder += str(x)
    for x in out[5:10]:
        holder += str(x) if x in value.values() else "00"
    out = int(holder)

    ranking[out] = i[0]
    numbers.append(out)
    stakes[i[0]] = i[1]


numbers.sort()

fullout = 0

# print(data)

# print(stakes)
for i in range(len(numbers)):
    fullout += stakes[ranking[numbers[i]]] * (i+ 1)
    # print(stakes[ranking[numbers[i]]], ranking[numbers[i]], numbers[i], i+1)

print(fullout)