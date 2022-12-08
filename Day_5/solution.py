from collections import deque
from multiprocessing import Condition

filename = 'input.txt'

#1. read the stack values in multiple stacks till you hit the numbers. 
#2. start reading the cmds and makes changes to the stack accordingly. 
#3. read out the top values from the stack. --> return this.

class StackofCrates:
    # stack of stacks.
    def __init__(self, nos):
        self.len = nos
        self.st = [deque() for i in range(nos)]
    
    def appendleft(self, data, st_id):
        self.st[st_id].appendleft(data) # used only while reading the file.
    
    def push(self, data, st_id):
        self.st[st_id].append(data)
    
    def pop(self, st_id):
        return self.st[st_id].pop()
    
    def execute(self, quantity, from_st, to_st):
        for _ in range(quantity):
            self.st[to_st].append(self.st[from_st].pop())
        
    def execute_part2(self, quantity, from_st, to_st):
        temp = []
        for _ in range(quantity):
            temp.append(self.st[from_st].pop())
        self.st[to_st].extend(temp[::-1])
    
    def top(self, st_id):
        return self.st[st_id][-1]

not_cmd = True
init_run = True 
with open(filename,'r') as f:
    while (not_cmd):
        line = f.readline()

        # when to stop
        if line[1] == '1':
            not_cmd = False
            break

        if init_run:
            nos = (len(line))//4 # number of stacks
            stoc = StackofCrates(nos) # stack of crates
            init_run = False
        
        # read elements
        vals = [line[i+1:i+2] for i in range(0,len(line),4)]
        for i,val in enumerate(vals):
            if val != ' ':
                stoc.appendleft(val,i)
    
    f.readline() # blank line

    for line in f:
        line = line.strip()
        line = line.split(' ')
        quantity, from_st, to_st = int(line[1]), int(line[3])-1, int(line[5])-1
        # execute cmd
        # print(quantity, from_st, to_st)
        #stoc.execute(quantity, from_st, to_st)
        stoc.execute_part2(quantity, from_st, to_st)


# read top element from all of the stacks. 
res = ''
for i in range(nos):
    res+=stoc.top(i)

print(f"Top elements of stacks are {res}")