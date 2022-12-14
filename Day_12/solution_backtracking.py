from collections import deque
from functools import lru_cache
import math
filename = 'input_sample.txt'

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
visited = set()


@lru_cache(None)
def recurse(r,c):
    # base case
    if (r,c) == E:
        return 0
    # add node to visited
    score = math.inf
    for d in range(4):
        nr, nc = r + DIR[d], c + DIR[d+1]
        if (nr,nc) in visited or nr < 0 or nr >= R or nc < 0 or nc >= C or grid[nr][nc] > (grid[r][c] + 1):
            continue
        visited.add((nr,nc))
        score = min(score, 1 + recurse(nr,nc))
        visited.remove((nr,nc))
    return score

r,c = S[0], S[1]
visited.add((r,c))
score = recurse(r,c)
visited.remove((r,c))
#minscore = math.inf
#for d in range(4):
#    nr, nc = r + DIR[d], c + DIR[d+1]
#    if (nr,nc) in visited or nr < 0 or nr >= R or nc < 0 or nc >= C or grid[nr][nc] > (grid[r][c] + 1):
#        continue
#    visited.add((r,c))
#    minscore = min(minscore, 1 + recurse(nr,nc))

print(f"Shortest path is {score}")
    
