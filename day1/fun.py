with open("data.txt", "r+") as f:
    data = f.readlines()

data = [x.strip("\n") for x in data]
fullout = 0
for i in range(len(data)):
    out = ""
    for j in range(len(data[i])):
        # print(data[i][j:j+3])
        if data[i][j:j+3] == "one":
            out += "1"
        if data[i][j:j+3] == "two":
            out += "2"
        if data[i][j:j+5] == "three":
            out += "3"
        if data[i][j:j+4] == "four":
            out += "4"
        if data[i][j:j+4] == "five":
            out += "5"
        if data[i][j:j+3] == "six":
            out += "6"
        if data[i][j:j+5] == "seven":
            out += "7"
        if data[i][j:j+5] == "eight":
            out += "8"
        if data[i][j:j+4] == "nine":
            out += "9"
        if data[i][j:j+4] == "zero":
            out += "0"
        if data[i][j] in [str(x) for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]:
            out += data[i][j]
    fullout += int(out[0]+out[-1])
    print(data[i])
    print(out)
    print(out[0]+out[-1])
print(fullout)