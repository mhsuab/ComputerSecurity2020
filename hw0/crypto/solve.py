from binascii import unhexlify
import time
import random

DAY = 86400
seed = int(time.time() - 10 * DAY)
NOW = int(time.time())
seed = 1599977586

hex_ct = "77f905c39e36b5eb0deecbb4eb08e8cb"
ct = unhexlify(hex_ct)

def transform(data, size=4):
    return [int.from_bytes(data[index:index+size], 'big') for index in range(0, len(data), size)]

def reverseTransform(data, size=4):
    return b''.join([element.to_bytes(size, 'big') for element in data])

def _decrypt(cts, key):
    count, delta, mask = 0, 0xFACEB00C, 0xffffffff
    last = 0x59d60180
    for _ in range(32):
        cts[1] = cts[1] - ((cts[0] << 4) + key[2] & mask ^ (cts[0] + last) & mask ^ (cts[0] >> 5) + key[3] & mask) & mask
        cts[0] = cts[0] - ((cts[1] << 4) + key[0] & mask ^ (cts[1] + last) & mask ^ (cts[1] >> 5) + key[1] & mask) & mask
        last = last - delta & mask
    return cts

def decrypt(seed, ct = ct):
    pt = b''
    random.seed(seed)
    key = random.getrandbits(128).to_bytes(16, 'big')
    for index in range(0, len(ct), 8):
        pt += reverseTransform(_decrypt(transform(ct[index:index + 8]), transform(key)))
    return pt

while seed < NOW:
    pt = decrypt(seed)
    print (pt, end = '\r')
    if b'flag{' in pt or b'FLAG{' in pt:
        print (str(seed) + ' ' * 64)
        print (pt)
        break
    seed += 1