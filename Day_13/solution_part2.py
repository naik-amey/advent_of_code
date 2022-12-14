from collections import deque
import functools
filename = 'input.txt'

'''
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
        if len(left) < len(right):
            return -1
        elif len(left) > len(right):
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
            return -1
        elif left > right:
            return 1
        else:
            return 0


score = 0    

with open(filename, encoding='utf-8') as f:
    content = f.readlines()
    nol = len(content)//3  + 1
    data_arr = []
    for i in range(nol):
        left = json.loads(content[3*i])
        right = json.loads(content[3*i + 1])
        data_arr.append(left)
        data_arr.append(right)

        if compare(left, right) == 1:
            print(i+1)
            score += (i+1)


# use lambda function for sorting. 
data_arr.append([[2]]) 
data_arr.append([[6]]) 
data_arr.sort(key=functools.cmp_to_key(compare))
a = data_arr.index([[2]]) + 1
b = data_arr.index([[6]]) + 1

print(f"Mul a*b = {a*b}")

