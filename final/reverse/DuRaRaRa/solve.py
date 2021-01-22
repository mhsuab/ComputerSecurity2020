'''
use the memory dumped file, 04050000

6bde0a2e4131eede7f7aef53687bc56d -> FLAG{
ca2555b00b694a2494b84b8ee911bc29 -> wait_
50b92ea83fef034ce2a7f3fdb82aea73 -> what_
8cb08bb0651be649a777d6578672c881 -> are_y
9c26df9ed253653eb1de64552bdd5a77 -> ou_lo
bbc23f75304b877490b8b81cd10e64ff -> oking
a2879a3a26467c43f039b0d224ec5c9e -> _for_
d850f04cdb48312a9be171e214c0b4ee -> there
cd22643b1c1627a0419a8a3ab0c9fb80 -> _is_n
f801f18ef1a5f4847863ed9e30544ef5 -> othin
e47390fe89658d45f3532d95dcc0c51e -> g_ins
a90e199623c1c7b73301dd4b46346a02 -> ide_t
0e38ee4c606cf8aa5294f70e525a67b5 -> his_b
38896c05de797867402b5a6bc816cd21 -> m_hac
f34e7e8b47404664968dd01536be8148 -> ker_h
5623a9bfaa9fdd31dc845be686f4f200 -> acker
ebdc04cdf7446ccb3b74ab493e8462f6 -> _go_a
94306df994fbde6bfe01920e4f269330 -> way!}
'''
from itertools import cycle
bxor = lambda b1, b2: bytes(a ^ b for a, b in zip(b1, cycle(b2)))

secret = 'c35f2bca2f79dcf56c4863b89c80a97362a474546521780f878ac7651dead037f8380f4c51a73167f1957f164cd1866d2431aa540b53d462b4455abc7289a49f34a7fe7abc1b5715a2ece8bedf26366913431e915e03b55f838a34f725f508e10a06bbde480e4e68e30b3c39d017308070d1d1a8b500030188d3fd09e03bd8f065a345df725e158b52a806d14432979e5080d06a9fedc6af6b516175c4af22eb4cf2b11ae72dbf6ee061a17e283ba900018f38724d89f59c203351a0b2cf061ca6b9cfa80e24ca8141a67be5a6a10bab90084de1b0314a4c5319d6803ceda13f5bcf5f6f2908744f85bf5cfec245ed56fea2885bc4d7ef1acfb6d70d720f9e1e435d2529990c5ee0284627a2ca7f0ee83cb14c1dfab3ec40ed331ee5bbddff2e'
secret_bytes = bytearray.fromhex(secret)
print (len(secret_bytes))
print (len(secret_bytes)/16)

v11 = [0xA8, 0x1A, 0x80, 0x9F, 0xB0, 0x33, 0x8E, 0xEC, 0x42, 0x1F, 0xCE, 0x4B, 0x87, 0xCF, 0x5A, 0x52, 0x28, 0xDA, 0xED, 0x62, 0x63, 9, 0x42, 0x57, 0x68, 2, 0xB7, 0x99, 0x95, 0xF9, 0x82, 45, 0x4B, 0x52, 117, 0x7A, 0xAD, 4, 216, 0x26, 0]
v10 = [0xEB, 32, 220, 0xCA, 0xC3, 0x56, 0xFC, 0x9F, 0x1E, 0x6B, 0xAB, 57, 245, 0xB6, 0x34, 0x3B, 0x46, 0xB3, 0xDE, 0x5A, 0x56, 56, 118, 0xB, 0x2C, 0x67, 0xC4, 0xf2, 225, 0x96, 0xF2, 113, 45, 0x3E, 20, 0x1D, 131, 0x70, 0xA0, 82]
print (hex(len(v11)))

r = b''
for i, j in zip(v11, v10):
    r += bytes([i ^ j])
print (r)

v8 = [0xA8, 0x81, 0x21, 0xE4, 0x6E, 0x48, 0x32, 0x2B, 0x13, 0x32, 0x8C, 0xEB, 0xF4, 0xFB, 0x6C, 0x1E]
for i in [secret_bytes[i:i+16] for i in range(0, len(secret_bytes), 16)]:
    # print (bxor(i, v8).hex(), end='", "')
    print (bxor(i, v8).hex())