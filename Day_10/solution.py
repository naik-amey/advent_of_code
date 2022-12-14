filename = 'input.txt'

'''
X = 1, cnt = 0
read the instruction

if noop -> just increment the counter. 
if addx v -> increment counter by 2 and value of x by v
'''
X = 1
cycle = 1
Score = 0

cycles_of_interest = [20+i*40 for i in range(6)]

with open(filename,'r') as f:
    for line in f:
        line = line.strip()
        # FIXME: below code looks dirty
        if line == 'noop':
            cycle += 1
            if cycle in cycles_of_interest:
                Score += (cycle*X)
        else:
            instruction, V = line.split(' ')
            cycle += 1
            if cycle in cycles_of_interest:
                Score += (cycle*X)
            #print(f"Cycle {cycle} X = {X}")
            cycle += 1
            X += int(V)
            if cycle in cycles_of_interest:
                Score += (cycle*X)
        #print(f"Cycle {cycle} X = {X}")

print(f"Sum of scores at {cycles_of_interest} is {Score}")
