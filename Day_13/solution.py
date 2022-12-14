from collections import deque
filename = 'input.txt'

'''
If left.val < right.val : validcase break. (1)
   left.val == right.val : continue to next 
   left.val > right.val ; invalidcase break

If left.islist && right.islist 
    - break left and right lists. 
    - now if left.int and right is int (invoke) ---- 1

'''

import json

def compare(left, right):
    if type(left) is list and type(right) is list:
        minlen = min(len(left), len(right))

        for i in range(minlen):
            res = compare(left[i], right[i])
            if res == -1:
                return -1
            elif res == 1:
                return 1
        if len(left) > len(right):
            return -1
        elif len(left) < len(right):
            return 1
        else: 
            return 0
    elif type(left) is list:
        right = [right]
        return compare(left, right)
    elif type(right) is list:
        left = [left]
        return compare(left, right)
    else:
        if left < right:
            return 1
        elif left > right:
            return -1
        else:
            return 0


score = 0    

with open(filename, encoding='utf-8') as f:
    content = f.readlines()
    nol = len(content)//3  + 1
    for i in range(nol):
        left = json.loads(content[3*i])
        right = json.loads(content[3*i + 1])

        if compare(left, right) == 1:
            print(i+1)
            score += (i+1)

print(f'score = {score}')
        

