import math
TotalScore = 0
filename = 'input.txt'

set1 = [0 for i in range(52)]
set2 = [0 for i in range(52)]

with open(filename,'r') as f:
    for line in f:
        l1 = line.strip()
        l2 = f.readline().strip()
        l3 = f.readline().strip()
        common_char = ''.join(set(l1).intersection(set(l2).intersection(set(l3))))
        if common_char.isupper():
            score = ord(common_char) - ord('A') + 1 + 26
        else:
            score = ord(common_char) - ord('a') + 1
        # print(f"common char is {common_char} with score is {score}")
        TotalScore += score

print(f"total score {TotalScore}")