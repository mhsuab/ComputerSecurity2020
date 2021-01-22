'''
main_rchvf
    Extended Euclidean algorithm -> guess?!

IDA Python
addrb = 0x4d23c0
addra = 0x4d22a0

array_a = []
array_b = []
for i in range(36):
    array_a.append(idc.Qword(addra))
    array_b.append(idc.Qword(addrb))
    addra += 8
    addrb += 8
'''

array_a = [3371804713, 3968017934, 2945697524, 1511754201, 837192973, 3280791527, 3371804713, 1257148539, 3759376991, 837192973, 160915013, 3509185091, 3330476591, 3371804713, 3968017934, 3968017934, 331295615, 3759376991, 3826889091, 3002195387, 3280791527, 3280791527, 2439222292, 1511754201, 837192973, 2353382065, 209109856, 141983835, 2372394284, 3256014716, 3968017934, 1511754201, 3852305411, 1998866177, 345601562, 3949286142]
array_b = [15, 32, 1, 29, 23, 18, 14, 31, 26, 8, 27, 2, 16, 20, 21, 34, 19, 28, 24, 22, 5, 7, 3, 25, 6, 0, 13, 12, 30, 11, 33, 9, 35, 10, 17, 4]

from sympy import mod_inverse
flag = [''] * 36
for i in range(36):
    flag[array_b[i]] = chr(mod_inverse(array_a[i], 0xfbc56a93))
print (''.join(flag))