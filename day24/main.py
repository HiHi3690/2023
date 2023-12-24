from re import findall
from sympy import *
from timeit import default_timer

file = "data.txt"

input = [[y.split(", ") for y in x.split(" @ ")] for x in open(file).read().strip().split("\n")]
s1data = {tuple([int(x) for x in x[0]]): tuple([int(x) for x in x[1]]) for x in input}
s2data = [[int(y) for y in findall("(-?\d+)", x)] for x in open(file).read().strip().split("\n")]
"""
Hailstone A: 19, 13, 30 @ -2, 1, -2
Hailstone B: 18, 19, 22 @ -1, -1, -2

ignore z

Hailstone A: 19, 13 @ -2, 1
Hailstone B: 18, 19 @ -1, -1

a(t) = <x = 19+t, y = 13-2t>
b(t) = <x = 18-t, y = 19-t>

solve for y:

a(x) = 13 - 2 * (x - 19)/1
b(x) = 19 - 1 * (x - 18)/-1

general case:

a(x) = aby - amy/amx * x - abx/amx * amy
b(x) = bby - bmy/bmx * x - bbx/bmx * bmy

solve
if in interval, +1, else, +0

divide by 2 if needed
"""

start = default_timer()

bounds = (7, 27) if file == "test.txt" else (200_000_000_000_000, 400_000_000_000_000)

def intersects(fpa, fva, fpb, fvb):
    a, c = fpa 
    b, d = fva

    f, h  = fpb
    g, i =  fvb

    if (d/b - i/g) == 0:
        return -1,-1

    x = ((h-c) + (a*d/b - f*i/g))/(d/b - i/g)
    y = c + d/b*x - a*d/b

    if (x - a)*b < 0 or (y - c)*d < 0 or (x - f)*g < 0 or (y - h)*i < 0:
        return -1, -1

    return (x, y)

tot = 0

for pa,va in s1data.items():
    for pb,vb in s1data.items():
        if pa == pb:
            continue

        fxa = pa[0:2]
        fya = va[0:2]
        fxb = pb[0:2]
        fyb = vb[0:2]

        x, y = intersects(fxa, fya, fxb, fyb)

        if bounds[0] <= x <= bounds[1] and bounds[0] <= y <= bounds[1]:
            tot += 1

print("s1", tot/2, "Time:", default_timer() - start)

#s2: put it into an eq solver because bruhhh

"""
System:
(H_2 - H_0) = lambda_1 (H_1 - H_0)
(H_3 - H_0) = lambda_2 (H_1 - H_0)

The following:
H_i = a_i + t_i b_i
a_i, b_i are 3d vecs
H_i is a 3d vec function (line)

turn this system to a system of 6 vars and 6 unknowns (h_0 pos and velo vecs)
"""
start = default_timer()

p = [[l[0], l[1], l[2]] for l in s2data[2:6]] #I had to do digging to get a valid result, indicies may vary
v = [[l[3], l[4], l[5]] for l in s2data[2:6]]

t0, t1, t2, t3, l1, l2 = symbols("t0, t1, t2, t3, l1, l2")

eqs = [Eq((p[2][i]-p[0][i]) + t2*v[2][i] - t0*v[0][i], l1*((p[1][i]-p[0][i]) + t1*v[1][i] - t0*v[0][i])) for i in range(3)]
eqs += [Eq((p[3][i]-p[0][i]) + t3*v[3][i] - t0*v[0][i], l2*((p[1][i]-p[0][i]) + t1*v[1][i] - t0*v[0][i])) for i in range(3)]



s = solve(eqs, [t0, t1, t2, t3, l1, l2])[0]

rock = [(s[1] * (p[0][i] + s[0]*v[0][i]) - s[0] * (p[1][i] + s[1]*v[1][i])) / (s[1]-s[0]) for i in range(3)]

print("s2", sum(rock), "Time:", default_timer() - start)