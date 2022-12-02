import os

f = open(os.path.dirname(__file__) + '/../input.txt', "r")

#Part 1
def rps_score(me):
    if me == "X":
        return 1
    if me == "Y":
        return 2
    if me == "Z":
        return 3

def win_lose_score(opp, me):
    if opp == 'A':
        if me == 'X':
            return 3
        if me == 'Y':
            return 6
        if me == 'Z':
            return 0
    
    if opp == 'B':
        if me == 'X':
            return 0
        if me == 'Y':
            return 3
        if me == 'Z':
            return 6
    
    if opp == 'C':
        if me == 'X':
            return 6
        if me == 'Y':
            return 0
        if me == 'Z':
            return 3

#Part 2
def win_lose_score2(c):
    if c == 'X':
        return 0
    if c == 'Y':
        return 3
    if c == 'Z':
        return 6

def rps_score2(opp, c):
    if opp == 'A':
        if c == "X":
            return 3
        if c == "Y":
            return 1
        if c == "Z":
            return 2
        
    if opp == 'B':
        if c == "X":
            return 1
        if c == "Y":
            return 2
        if c == "Z":
            return 3
        
    if opp == 'C':
        if c == "X":
            return 2
        if c == "Y":
            return 3
        if c == "Z":
            return 1

score1 = 0
score2 = 0   
for line in f:   
    line = line.replace("\n", "")
    score1 += rps_score(line[2])+win_lose_score(line[0], line[2])
    score2 += win_lose_score2(line[2])+rps_score2(line[0], line[2])
print(score1)
print(score2)