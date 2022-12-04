import os

f = open(os.path.dirname(__file__) + '/../input.txt', "r")
numFullContain = 0
numOverlap = 0

#Part 1
# for line in f:
#     groups = []
#     group1 = []
#     group2 = []
#     line = line.replace("\n", "")
#     groups = line.split(",")
#     group1 = groups[0].split("-")
#     group2 = groups[1].split("-")
#     if int(group1[0]) <= int(group2[0]):
#         if group1[1] >= group2[1]:
#             numFullContain += 1
#             continue      
#     if int(group1[0]) >= int(group2[0]):
#         if int(group1[1]) <= int(group2[1]):
#             numFullContain += 1
#             continue
# print(numFullContain)

#Part 2
for line in f:
    groups = []
    group1 = []
    group2 = []
    line = line.replace("\n", "")
    groups = line.split(",")
    group1 = groups[0].split("-")
    group2 = groups[1].split("-")
    if int(group1[0]) < int(group2[0]):
        if int(group1[1]) >= int(group2[0]):
            numOverlap += 1
            continue
    if int(group1[0]) > int(group2[0]):
        if int(group1[0]) <= int(group2[1]):
            numOverlap += 1
            continue
    if  int(group1[0]) == int(group2[0]):
        numOverlap += 1
        print(line)
        continue
print(numOverlap)