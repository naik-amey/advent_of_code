import math
maxval = -math.inf
maxElf = 0
filename = 'input.txt'
currSum = 0
elfCnt = 1
# f = open(filename, "r")
with open(filename,'r') as f:
   for line in f:
      if line == '\n':
         maxElf = elfCnt if currSum > maxval else maxElf
         maxval = max(maxval, currSum)
         currSum = 0
         elfCnt += 1
      else:
         currSum += int(line)

print(f" maxval is {maxval} and Elf is {maxElf} / {elfCnt}")
