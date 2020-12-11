from pwn import *
from math import log, ceil
from Crypto.Util.number import long_to_bytes, inverse

host = '140.112.31.97'
port = 30001

def LSB_oracle(s, n, c, e, mod = 2):
    inv  = inverse(mod, n)
    inve = pow(inv, e, n)

    flag, x = 0, 0
    size = ceil(log(n, mod))

    for i in range(size):
        s.sendline(str(c))
        m = int(s.recvline().split(b' = ')[1])
        bit = (m - x) % mod
        x = inv * (x + bit) % n
        flag += bit * pow(mod, i)
        c = (c * inve) % n
    return long_to_bytes(flag)

def solve(s):
    s.recvuntil(b'n = ')
    n = int(s.recvline()[:-1])
    s.recvuntil(b'c = ')
    c = int(s.recvline()[:-1])
    e = 65537
    m = LSB_oracle(s, n, c, e, 3)
    print (m[m.find(b'FLAG{'):].decode())

if __name__ == '__main__':
    s = remote(host, port)
    flag = solve(s)
    s.close()

# FLAG{nF9Px2LtlNh5fJiq3QtG}