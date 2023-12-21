from collections import deque
from timeit import default_timer

start = default_timer()

input = open("data.txt").read().strip().split("\n")
m, n = len(input), len(input[0]) #height, width of grid

stepper = {'U': (-1, 0),'D': (1, 0),'R': (0, 1),'L': (0, -1)}

rocks = set()
circles = set()

for i,line in enumerate(input):
    for j,ch in enumerate(line):
        if ch == "#":
            rocks.add((j,i)) #x, y pairs
        if ch == "S":
            circles.add((j,i))

def step():
    dq = deque(circles)
    cout = set()
    while dq:
        px, py = dq.pop()
        for dir in "UDRL":
            nx, ny = px + stepper[dir][1], py + stepper[dir][0]
            if (nx%n, ny%m) not in rocks:
                cout.add((nx,ny))
    return cout

dp = []

#main looper, simulates enough cycles to get data points
for t in range(65+131*2):
    circles = step()
    if t == 63:
        print("s1", len(circles), "Time:",  default_timer() - start) # s1 solution occurs at t = 63
    if t in [64, 195, 326]: #data points based on reflections
        dp.append(len(circles))

#s2
'''
s2 works on many assumptions based on the input, and uses quadratic regression to calculate the answer.
Specifically, because 202300 * 131 + 65 is equal to the amount of requested steps, and because the restricted
space repeats and has nice symmetry, we can show that if we make a quadratic function f(t) that passes through the 
points (0,n(65)), (0,n(65+131)), and (0,n(65+2*131)), we can then plug in f(202300) to get our answer. This is 
accomplished in the below code, using a simplified Lagrange interpolation to find f(t).
'''

def lagrangeIterp(values):
    a = values[0] / 2 - values[1] + values[2] / 2 
    b = -3 * (values[0] /  2) + 2 * values[1] - values[2] / 2
    c = values[0]
    return a, b, c

x = 26501365 // 131 #202300
print("s2", (lambda x, coeffs: int(coeffs[0]*x*x + coeffs[1]*x + coeffs[2]))(x, lagrangeIterp(dp)), "Time:", default_timer() - start)