'''
  Decimal          SNAFU
        1              1
        2              2
        3             1=
        4             1-
        5             10
        6             11
        7             12
        8             2=
        9             2-
       10             20
       15            1=0
       20            1-0
     2022         1=11-2
    12345        1-0---0
314159265  1121-1110-1=0

8 
8 % 5 = 3 (5 - 3 = -2)
8 / 5 = 1 
2-2

2022
   1=11-2
2022 % 5 = 2
2022 / 5 = 404
404 % 5 = -1
404 // 5 
81 % 5 = 1
16 % 5 = 1
'''
filename = 'input.txt'

def decode(data):
    data_b10 = 0
    for i,ch in enumerate(data[::-1]):
        if not(ch.isnumeric()):
            d = -1 if ch == '-' else -2
        else:
            d = int(ch)
        data_b10+=(d*(5**i))
    return data_b10


def encode(data):
    num = data
    s = []
    while num:
        r = num % 5
        if r < 3:
            s += (str(r))
        else:
            if r - 5 == -1:
                s += '-'
            else:
                s += '='
        num = num // 5
        if s[-1] in ['-', '=']:
            num += 1
    return s[::-1]

score = 0
with open(filename, encoding='utf-8') as f:
    for line in f:
        data = [ch for ch in line.strip()]
        data_b10 = decode(data)
        #print(data_b10)
        score += data_b10
    out = ''.join(encode(score)) 
    print(f'Final answer is {score} in base 5 {out}')
