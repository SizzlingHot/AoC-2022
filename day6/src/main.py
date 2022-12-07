import os

sequence = [None, None, None, None] # , None, None, None, None, None, None, None, None, None, None
count = 0

f = open(os.path.dirname(__file__) + '/../input.txt', "r")
for line in f:
    for char in line:
        count += 1
        sequence[0] = sequence[1]
        sequence[1] = sequence[2]
        sequence[2] = sequence[3]
        # sequence[3] = sequence[4]
        # sequence[4] = sequence[5]
        # sequence[5] = sequence[6]
        # sequence[6] = sequence[7]
        # sequence[7] = sequence[8]
        # sequence[8] = sequence[9]
        # sequence[9] = sequence[10]
        # sequence[10] = sequence[11]
        # sequence[11] = sequence[12]
        # sequence[12] = sequence[13]
        sequence[3] = char
        # sequence[13] = char
        if len(set(sequence)) == 4 and sequence[0] is not None:
            break
print(count)