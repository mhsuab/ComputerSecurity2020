from pwn import *
import codecs

host = '140.112.31.97'
port = 30000

BS = 16

def bxor(b1, b2):
    return bytes(a ^ b for a, b in zip(b1, b2))

def PaddingOracle(s, ivNct, ivNcts, blockIdx):
    I = b'\x00' * BS
    for i in range(BS):
        for j in range(256):
            tmp = (i * b'\x00')
            mod = ivNct[:BS * (blockIdx - 1)] + I[:(15 - i)] + bytes([j]) + bxor(I[(BS - i):], tmp) + ivNcts[blockIdx]
            mod = mod.hex()
            s.sendline(mod)
            stat = s.recvline()
            s.recvuntil(b' = ')
            if b'NOOOOOOOOO' not in stat:
                I = I[:(15-i)] + bxor(bytes([j]), b'\x80') + I[(16 - i):]
                print (I)
                break
    pt = bxor(ivNcts[blockIdx - 1], I)
    print (blockIdx, pt)
    return pt, I

def get_ptNi(s, ivNct, ivNcts, totalBlocks = 3):
    pt_s, i_s = b'', b''
    for j in range(1, totalBlocks + 1):
        pt, i = PaddingOracle(s, ivNct, ivNcts, j)
        pt_s += pt
        i_s += i_s
        print (pt_s)
    return pt_s, i_s

def solve(s):
    s.recvuntil(b' = ')
    ct_hex = s.recvline()[:-1].decode()
    ct = codecs.decode(ct_hex.encode(), 'hex')
    ivNcts =  [ ct[i:i+BS] for i in range(0, len(ct), BS) ]
    pt, inter = get_ptNi(s, ct, ivNcts, 2)
    pt = pt[:pt.find(b'}') + 1].decode()
    print (pt)

if __name__ == '__main__':
    s = remote(host, port)
    solve(s)
    s.close()

# FLAG{31a7f10f1317f622}