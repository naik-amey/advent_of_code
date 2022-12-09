import math
TotalScore = 0
filename = 'input.txt'

'''
30373 vvvvv 03337   77730   00000   65599
25512 vvvnv 02555   55220   30373   65599
65332 vvnvv 06666   53320   35573   35599
33549 vnvnv 03355   99990   65573   35390
35390 vvvvv 03559   99900   65579   00000

Solution:
- O(M*N*4) using stack to find index of next max on left, right, up and down
'''

with open(filename,'r') as f:
    grid = [[int(ch) for ch in line.strip()] for line in f]

# print(f"total score {grid}")
R, C = len(grid), len(grid[0])

# l,r,u,d = 0,1,2,3 # index in each dir
NINF = -math.inf
#maxG = [[[0,0,0,0] for c in range(C)] for r in range(R)]
maxG = [[[0,C-1,0,R-1] for c in range(C)] for r in range(R)]

# check next greatest index on left and right side
for r in range(R):
    stack = []
    for c in range(C):
    #for i in range(len(H)):
        while stack and grid[r][stack[-1]] <= grid[r][c]:
            idx = stack.pop()
            maxG[r][idx][1] = c
        #maxG[r][c][0] = stack[-1] if stack else 0  # IMPORTANT LINE
        stack.append(c)
    #maxG[r][c][0] = max(maxG[r][c][0],grid[r][c-1],maxG[r][c-1][0])

for r in range(R):
    stack = []
    for c in range(C-1,-1,-1):
    #for i in range(len(H)):
        while stack and grid[r][stack[-1]] <= grid[r][c]:
            idx = stack.pop()
            maxG[r][idx][0] = c
        #maxG[r][c][0] = stack[-1] if stack else 0  # IMPORTANT LINE
        stack.append(c)
    #maxG[r][c][0] = max(maxG[r][c][0],grid[r][c-1],maxG[r][c-1][0])

# check next greatest index on left and right side
for c in range(C):
    stack = []
    for r in range(R):
    #for i in range(len(H)):
        while stack and grid[stack[-1]][c] <= grid[r][c]:
            idx = stack.pop()
            maxG[idx][c][3] = r
        #maxG[r][c][2] = stack[-1] if stack else 0  # IMPORTANT LINE
        stack.append(r)
    #maxG[r][c][0] = max(maxG[r][c][0],grid[r][c-1],maxG[r][c-1][0])

for c in range(C):
    stack = []
    for r in range(R-1,-1,-1):
    #for i in range(len(H)):
        while stack and grid[stack[-1]][c] <= grid[r][c]:
            idx = stack.pop()
            maxG[idx][c][2] = r
        #maxG[r][c][2] = stack[-1] if stack else 0  # IMPORTANT LINE
        stack.append(r)
    #maxG[r][c][0] = max(maxG[r][c][0],grid[r][c-1],maxG[r][c-1][0])
#print(maxG)

maxScore = -math.inf
for r in range(R):
    for c in range(C):
        leftScore = c-maxG[r][c][0] 
        rightScore = maxG[r][c][1] - c 
        upScore = r-maxG[r][c][2] 
        downScore = maxG[r][c][3] - r 
        maxScore = max(leftScore*rightScore*upScore*downScore, maxScore)
        #print(maxScore)

print(f"Tree with max scenary score {maxScore}")


