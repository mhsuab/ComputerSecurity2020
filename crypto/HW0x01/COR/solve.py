# 75% of LFSR2, 3
# FLAG{...}
from output import KEY
from functools import reduce
from Crypto.Util.number import long_to_bytes
from string import printable
from itertools import product
from generate import LFSR

SIZE = 16
print (len(printable))
printable = printable[:-5]
print (len(printable))

def checkACU(cal, keystream = KEY):
    return sum([a ^ b for a, b in zip(cal, keystream)])/100

combineMethod = lambda x1, x2, x3: (x1 & x2) ^ ((not x1) & x3)

# test correlation rate
rate = [0.0 for i in range(3)]
for (i, j, k) in product([0, 1], [0, 1], [0, 1]):
    z = combineMethod(i, j, k)
    if i == z:
        rate[0] += 0.125
    if j == z:
        rate[1] += 0.125
    if k == z:
        rate[2] += 0.125

last = rate.index(min(rate))
brute = [i for i in range(3)]
brute.remove(last)

feedback = [[int(i) for i in f'{39989:016b}'], [int(i) for i in f'{40111:016b}'], [int(i) for i in f'{52453:016b}']]

dict4COR = [{}, {}, {}]
lfsr = [[] for _ in range(3)]

for i in product(printable, printable):
    flag = ''.join(s for s in i)
    print (flag, end='\r')
    init = [int(j) for j in f"{int.from_bytes(flag.encode(), 'big'):016b}"]
    for j in brute:
        lfsr[j] = LFSR(init, feedback[j])
        tmp = [lfsr[j].getbit() for _ in range(100)]
        if checkACU(tmp) < (1 - rate[j] + 0.05):
            dict4COR[j][flag] = tmp

for i in product(printable, printable):
    flag = ''.join(k for k in i)
    print (flag, end='\r')
    init = [int(j) for j in f"{int.from_bytes(flag.encode(), 'big'):016b}"]
    lfsr[last] = LFSR(init, feedback[last])
    tmp = [lfsr[last].getbit() for _ in range(100)]
    for flag2, flag3 in product(dict4COR[1].keys(), dict4COR[2].keys()):
        correct = True
        for (a, b, c, y) in zip(tmp, dict4COR[1][flag2], dict4COR[2][flag3], KEY):
            if combineMethod(a, b, c) != y:
                correct = False
                break
        if correct:
            print ('FLAG{' + flag + flag2 + flag3 + '}')
            exit()
