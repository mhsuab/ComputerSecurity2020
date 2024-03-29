from hashlib import md5
# from string import printable
from itertools import product
import sys

printable = 'Fabcdefghijklmnopqrstuvwxyz_}!LAG{'
targets = ["6bde0a2e4131eede7f7aef53687bc56d", "ca2555b00b694a2494b84b8ee911bc29", "50b92ea83fef034ce2a7f3fdb82aea73", "8cb08bb0651be649a777d6578672c881", "9c26df9ed253653eb1de64552bdd5a77", "bbc23f75304b877490b8b81cd10e64ff", "a2879a3a26467c43f039b0d224ec5c9e", "d850f04cdb48312a9be171e214c0b4ee", "cd22643b1c1627a0419a8a3ab0c9fb80", "f801f18ef1a5f4847863ed9e30544ef5", "e47390fe89658d45f3532d95dcc0c51e", "a90e199623c1c7b73301dd4b46346a02", "0e38ee4c606cf8aa5294f70e525a67b5", "38896c05de797867402b5a6bc816cd21", "f34e7e8b47404664968dd01536be8148", "5623a9bfaa9fdd31dc845be686f4f200", "ebdc04cdf7446ccb3b74ab493e8462f6", "94306df994fbde6bfe01920e4f269330"]
ans = ''
# target = sys.argv[1]
# if (len(sys.argv) == 4):
#     if (sys.argv[2] != '__'):
#         prev = sys.argv[2]
#     else:
#         prev = ''
#     end = sys.argv[3]
# elif (len(sys.argv) == 3):
#     prev = sys.argv[2]
#     end = ''
# else:
#     prev = ''
#     end = ''
prev = ''
end = ''
d = {}
for l in product(printable, repeat=(5 - len(prev) - len(end))):
    s = prev + ''.join(l) + end
    result = md5(s.encode()).hexdigest()
    print (f'{s}\t{result}\r', end='')
    if (result in targets):
        d[result] = s
        print (f'ANS: {s} for {result}')
        # input()

# if not ans:
#     print ('fail')
# else: print (f'ANS: {ans}')

for i in targets:
    print (d[i], end='')
print ()