input = [x for x in open("data.txt").read().split("\n")]
# input = [[i[0], [int(z) for z in i[1].split(",")]] for i in input]
# print(input)

def isvalid(input, key):
    return key == [len(x) for x in input.split(".") if x != ""]

dp = {}
def f(data, blocks, pos, bpos, lenh):
    key = (pos, bpos, lenh)
    if key in dp:
        return dp[key]
    if pos == len(data):
        if len(blocks) == bpos and lenh == 0:
            return 1
        if bpos == len(blocks)-1 and lenh == blocks[bpos]:
            return 1
        else:
            return 0
    ans = 0
    for c in ['.', "#"]:
        if data[pos] == c or data[pos] == "?":
            if c == "." and lenh == 0:
                ans += f(data, blocks, pos+1, bpos, 0)
            elif c == "." and lenh > 0 and bpos<len(blocks) and blocks[bpos] == lenh:
                ans += f(data, blocks, pos+1, bpos+1, 0)
            elif c == "#":
                ans += f(data, blocks, pos+1, bpos, lenh+1)
    dp[key] = ans
    return ans

total = 0
for i in input:
    line,keys = i.split()
    keys = [int(x) for x in keys.split(",")]
    dp.clear()
    sum = f(line, keys, 0, 0, 0)
    total += sum
print("s1:", total)

total = 0
for i in range(len(input)):
    line,keys = input[i].split()
    # print(i)
    keys = ",".join([keys, keys, keys, keys, keys])
    keys = [int(x) for x in keys.split(",")]
    line = "?".join([line]*5)
    dp.clear()
    total += f(line, keys, 0, 0, 0)
print("s2:", total)