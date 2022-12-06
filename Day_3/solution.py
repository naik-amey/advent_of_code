import math
TotalScore = 0
filename = 'input.txt'

set1 = [0 for i in range(52)]
set2 = [0 for i in range(52)]

with open(filename,'r') as f:
    for line in f:
        line = line.strip()
        hlen = len(line) // 2
        common_char = ''.join(set(line[:hlen]).intersection(set(line[hlen:])))
        if common_char.isupper():
            score = ord(common_char) - ord('A') + 1 + 26
        else:
            score = ord(common_char) - ord('a') + 1
        # print(f"common char is {common_char} with score is {score}")
        TotalScore += score

print(f"total score {TotalScore}")