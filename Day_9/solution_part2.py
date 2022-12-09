filename = 'input.txt'
'''
start with 0,0 position. H and T are initialized to this position. 
T = H = (0,0)

read the instruction

for every step:
    H.move()
    Check distance between H and T (diagonal is allowed)
    if dist > 1: move Tail diagonally if required
        - it can take 8 possible directions. 
        - store the location T appears at in a set. 
    - finally return the size of the set. 

'''
class Object:
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
    
    def pos(self):
        return (self.x, self.y)

    def move(self, direction, step=1):
        if direction == 'R':
            self.x += 1
        elif direction == 'L':
            self.x -= 1
        elif direction == 'U':
            self.y += 1
        elif direction == 'D':
            self.y -= 1
    
    def movetail(self, orient, step=1):
        #x_orient, y_orient = orient
        if orient == ('R', 'F'):
            self.x += 1
        elif orient == ('L', 'F'):
            self.x -= 1
        elif orient == ('F', 'U'):
            self.y += 1
        elif orient == ('F', 'D'):
            self.y -= 1
        elif orient == ('R', 'U'):
            self.x += 1
            self.y += 1
        elif orient == ('R', 'D'):
            self.x += 1
            self.y -= 1
        elif orient == ('L', 'U'):
            self.x -= 1
            self.y += 1
        elif orient == ('L', 'D'):
            self.x -= 1
            self.y -= 1

    def DistandOrientation(self, other):
        # Chebyshev Distance
        x_ = (self.x - other.x)
        y_ = (self.y - other.y)
        dist = max(abs(x_), abs(y_))
        # Four possible orientations. 
        # 1. L 2. R 3. UL 4. UR 5. DL 6. DR
        x_orient = None
        y_orient = None
        if (x_ > 0):
            x_orient = 'R'
        elif (x_ < 0):
            x_orient = 'L'
        else:
            x_orient = 'F'

        if (y_ > 0):
            y_orient = 'U'
        elif (y_ < 0):
            y_orient = 'D'
        else:
            y_orient = 'F'
        return dist, (x_orient, y_orient)

P = [Object() for i in range(10)] # includes head. 
tail_loc = set()
tail_loc.add(P[9].pos())

with open(filename,'r') as f:
    for line in f:
        line = line.strip()
        Direction, Steps = line.split(' ')
        for step in range(int(Steps)):
            P[0].move(Direction,1)
            for i in range(1,10): # move tails
                dist, orient = P[i-1].DistandOrientation(P[i])
                if dist > 1:
                    P[i].movetail(orient,1)
            tail_loc.add(P[9].pos())

#print(tail_loc)
print(f"Size of the positions visited by tail are {len(tail_loc)}")
