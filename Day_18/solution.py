# read in the cubes.

import itertools
from collections import deque


cubes = {}

# so let's add the coordinates of each cube we scan to a dictionary of the form {coords: free_faces}, 
# initially filled with all 6.
with open('input.txt') as fin:
    for line in fin:
        coords = tuple(map(int, line.split(',')))
        cubes[coords] = 6

# A unit cube at x,y,z can be in contact with any of its immediate neighbors, 
# at x±1,y,z, x,y±1,z and x,y,z±1. Let's write a generator function to calculate 
# and yield the coordinates of the neighbors of a cube. We only need to go forward
# one step in any of the 6 possible directions:

def neighbors(x,y,z):
    yield (x+1,y  ,z  )
    yield (x-1,y  ,z  )
    yield (x  ,y+1,z  )
    yield (x  ,y-1,z  )
    yield (x  ,y  ,z+1)
    yield (x  ,y  ,z-1)


for c in cubes:
    for n in neighbors(*c):
        if n in cubes:
            cubes[c] -= 1

surface = sum(cubes.values())
print('Part 1:', surface)

######## solution part 2 ##########
minx = miny = minz = float('inf')
maxx = maxy = maxz = 0

for x, y, z in cubes:
    minx, maxx = min(x, minx), max(x, maxx)
    miny, maxy = min(y, miny), max(y, maxy)
    minz, maxz = min(z, minz), max(z, maxz)


rangex = range(minx, maxx + 1)
rangey = range(miny, maxy + 1)
rangez = range(minz, maxz + 1)

allseen = set()

# Now that we have a function able to identify and count internal faces, 
# we can call it for every empty unit cube inside our bounding box, and 
# accumulate the results. We need three nested for loops to iterate over 
# all possible x,y,z coordinates, so we can use itertools.product() to make our life easier.

def escape(cubes, src, rangex, rangey, rangez):
    touched = 0 # local counter. 
    seen = set()
    q = deque()
    q.append(src)

    while q:
        p = q.pop()
        
        if p in seen: continue

        seen.add(p)
        x, y, z = p

        # did we escape bounding box?
        if x not in rangex or y not in rangey or z not in rangez:
            return 0, seen 
        
        for n in neighbors(*p):
            if n in cubes:
                touched += 1
            else:
                if n not in seen:
                    q.append(n)
    # We ran out of free space to visit, which means we are trapped in an internal pocket
    return touched, seen


for c in itertools.product(rangex, rangey, rangez):
    if c not in cubes: # this is an empty unit cube of space
        if c not in allseen: # this is not in an internal pocket we already found
            touched, seen = escape(cubes, c, rangex, rangey, rangez)
            surface -= touched
            allseen |= seen


print('Part 2:', surface)
