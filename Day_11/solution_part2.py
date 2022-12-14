from collections import deque
filename = 'input.txt'

'''
create a array of monkey objects. 
Read the input

item(m)

'''

class Monkey:
    def __init__(self, items, rule_op, rule_fac, test_fac, m_yes, m_no):
        self.items = deque([int(item) for item in items])
        self.rule_op = rule_op
        self.rule_fac = rule_fac
        self.test_fac = int(test_fac)
        self.m_yes = int(m_yes)
        self.m_no = int(m_no)
        self.cnt = 0
    def popleft(self):
        self.cnt += 1
        return self.items.popleft()
    def additem(self,item):
        self.items.append(item)
    def operate(self, item):
        factor = int(self.rule_fac) if (self.rule_fac.isnumeric()) else item
        if self.rule_op == '+':
            item = item + factor
        elif self.rule_op == '-':
            item = item - factor
        elif self.rule_op == '*':
            item = item * factor
        return item 
    def runtest(self, item): # return index of monkey it transfers to
        return self.m_yes if item % self.test_fac == 0 else self.m_no
        

monkeys = []

with open(filename,'r') as f:
    content = f.readlines()
    nofm = (len(content)//7) + 1

for i in range(nofm):
    items = content[i*7+1].strip().split(':')[1].split(',')
    rule_op = content[i*7+2][23]
    rule_fac = content[i*7+2].strip().split(rule_op)[1].strip()
    test_fac = content[i*7+3].strip().split('by')[1].strip()
    m_yes = content[i*7+4].strip().split('monkey')[1].strip()
    m_no = content[i*7+5].strip().split('monkey')[1].strip()
    monkeys.append(Monkey(items, rule_op, rule_fac, test_fac, m_yes, m_no))

TotalRounds = 10000

mod = 1
for m in range(nofm):
    mod *= monkeys[m].test_fac

for r in range(TotalRounds):
    if r % 100 == 0:
        print(f"current round {r}")
    for m in range(nofm):
        noi = len(monkeys[m].items)
        for _ in range(noi):
            item = monkeys[m].popleft()
            item = monkeys[m].operate(item)
            item = item % mod
            next_m = monkeys[m].runtest(item)
            monkeys[next_m].items.append(item)

for m in range(nofm):
    print(f'{m} : {monkeys[m].cnt}')

temp  = sorted([monkeys[m].cnt for m in range(nofm)])
print(f'Monkey Business score : {temp[-1]*temp[-2]}')