from collections import deque
input = open("data.txt").read().strip().split("\n")
m, n = len(input), len(input[0]) #height, width of grid


stepper = {'U': (-1, 0),'D': (1, 0),'R': (0, 1),'L': (0, -1)}

pos = (0,0)
rocks = set()
circles = set()

for i,line in enumerate(input):
    for j,ch in enumerate(line):
        if ch == "#":
            rocks.add((j,i)) #x, y pairs
        if ch == "S":
            pos = (j,i) #x,y pair

print(pos)
# print(rocks)

#iter 1
for dir in "UDRL":
    nx, ny = pos[0] + stepper[dir][1], pos[1] + stepper[dir][0]
    if (nx, ny) not in rocks:
        circles.add((nx,ny))

def step(barriers):
    dq = deque(circles)
    cout = set()
    while dq:
        px, py = dq.pop()
        for dir in "UDRL":
            nx, ny = px + stepper[dir][1], py + stepper[dir][0]
            if (nx%n, ny%m) not in barriers:
                cout.add((nx,ny))

    return cout

# #d1
# for t in range(1,64):
#     circles = step(rocks)
# print("s1", len(circles))

dp = []

for t in range(1,65+131*2):
    circles = step(rocks)
    if t == 63:
        print("s1", len(circles))
    if t in [64, 195, 326]:
        dp.append(len(circles))

def lagrangeIterp(values):
    a = values[0] / 2 - values[1] + values[2] / 2 
    b = -3 * (values[0] /  2) + 2 * values[1] - values[2] / 2
    c = values[0]
    return a, b, c

#d2
def f(x):
    a, b, c = lagrangeIterp(dp)
    return int(a*x*x + b*x + c) 

x = 26501365 // 131 #202300
print("s2", f(x))