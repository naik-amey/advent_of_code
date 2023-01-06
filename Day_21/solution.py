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
    if node.val is not None:
        return node.val
    
    if node.op == '+':
        return (recurse(node.left) + recurse(node.right))

    if node.op == '-':
        return (recurse(node.left) - recurse(node.right))

    if node.op == '*':
        return (recurse(node.left) * recurse(node.right))

    if node.op == '/':
        return (recurse(node.left) / recurse(node.right))


print(recurse(seen['root']))

