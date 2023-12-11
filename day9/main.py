f = lambda x : 0 if all(i==0 for i in x) else x[-1]+f([x[k]-x[k-1] for k in range(1,len(x))]) #star1
# f = lambda x : 0 if all(i==0 for i in x) else x[0]-f([x[k]-x[k-1] for k in range(1,len(x))]) #star2
print(sum([f(x) for x in [[int(y) for y in x.split()] for x in open("data.txt").read().split("\n")]]))