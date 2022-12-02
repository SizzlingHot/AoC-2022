import os

f = open(os.path.dirname(__file__) + '/../input.txt', "r")
highest = [0, 0, 0]
temp = 0
total = 0
for line in f:
    line = line.replace("\n", "")
    if line == "":
        for i in range(len(highest)):
            if highest[i] < total:
                temp = highest[i]
                highest[i] = total
                total = temp
        total = 0
    else:
        total += int(line)
print(highest[0])
print(highest[0]+highest[1]+highest[2])