import re

mapping, input = [x for x in open("data.txt").read().split("\n\n")]
m, n = len(input), len(input[0])

mapping = [re.sub("}", "", x).split("{") for x in mapping.split("\n")] #key, rule sets
mapping = {x[0]: [re.sub(">", " 1 ", re.sub("<", " 0 ", re.sub(":", " ", rule))).split() for rule in x[1].split(",")] for x in mapping}

#day1 input gen
input = [[int(num) for num in re.sub("[{}xmas=]", "", x).split(",")] for x in input.split("\n")] #x, m, a, s tuples

for m in mapping:
    mapping[m][-1] = mapping[m][-1][0]
    # print(mapping[m])
# print(input)

ci = {"x": 0, 'm': 1, 'a': 2, 's': 3}

# print(mapping.keys())

total = 0
processed = 0
def processInput(OP):
    currMap = mapping["in"]
    # print(i, currMap)   
    while currMap not in ["A", "R"]:
        if type(currMap) == type(""):
            currMap = mapping[currMap]
            continue
        for rule in currMap:
            # print("new rule")
            # print(rule)
            # print(currMap)
            if rule in ["A", "R"]:
                currMap = rule
                break
            if type(rule) == type(""):
                "reached end"
                currMap = mapping[rule]
                break
            # print(rule)
            var, operation, comp, newMap = rule
            var = ci[var]
            operation = int(operation)
            comp = int(comp)
            # print(var, operation, comp, newMap)
            if operation and OP[var] > comp:
                # print("GT")
                currMap = newMap
                break
            if not operation and OP[var] < comp:
                # print("LT")
                currMap = newMap
                break
            else:
                # print("OTHER")
                pass
    # print(i, currMap)

    if currMap == "A":
        return sum(OP)
    else:
        return 0

for x in range(1,4001):
    for m in range(1,4001):
        for a in range(1,4001):
            for s in range(1,4001):
                total += processInput([x, m, a, s])
                processed += 1
                if processed % 10000 == 0:
                    print(processed)

print(total)