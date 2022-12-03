import os
import string

f = open(os.path.dirname(__file__) + '/../input.txt', "r")
prioDict = {}
priority = []
points = []
for i in range(52):
    prioDict.update({string.ascii_letters[i]: i+1})
    
#Part 1
# for line in f:
#     line = line.replace("\n", "")
#     firstHalf = line[:len(line.strip())//2]
#     secondHalf = line[len(line.strip())//2:]
#     priority.append(''.join(set(firstHalf).intersection(secondHalf)))
# for i in priority:
#     if prioDict.get(i):
#         points.append(prioDict[i])
# print(sum(points))

#Part 2
count = 0
group = []
for line in f:
    count += 1
    line = line.replace("\n", "")
    group.append(line)
    if count % 3 == 0:
        priority.append(''.join(set.intersection(set(group[0]), set(group[1]), set(group[2]))))
        group = []
for i in priority:
    if prioDict.get(i):
        points.append(prioDict[i])
print(sum(points))