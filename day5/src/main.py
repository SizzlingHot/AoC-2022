import os
import re

f = open(os.path.dirname(__file__) + '/../input.txt', "r")
stack = []
rearrangedStack = []

for line in f:
    stackInsert = []
    if line == "\n": 
        break
    for i in range(len(line) // 4):
        stackInsert.append(line[i * 4 + 1])
    stack.append(stackInsert)

stack.pop()
for i in zip(*stack):
    rearrangedStack.append(list("".join(i).strip()[::-1]))

for line in f:
    noMoved, pos1, pos2 = map(int, re.findall("\\d+", line))
    rearrangedStack[pos2 - 1].extend(rearrangedStack[pos1 - 1][-noMoved:][::-1]) #Part 2, Remove [::-1]
    rearrangedStack[pos1 - 1] = rearrangedStack[pos1 - 1][:-noMoved]
print(rearrangedStack)