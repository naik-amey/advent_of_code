from collections import deque
filename = 'input.txt'

'''
tree DS
'''
class Node:
    def __init__(self, name,size=0,parentNode=None):
        self.name = name
        self.size = size
        self.parent = parentNode
        self.children = {}

'''
1. build the tree. 
2. update the size of each dir. Go back to root, 
    each time you go back, update the dir size.
    -   while you update the dir size, create a list which holds (3)
        3. find the dirs with size at most X; sum their total
'''
SIZELIMIT = 100000
currNode = None
with open(filename,'r') as f:
    for line in f:
        line = line.strip().split(' ')
        if line[0] == '$': # its a cmd
            if line[1] == 'cd':
                if line[2] != '..': # enter a new node
                    if line[2] == '/': # create a new node only if '/'
                        currNode = Node(line[2])
                        rootNode = currNode
                    else:
                        currNode = currNode.children[line[2]]
                else: # '..' go back to parent node
                    currSize = 0
                    for childNode in currNode.children.values():
                        currSize += childNode.size
                    currNode.size += currSize
                    currNode = currNode.parent
            else: # ls
                # add children (files and dir) # do nothing?
                None
        else: # list of file names and dir
            # add children as node
            if line[0] == 'dir':
                currNode.children[line[1]] = Node(line[1],0,parentNode=currNode)
            else:
                currNode.children[line[1]] = Node(line[1],int(line[0]),parentNode=currNode)

            
        # two type of text:
        #   cmds, 
        #     1. cd
        #     2. ls
        #   text,
        #     1. size filename
        #     2. dir dirname

# now do BFS to get the dir below SIZELIMIT

while currNode is not None:
    currSize = 0
    for childNode in currNode.children.values():
        currSize += childNode.size
    currNode.size += currSize
    currNode = currNode.parent

freeSpace = 70000000 - rootNode.size
if freeSpace >= 30000000:
    print("Nothing needs to be Deleted.")
else:
    SIZELIMIT = 30000000 - freeSpace

q = deque()
q.append(rootNode)
res = []

while (q):
    currNode = q.popleft()

    for childNode in currNode.children.values():
        if len(childNode.children) != 0: # consider only dir
            q.append(childNode)
            if childNode.size >= SIZELIMIT:
                res.append(childNode.size)
        
print(f"Sum of directory sizes >= {SIZELIMIT} = {min(res)}")


