'''
Bypass ptrace https://gist.github.com/poxyran/71a993d292eee10e95b4ff87066ea8f2
'''

import struct
from string import ascii_uppercase, digits

ct = [0x55,0x33,0x46,0x44,0x6B,0x2E,0x11,0x69,0x6D,0x3D,0x43,0x70,0x6A,0x1D,0x6A,0x44,0x2E,0x5E,0x69,0x33,0x1A,0x6D,0x1A,0x16,0x2C,0x7B,0x5C,0x6F,0x23,0x40,0x67,0x37,0x39,0x65,0x21,0x64,0x2F,0x2A,0x74,0x49,0x77,0x62,0x2A,0x7D,0x26,0x03,0x26,0x32,0x41,0x63,0x4D,0x10,0x22,0x24,0x0F,0x2A,0x37,0x0A,0x5C,0x38,0x2C,0x31,0x41,0x3D,0x76,0x52,0x58,0x1B,0x5B,0x1F]
ct = b''.join(bytes([i]) for i in ct)

DWORD = ['I', 4]
QWORD = ['Q', 8]
LENGTH = 70

bxor = lambda b1, b2: bytes(a ^ b for a, b in zip(b1, b2))

characters = (ascii_uppercase + digits).encode()

def sub_4011d6(_input):
    v3 = 0
    v4 = 1
    for j in range(_input):
        v1 = (v3 + v4) & 0xffffffff
        v3 = v4
        v4 = v1
    return v1
dict_4011d6 = {sub_4011d6(i):i for i in characters}

def sub_40102d(_input):
    v1 = 0
    for i in range(_input):
        if (i & 1):
            v1 += 2
        else:
            v1 += 11
    return v1
dict_40102d = {sub_40102d(i):i for i in characters}

def sub_401138(_input):
    v1 = 0xFAC0B00C
    for i in range(_input):
        if (i & 1):
            v1 -= 0x78
        else:
            v1 -= 0x7788
    return v1
dict_401138 = {sub_401138(i):i for i in characters}

def sub_4010C8(_input):
    return _input ^ 0x52756279
dict_4010C8 = {sub_4010C8(i):i for i in characters}

def sub_400FBE(_input):
    return _input * 135
dict_400FBE = {sub_400FBE(i):i for i in characters}

val2func = {4198870: dict_4011d6, 4198445: dict_40102d, 4198712: dict_401138, 4198600: dict_4010C8, 4198334: dict_400FBE}

binary = open('wishMachine', 'rb')

OFFSET = 0x600000
dword_8A1070 = 0
INPUT = [b'_' for i in range(LENGTH)]

def addr2int(addr, t):
    binary.seek(addr - OFFSET)
    data = binary.read(t[1])
    return struct.unpack('<' + t[0], data)[0]

for k in range(1000):
    i = 0
    while i <= 69:
        dword_8A2114 = addr2int(0x6D5114 + 40 * dword_8A1070, DWORD)
        dword_8A2118 = addr2int(0x6D5118 + 40 * dword_8A1070, DWORD)
        dword_8A211C = addr2int(0x6D511C + 40 * dword_8A1070, DWORD)
        dword_8A2120 = addr2int(0x6D5120 + 40 * dword_8A1070, DWORD)
        dword_8A2110 = addr2int(0x6D5110 + 40 * dword_8A1070, DWORD)
        qword_8A2100 = addr2int(0x6D5100 + 40 * dword_8A1070, QWORD) + dword_8A2110
        dword_8A1070 += 1
        i += dword_8A2118

        for j in range(dword_8A2118):
            if j == 0:
                INPUT[dword_8A2114 + j] = val2func[qword_8A2100][dword_8A211C]
            elif j == 1:
                INPUT[dword_8A2114 + j] = val2func[qword_8A2100][dword_8A2120]
            else:
                raise ValueError

    ct = bxor(b''.join(bytes([i]) for i in INPUT), ct)

binary.close()
print (ct.decode())