'''
each monkey
    - yell a specific number (know it in advance)
    - yell result of a math operation (need to wait for other 2 monkeys)

What will root yell?
    - back calculate to identify the parameters used by root.

Lone number here basically form leaf of the tree. 

(root) ---> pppw --
       ---> sjmn
'''
import re

class Node:
    def __init__(self, name, val=None, left=None, right=None, parent = None, op = None):
        self.name = name
        self.left = left
        self.right = right
        self.parent = parent
        self.op = op
        self.val = val


seen = {}

filename = 'input.txt'
with open(filename, encoding='utf-8') as f:
    for line in f:
        data = [s for s in re.findall(r"[a-z]{4}|\d+|[+]|[-]|[/]|[*]", line)]
        if len(data) != 2: #tree node
            pname, lname, op, rname = data
            if pname not in seen:
                seen[pname] = Node(pname)

            if lname not in seen:
                seen[lname] = Node(lname)

            if rname not in seen:
                seen[rname] = Node(rname)

            seen[pname].left = seen[lname]
            seen[pname].right = seen[rname]
            seen[pname].op = op
            seen[lname].parent = seen[pname]
            seen[rname].parent = seen[pname]
        else:
            pname,val = data
            if pname not in seen:
                seen[pname] = Node(pname)
            seen[pname].val = int(val)


def recurse(node):
    
    if node.op == '+':
        node.val = (recurse(node.left) + recurse(node.right))

    if node.op == '-':
        node.val = (recurse(node.left) - recurse(node.right))

    if node.op == '*':
        node.val = (recurse(node.left) * recurse(node.right))

    if node.op == '/':
        node.val =  (recurse(node.left) / recurse(node.right))
    
    return node.val


#recurse(seen['root'].left) == recurse(seen['root'].right)
print(recurse(seen['root']))


start_name = 'humn'
path = [start_name]
# find the path to root for humn
while start_name != 'root':
    next_name = seen[start_name].parent.name
    path.append(next_name)
    start_name = next_name

print(path)

# we know 
print(seen['root'].left.val, seen['root'].right.val)
print(seen['root'].left.name, seen['root'].right.name)


seen['root'].op = '=='
currnode = seen['root']

def functionleft(node, rnode, op):
    if op == '==':
        return rnode.val
    if op == '+':
        return node.val - rnode.val
    if op == '-':
        return node.val + rnode.val
    if op == '*':
        return node.val / rnode.val
    if op == '/':
        return node.val * rnode.val

def functionright(node, lnode, op):
    if op == '==':
        return lnode.val
    if op == '+':
        return node.val - lnode.val
    if op == '-':
        return lnode.val - node.val
    if op == '*':
        return node.val / lnode.val
    if op == '/':
        return lnode.val / node.val

while currnode.name != 'humn':
    # check if left or right in path
    left, right = currnode.left, currnode.right
    if left.name in path:
        expected_val = functionleft(currnode, currnode.right, currnode.op)
        left.val = expected_val
        currnode = left
    else:
        expected_val = functionright(currnode, currnode.left, currnode.op)
        right.val = expected_val
        currnode = right


print(currnode.val)