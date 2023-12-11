import re

with open("data.txt", "r+") as f:
    data = f.readlines()

data = [x.strip("\n") for x in data]
fullout = 0
for i in range(len(data)):
    print(data[i])
    data[i] = re.sub("one","o!e",data[i])
    data[i] = re.sub("two","t@o",data[i])
    data[i] = re.sub("three","t#e",data[i])
    data[i] = re.sub("four","f$r",data[i])
    data[i] = re.sub("five","e?e",data[i])
    data[i] = re.sub("six","s^x",data[i])
    data[i] = re.sub("seven","s&n",data[i])
    data[i] = re.sub("eight","e*t",data[i])
    data[i] = re.sub("nine","n(e",data[i])
    data[i] = re.sub("zero","z)o",data[i])
    data[i] = re.sub("[^!^@^#^$^%^^^&^*^(^)^0-9]","",data[i])
    print(data[i])
    out = ""
    for s in data[i]:
        if s == "!":
              out += "1"
        if s == "@":
              out += "2"
        if s == "#":
              out += "3"
        if s == "$":
             out += "4"
        if s == "?":
             out += "5"
        if s == "^":
            out += "6"
        if s == "&":
            out += "7"
        if s == "*":
            out += "8"
        if s == "(":
            out += "9"
        if s == ")":
            out += "0"
        if s in [str(x) for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]:
            out += s
    print(out)
    print(s)
    print(out[0]+ out[-1]if out != "" else "")
    fullout += int(out[0]+ out[-1]) if out != '' else 0
        
print(fullout)
    
