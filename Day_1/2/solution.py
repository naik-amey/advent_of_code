import math
maxvals = [0,0,0]
filename = 'input.txt'
currSum = 0
with open(filename,'r') as f:
   for line in f:
      if line == '\n':
         if currSum > maxvals[0]:
            maxvals[0],maxvals[1],maxvals[2] = currSum, maxvals[0], maxvals[1]
         elif currSum > maxvals[1]:
            maxvals[1],maxvals[2] = currSum, maxvals[1]
         elif currSum > maxvals[2]:
            maxvals[2] = currSum
         currSum = 0
      else:
         currSum += int(line)

print(f"Top 3 maxval is {sum(maxvals)} which is sum of {maxvals}")
