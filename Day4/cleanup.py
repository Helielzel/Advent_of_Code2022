f = open("input.txt", "r")
inputs = f.readlines()

result = 0
for elem in inputs:
    elem = elem.strip("\n")
    pair = elem.split(",")
    pair[0], pair[1] = pair[0].split("-"), pair[1].split("-")
    if ((int(pair[0][0]) <= int(pair[1][0]) and int(pair[0][1]) >= int(pair[1][1])) or (int(pair[0][0]) >= int(pair[1][0]) and int(pair[0][1]) <= int(pair[1][1]))):
        result += 1

print(result)