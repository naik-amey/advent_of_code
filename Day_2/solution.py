import math
TotalScore = 0
filename = 'input.txt'

PIndex = {'X':1, 'Y':2, 'Z':3}
OIndex = {'A':1, 'B':2, 'C':3}

ChoicePoints = {'X':1, 'Y':2, 'Z':3}
MatchPoints = {'W':6, 'L':0, 'D':3}


def check(OppChoice, PlayerChoice):
    if OIndex[OppChoice] == PIndex[PlayerChoice]:
        return 'D'
    # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
    # X for Rock, Y for Paper, and Z for Scissors
    # A for Rock, B for Paper, and C for Scissors.
    # 1 for Rock, 2 for Paper, and 3 for Scissors
    # 1 > 3 or 3 > 2 or 2 > 1
    if ((OIndex[OppChoice] == 1 and PIndex[PlayerChoice] == 3) or \
       (OIndex[OppChoice] == 3 and PIndex[PlayerChoice] == 2) or \
        (OIndex[OppChoice] == 2 and PIndex[PlayerChoice] == 1)):
        return 'L'
    else:
        return 'W'

with open(filename,'r') as f:
    for line in f:
        line = line.strip()
        Ochoice, Pchoice = line.split(' ')
        matchRes = check(Ochoice, Pchoice)
        TotalScore += (ChoicePoints[Pchoice] + MatchPoints[matchRes])

print(f"total score {TotalScore}")