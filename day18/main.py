import re

input = [re.sub("[()#]", "", x).split() for x in open("data.txt").read().split("\n")] #janky parser, but gets lines into (dir: str, num: str, color: str) format

def calcArea(s2: bool):
    if not s2:
        stepper = {'U': (-1, 0),'D': (1, 0),'R': (0, 1),'L': (0, -1)}
    else:
        stepper = {'3': (-1, 0),'1': (1, 0),'0': (0, 1),'2': (0, -1)}
    verticies = []
    border = 0
    pointer = (0, 0)
    for i in input:
        dir, num, color = i
        num = int(num)
        if s2:
            num = int(color[:5], 16)
            dir = color[-1]
        border += int(num)
        pointer = (pointer[0] + stepper[dir][1] * num, pointer[1] +stepper[dir][0] * num)
        verticies.append(pointer)   

    #get raw area of polygon with shoelace formula
    area = 0
    for i in range(-1,len(verticies)-1):
        xi,yi = verticies[i]
        xi1,yi1 = verticies[i+1]
        area += (yi + yi1) * (xi - xi1) * 0.5

    #get internal lattice points with Pick's thm
    intlat = area - border/2 + 1

    return int(border + intlat)

print("s1", calcArea(False), "\ns2", calcArea(True))