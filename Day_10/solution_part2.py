filename = 'input.txt'

'''
X = 1, cnt = 0
read the instruction

if noop -> just increment the counter. 
if addx v -> increment counter by 2 and value of x by v
'''
def update(screen_map, X):
    if cycle%40 in [X-1,X,X+1]:
        screen_map[cycle] = '#'

X = 1
cycle = 0
sprite = X # location of the sprite
screen_map = ['.' for i in range(40*6)] # dimention

with open(filename,'r') as f:
    for line in f:
        line = line.strip()
        if line == 'noop':
            update(screen_map,X)
            cycle += 1
        else:
            instruction, V = line.split(' ')
            update(screen_map,X)
            cycle += 1
            update(screen_map,X)
            cycle += 1
            X += int(V)

for i in range(6):
    print(''.join(screen_map[i*40:(i+1)*40]))