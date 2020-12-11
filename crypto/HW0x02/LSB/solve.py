from pwn import *
from math import log, ceil
from Crypto.Util.number import long_to_bytes

host = '140.112.31.97'
port = 30001

def LSB_oracle(s, n, c, e):
    _3e = pow(3, e, n)
    size = ceil(log(n, 3))
    L, R = 0, 1
    for i in range(size):
        print (str(i).rjust(3, '0'), end='\b' * 3)
        c = (c * _3e) % n
        s.sendline(str(c))
        m = int(s.recvline().split(b' = ')[1])
        L, R = L * 3, R * 3
        if m == 0:
            R -= 2
        elif m == 1:
            R -= 1
            L += 1
        else:
            L += 2
    return long_to_bytes(R * n // pow(3, size))

def solve(s):
    s.recvuntil(b'n = ')
    n = int(s.recvline()[:-1])
    s.recvuntil(b'c = ')
    c = int(s.recvline()[:-1])
    e = 65537
    m = LSB_oracle(s, n, c, e)
    index = m.find(b'FLAG{')
    if index == -1:
        return False
    else:
        print (m[index:].decode())
        return True

if __name__ == '__main__':
    flag = False
    while not flag:
        s = remote(host, port)
        flag = solve(s)
        s.close()

# FLAG{nF9Px2LtlNh5fJiq3QtG}