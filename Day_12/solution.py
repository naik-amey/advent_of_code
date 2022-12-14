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
visited = [[0 for c in range(C)] for r in range(R)]
q = deque()
q.append((E,0)) # end node and score

part = 2

while (q):
    node, score = q.popleft()
    r, c = node
    if grid[r][c] == 0 and (part == 2 or node == S):
        break #score
    
    for d in range(4):
        nr, nc = r + DIR[d], c + DIR[d+1]
        if nr < 0 or nr >= R or nc < 0 or nc >= C or (grid[nr][nc] < grid[r][c]-1) or visited[nr][nc] == 1:
            continue
        visited[nr][nc] = 1
        q.append(((nr,nc),1 + score))

print(f"Shortest path is {score}")
    

'''
19 < 21-1 : True
20 < 21-1 : False
21 < 21-1 : False
22 < 21-1 : False
'''
