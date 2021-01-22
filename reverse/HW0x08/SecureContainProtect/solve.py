'''
solve sudoku https://www.sudokuwiki.org/sudoku.htm
flag => FLAG{oh_my_g0d_hoo0ow_did_you_decrypt_this???}
ACTION NOTE => decrypt_the_document_of_SCP-2521
'''
from string import printable, ascii_uppercase, digits, ascii_lowercase
from itertools import cycle
from time import sleep
from tqdm import tqdm

binary = open('./sudoku', 'rb')
OFFSET = 0x200000
ans_sudo = b'812753649943682175675491283154237896369845721287169534521974368438526917796318452'
ans_sudo = b''.join(bytes([i - 48]) for i in ans_sudo)

bxor = lambda b1, b2: bytes(a ^ b for a, b in zip(b1, cycle(b2)))

'''
SUDOKU
'''
binary.seek(0x1270)
print (binary.read(0x1763 - 0x1270).decode())

'''
check XOR with byte_2020E0
result of sum should be 0xFFFD09F2 = 4294773234
'''
binary.seek(0x2020E0 - OFFSET)
byte_2020E0 = binary.read(3161)
# print (bxor(byte_2020E0, ans_sudo).decode())

'''
check XOR with byte_202D40
result of sum should be 0x39AB = 14763
'''
binary.seek(0x202D40 - OFFSET)
byte_202D40 = binary.read(169)
# print (bxor(byte_202D40, ans_sudo).decode())

'''
XOR byte_202E00 and ans_sudo
'''
binary.seek(0x202E00 - OFFSET)
byte_202E00 = binary.read(6015)
CT = bxor(byte_202E00, ans_sudo)

binary.close()

# guess due repeated pattern in CT
LENGTH = 32
block = [CT[k:k+LENGTH] for k in range(0, len(CT), LENGTH)]
ascii_range = [i for i in range(128)]
printable_range = [ord(i) for i in printable[:-3]]

d = {i: [] for i in range(LENGTH)}
for i in printable_range:
    t = (bxor(CT, bytes([i])))
    tt = [t[k:k+LENGTH] for k in range(0, len(t), LENGTH)]
    for j in range(LENGTH):
        flag = True
        for k in tt[:-1]:
            if k[j] not in printable_range:
                flag = False
                break
        if flag:
            d[j].append(chr(i))

for i in d:
    print (i, d[i])

addr = 0x4c0
for i in printable_range:
    tmp = bxor(CT[addr:addr + LENGTH], bytes([i]))
    if (chr(tmp[-1]) in d[31]):
        print (i, tmp)

print (bxor(CT, b'decrypt_the_document_of_SCP-2521').decode())

# while True:
#     print (CT[addr: addr + LENGTH])
#     for i in printable_range:
#         print (bytes([i]), bxor(CT[addr: addr + LENGTH], bytes([i])))
#     for i in range(LENGTH):
#         print (i%10, end='')
#     print ('')
#     tmp = input('.' * LENGTH + '\b' * LENGTH)
#     _length = len(tmp)
#     tmp = tmp.encode()
#     if _length < LENGTH:
#         tmp += b'\x00' * (LENGTH - _length)
#     tmp = bxor(CT, tmp)
#     kk = [tmp[k:k+LENGTH] for k in range(0, len(tmp), LENGTH)]
#     print (tmp.decode())

# for i in printable_range:
#     tmp = bxor(CT, bytes([i]))
#     kk = [tmp[k:k+LENGTH] for k in range(0, len(tmp), LENGTH)]
#     for i in kk[:50]:
#         print (i)
