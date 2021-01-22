from pwn import *
import subprocess

host = '140.112.31.97'
port = 30002

def solve(s):
    subprocess.run(['node', './../getStarted.js'])
    s.recvuntil(b'validate(')
    validate_address = s.recvuntil(b')')[:-1].decode()
    print (validate_address)
    s.recvuntil(b'----- flag will appear below -----\n')
    subprocess.run(['node', './../validate.js', validate_address])
    print (s.recvline()[:-1].decode())

if __name__ == '__main__':
    s = remote(host, port)
    solve(s)
    s.close()