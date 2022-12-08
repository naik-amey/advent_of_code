import math
TotalScore = 0
filename = 'input.txt'

class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def getrange(S):
    start, end = S.split('-')
    r = Range(int(start), int(end))
    return r

with open(filename,'r') as f:
    for line in f:
        line = line.strip()
        R1, R2 = line.split(',')
        r1, r2 = getrange(R1), getrange(R2)
        if (r1.start <= r2.start and r2.start <= r1.end) or \
            (r2.start <= r1.start and r1.start <= r2.end):
            TotalScore += 1

print(f"total score {TotalScore}")