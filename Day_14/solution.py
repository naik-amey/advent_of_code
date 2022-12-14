from collections import deque
from posixpath import split
filename = 'input.txt'

'''
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9

Sand always pours in from 500,0 (source)

try down, 
    try down left 
        try down right

curr_node (dnode if not rock -> update curr_node, and recurse
           dlnode is not rock -> update curr_node and recurse
           drnode is not rock -> update curr_node and recurse
curr_node (dnode, dlnode, drnode) if all 3 are rock. I mark curr_node as rock

1. calling recurse( till curr_node is marked as rock) do this till when?
2. if your sand is settling beyond max 'y' co-ordinate. STOP!

(1) seems to be slow, is there a better way?
    - recall where sand settled. - originate above that and run recurse. do this while that location is filled with sand. (try up)
    - then try up again till it gets filled with sand.

  4     5  5
  9     0  0
  4     0  3
0 ......+...
1 ..........
2 ......7...
3 .....767..
4 ....#656##
5 ....#545#.
6 ..###434#.
7 ....4323#.
8 ...43212#.
9 #########.

.......+...
.......~...
......~o...
.....~ooo..
....~#ooo##
...~o#ooo#.
..~###ooo#.
..~..oooo#.
.~o.ooooo#.
~#########.
~..........
~..........
~..........
'''

y_max = 0
wall_set = set()
sand_set = set()

with open(filename, encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        for i, cord in enumerate(line.split('->')):
            dim = cord.split(',')
            x, y = int(dim[0]), int(dim[1])
            y_max = max(y_max, y)
            if i == 0:
                px, py = x,y
                continue
            if px == x: # vertical line. 
                for ys in range(min(y,py), max(y,py)+1):
                    wall_set.add((x,ys))
                    #print((x,ys))
            else:
                for xs in range(min(x,px), max(x,px)+1):
                    wall_set.add((xs,y))
                    #print((xs,y))
            
            px, py = x,y

# run recurse once from the origin (500,0)
DIR = [(0,1), (-1,1), (1,1)]
DO, DL, DR = 0, 1, 2
def recurse(sx,sy):
    if sy == y_max: #no where to go
        return (None, None) # which means you need to stop

    for i in range(len(DIR)):
        nx, ny = sx+DIR[i][0], sy+DIR[i][1]
        if (nx,ny) not in wall_set and (nx,ny) not in sand_set and ny < y_max+2:
            return recurse(nx,ny)
    # if you have reached here, you don't have anywhere to go, so set sx,sy as rock and return its dimensions
    sand_set.add((sx,sy))
    return (sx,sy)
    
        

sx,sy = 500,0
init_sand_location = recurse(sx,sy)

# go up one level from the sand location
rx, ry = init_sand_location

while rx != None and ry != None:
    sx, sy = rx, ry-1
    while (sx,sy) not in sand_set:
        rx,ry = recurse(sx,sy)
        if rx == None and ry == None: 
            break

print(f"size of sand set {len(sand_set)}")
        

