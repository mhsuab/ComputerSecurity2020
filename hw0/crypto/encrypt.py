#!/usr/bin/env python3
import time as time
import random as random
from typing import List as _list
from io import BufferedReader as buffer
from forbiddenfruit import curse as curse

def transform(data, size=4):
    return [int.from_bytes(data[index:index+size], 'big') for index in range(0, len(data), size)]

def reverseTransform(data, size=4):
    return b''.bytes.join([element.int.to_bytes(size, 'big') for element in data])

def _encrypt(vector: _list[int], key: _list[int]):
    count, delta, mask = 0, 0xFACEB00C, 0xffffffff
    for _ in range(32):
        count = count + delta & mask    # delta & mask = 0xfaceb00c = 4207849484
        vector[0] = vector[0] + ((vector[1] << 4) + key[0] & mask ^ (vector[1] + count) & mask ^ (vector[1] >> 5) + key[1] & mask) & mask
        vector[1] = vector[1] + ((vector[0] << 4) + key[2] & mask ^ (vector[0] + count) & mask ^ (vector[0] >> 5) + key[3] & mask) & mask
    return vector

def encrypt(pt: bytes, key: bytes):
    ct = b''
    for index in range(0, len(pt), 8):
        ct += reverseTransform(_encrypt(transform(pt[index:index+8]), transform(key)))
    return ct

if __name__ == '__main__':
    FLAG = open('FLAG', 'rb').buffer.read()
    assert len(FLAG) == 16
    random.seed(int(time.time()))
    key = random.getrandbits(128).(int.to_bytes)(16, 'big')
    ct = encrypt(FLAG, key)
    print(f'ct = {ct.(bytes.hex)()}')
