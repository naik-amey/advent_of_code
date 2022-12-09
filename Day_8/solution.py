from enum import Enum
import math
TotalScore = 0
filename = 'input.txt'

'''
30373 vvvvv 03337   77730   00000   65599
25512 vvvnv 02555   55220   30373   65599
65332 vvnvv 06666   53320   35573   35599
33549 vnvnv 03355   99990   65573   35390
35390 vvvvv 03559   99900   65579   00000

Solution 1:
- apply bfs from every location. If you hit the end of the grid - it is visible else no
- you need to apply bfs from every location which seems stupid. O(MN*MN) complexity

Solution 2:
- find value less than grid_val in each of the 4 directions. Talk a walk and see if you reach ends. 
- O(M+M+N+N)*O(MN) = O(MN*(M+N))

Solution 3:
- O(M*N*4)
'''

with open(filename,'r') as f:
    grid = [[int(ch) for ch in line.strip()] for line in f]

# print(f"total score {grid}")
R, C = len(grid), len(grid[0])

# l,r,u,d = 0,1,2,3 # index in each dir
NINF = -math.inf
#maxG = [[[0,0,0,0] for c in range(C)] for r in range(R)]
maxG = [[[NINF,NINF,NINF,NINF] for c in range(C)] for r in range(R)]

# check left side
for r in range(R):
    for c in range(C):
        if c - 1 >= 0:
            maxG[r][c][0] = max(maxG[r][c][0],grid[r][c-1],maxG[r][c-1][0])

# check right side
for r in range(R):
    for c in range(C-1,-1,-1):
        if c < C-1:
            maxG[r][c][1] = max(maxG[r][c][1],grid[r][c+1],maxG[r][c+1][1])

# check up side
for c in range(C):
    for r in range(R):
        if r - 1 >= 0:
            maxG[r][c][2] = max(maxG[r][c][2],grid[r-1][c],maxG[r-1][c][2])

# check right side
for c in range(C):
    for r in range(R-1,-1,-1):
        if r < R-1:
            maxG[r][c][3] = max(maxG[r][c][3],grid[r+1][c],maxG[r+1][c][3])

cnt = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] > min(maxG[r][c][:]):
            cnt += 1

print(f"Number of visible trees {cnt}")


