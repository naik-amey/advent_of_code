from collections import deque
from functools import lru_cache
import math
filename = 'input.txt'

'''
Read in the input

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

012
123

locate S and E in the grid. 
    - Replace it with 'a' and 'z' in the grid for simplicity? 

There are 4 possible directions we can go it. 
Consider it to be a grid. 
Apply BFS? or DFS? Djiktras is not required because it is not weighted.

Read the input

BFS:
    add S to the queue. 
    - pop from the queue, 
        visit all the the valid unvisited cells. 

Looks like we need backtracking algorithm?

add node to visited set. 
- enter next node for every possible node. 
- 

'''
        
#DIR = [(0,1),(0,-1),(1,0),(-1,0)]
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
#checkmap = [[0 for c in range(C)] for r in range(R)]
#c1 = [[[] for c in range(C)] for r in range(R)]

cnt =[0]

@lru_cache(None)
def recurse(r,c,curr_score):
    for d in range(4):
        nr, nc = r + DIR[d], c + DIR[d+1]
        #if nr < 0 or nr >= R or nc < 0 or nc >= C or grid[nr][nc] > (grid[r][c] + 1) or (visited[nr][nc] <= (1 + curr_score)):
        if nr < 0 or nr >= R or nc < 0 or nc >= C or (grid[nr][nc] < grid[r][c]-1) or (visited[nr][nc] <= (1 + curr_score)):# or visited[nr][nc] == 1:
            continue
        visited[nr][nc] = 1 + curr_score
        #checkmap[nr][nc] += 1
        #c1[nr][nc].append((r,c))
        recurse(nr,nc,1 + curr_score)
    return 

r,c = E[0], E[1]
visited[r][c] = 0
recurse(r,c,0)

#print(checkmap)
#print(visited)

print(f"Shortest path is {visited[S[0]][S[1]]}")
    
