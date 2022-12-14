from collections import deque
from functools import lru_cache
import math
filename = 'input_sample.txt'

DIR = [-1,0,1,0,-1]

grid = []

with open(filename,'r') as f:
    content = f.readlines()
    for r,line in enumerate(content):
        row = []
        for c,ch in enumerate(line.strip()):
            if ch.islower():
                row.append(ord(ch)-ord('a'))
            else:
                if ch == 'S':
                    row.append(0)
                    S = (r,c)
                else:
                    row.append(25)
                    E = (r,c)
        grid.append(row)
    
R, C = len(grid), len(grid[0])
visited = [[math.inf for c in range(C)] for r in range(R)]

def recurse(r,c,curr_score):
    for d in range(4):
        nr, nc = r + DIR[d], c + DIR[d+1]
        if nr < 0 or nr >= R or nc < 0 or nc >= C or grid[nr][nc] > (grid[r][c] + 1) or (visited[nr][nc] <= (1 + curr_score)):
            continue
        visited[nr][nc] = 1 + curr_score
        recurse(nr,nc,1 + curr_score)
    return 

r,c = S[0], S[1]
visited[r][c] = 0
recurse(r,c,0)

print(f"Shortest path is {visited[E[0]][E[1]]}")
    
