##FAILED ATTEMPT 2


import collections

input = [list(x) for x in open("test.txt").read().split("\n")]
m, n = len(input), len(input[0])

print(m,n)


# turn with lower number in correct dir (RD)
# after getting here, save number at every point (current best case scenario)
# extra data point: how many blocks have you moved in straight line
# graph, seperate array current best (init at high number, 100mil)
# after you get to a point, what is current min heat loss at this point, and what is current least number blocks
# if gotten to point and traveled more and lost more heat, kill run ##IMPORTANT
# given at a point, what is lowest heat loss when going towards 


# how to say soln is obj worse: at this point, best i have ever done is heatloss, dir, dconsec, if dir = dir, heatlossN > heatloss, dconsecN >= dconsec

# make generator to ensure you have made every non-self-intersecting single path:
# at this point, change one thing at a time recursively

directions = {'u': (-1, 0),'d': (1, 0),'r': (0, 1),'l': (0, -1)}
nextnodedirs = {"r" : "udr", "l" : "udl", "u" : "lru", "d": "lrd"} 


def scorePath(nodesPassed: list([int,int])):
    return sum([int[node[1]][node[0]] for node in nodesPassed])

def bfs(input, x0: int, y0: int):
    minHL = 9 * m * n + 100 #well over max possible HL

    traversed = [[["", {c : [minHL, 5] for c in "uldr"}] for x in range(n)] for y in range(m)] #dir, HL, CD tripets
    traversed[y0][x0][0] += "rd"
    # print(traversed)

    pq = collections.deque([(y0, x0, "r", 0, 0), (y0, x0, "d", 0, 0)]) 

    while len(pq) > 0:
        currNode = pq.popleft() #x0, y0, dir, dconsec, HL

        currDir = currNode[2]
        i,j = currNode[0] + directions[currDir][0], currNode[1] + directions[currDir][1]


        if i>= m or j >= n or i < 0 or j < 0:
            continue

        heatloss = currNode[-1] + int(input[i][j])

        if i == m - 1 and j == n - 1:
            # update min dist to corner, then next in queue
            minHL = heatloss if heatloss < minHL else minHL
            continue
        
        pdata = traversed[i][j] # str, dict(minHL, dconsec)
        #insert above opt in comment spam here
        if currDir in pdata[0]:
            complist = pdata[1][currDir]
            if complist[0] < heatloss and complist[1] <= currNode[3]:
                continue
        
        pdata[0] += currDir
        if heatloss < pdata[1][currDir][0]:
            pdata[1][currDir] = [heatloss, currNode[4]]

        for d in nextnodedirs[currDir]:
            if d == currDir and currNode[3] < 4:
                bn = (i, j, d, currNode[3] + 1, heatloss)
                pq.appendleft(bn)
            elif d == currDir:
                continue
            else:
                bn = (i, j, d, 0, heatloss)
                pq.appendleft(bn)
        # print([x for x in traversed])
        # print(len([x for x in pq]))
    
    return minHL

print(bfs(input, 0, 0))