import re
from timeit import default_timer
def soln(file: str):
    data = [[int(y) for y in x.strip("\n").split(" ")] for x in open(file).readlines()]
    fullout = 1
    for i in data:
        count = 0
        for j in range(1,i[0]+1):
            if (i[0] - j)*j > i[1]:
                count += 1
        fullout *= (count if count != 0 else 1)
    return fullout
start1 = default_timer()
print("s1:", soln("data1.txt"), "Time:", default_timer() - start1)
start2 = default_timer()
print("s2:", soln("data2.txt"), "Time:", default_timer() - start2)