from collections import deque
filename = 'input.txt'

# part 1
#LEN = 4
# part 2
LEN = 14

with open(filename,'r') as f:
    for line in f:
        line = line.strip()
        chr = deque()
        for r in range(len(line)):
            if r < LEN-1:
                chr.append(line[r])
                continue
            
            chr.append(line[r])
            ulen = len(set(chr))
            if ulen == LEN:
                print(f"start index is {r+1}")
                break
            chr.popleft()
