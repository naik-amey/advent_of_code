import math
TotalScore = 0
filename = 'input.txt'

PIndex = {'X':1, 'Y':2, 'Z':3}
OIndex = {'A':1, 'B':2, 'C':3}
ChoicePoints = {'A':1, 'B':2, 'C':3}
MatchPoints = {'Z':6, 'X':0, 'Y':3}
LoseCompliment = {'A':'C','B':'A','C':'B'}
WinCompliment = {'A':'B','B':'C','C':'A'}

def MakeChoice(OppChoice, matchRes):

    if matchRes == 'Y':
        return OppChoice

    if matchRes == 'X': # player should lose
        return LoseCompliment[OppChoice]
    else:
        return WinCompliment[OppChoice]
    # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
    # X for Lose, Y for Draw, and Z for Win
    # A for Rock, B for Paper, and C for Scissors.
    # 1 for Rock, 2 for Paper, and 3 for Scissors
    # 1 > 3 or 3 > 2 or 2 > 1

with open(filename,'r') as f:
    for line in f:
        line = line.strip()
        Ochoice, matchRes = line.split(' ')
        Pchoice = MakeChoice(Ochoice, matchRes)
        TotalScore += (ChoicePoints[Pchoice] + MatchPoints[matchRes])

print(f"total score {TotalScore}")