mixedIdx = [0xf,0x20,0x1,0x1d,0x17,0x12,0xe,0x1f,0x1a,0x8,0x1b,0x2,0x10,0x14,0x15,0x22,0x13,0x1c,0x18,0x16,0x5,0x7,0x3,0x19,0x6,0x0,0xd,0xc,0x1e,0xb,0x21,0x9,0x23,0xa,0x11,0x4]

dump = ['29a8f9c8', '0e2683ec', 'f4c693af', 'd9891b5a', '0d8de631', 'e7e78cc3', '29a8f9c8', '7b90ee4a', '5f8a13e0', '0d8de631', '455e9709', '43ea29d1', '2f0a83c6', '29a8f9c8', '0e2683ec', '0e2683ec', '7f2bbf13', '5f8a13e0', '83b119e4', 'bbddf1b2', 'e7e78cc3', 'e7e78cc3', '14946391', 'd9891b5a', '0d8de631', 'b1c2458c', '60c3760c', '5b807608', '2cdd678d', '7cd712c2', '0e2683ec', 'd9891b5a', '03849de5', '01472477', '1a769914', 'fe5265eb']
qword_4D22A0 = []
for i in dump:
    qword_4D22A0.append('0x' + ''.join(k for k in [i[j: j + 2] for j in range(0, len(i) , 2)][::-1]))

d = {'0xc212d77c': 48,
    '0x148d80dd': 49,
    '0xc461aa2b': 50,
    '0x13bf2b7f': 51,
    '0xbbe3907d': 67,
    '0xc6830a2f': 52,
    '0x390139f1': 53,
    '0x748f8b6a': 54,
    '0x2932ec34': 55,
    '0xee488e02': 56,
    '0x962de5bf': 57,
    '0xade75eba': 97,
    '0x882975b8': 98,
    '0xf6af53bc': 99,
    '0xe0138a5f': 100,
    '0xc76c360': 101,
    '0x87c24b09': 102,
    '0xc38ce7e7': 103,
    '0xe1243a61': 104,
    '0x9975e45': 105,
    '0x9a635242': 106,
    '0x6c3cf201': 107,
    '0x3a47c5b5': 108,
    '0x5c64a13d': 109,
    '0x1499761a': 110,
    '0x31e68d0d': 111,
    '0x77244701': 112,
    '0xc411cf99': 113,
    '0xc8f9a829': 114,
    '0x348b25d3': 115,
    '0x95c2ab88': 116,
    '0xe419b183': 117,
    '0x977d4af9': 118,
    '0x876805b': 119,
    '0xe4b12fbd': 120,
    '0xb2f1ddbb': 121,
    '0xb7ab4ba6': 122,
    '0xd129ea43': 65,
    '0x76419307': 66,
    '0xbbe3907d': 67,
    '0x4dc0bb44': 68,
    '0x3a61b84': 69,
    '0x8c45c2b1': 70,
    '0x91639414': 71,
    '0xd54e5dd9': 72,
    '0x8d67dd2c': 73,
    '0xc8bc88dd': 74,
    '0xd6d83fa3': 75,
    '0xaf93c6f4': 76,
    '0xad4c0a30': 77,
    '0xd843d4fb': 78,
    '0x8f69f8a8': 79,
    '0xd9271252': 80,
    '0x4db5079c': 81,
    '0x655291ea': 82,
    '0x3699d96d': 83,
    '0x4aee907b': 84,
    '0xbd91a19': 85,
    '0x31c4caa6': 86,
    '0x73c1c12f': 87,
    '0x97a288ea': 88,
    '0x87c964a': 89,
    '0xdcffc6cb': 90,
    '0xec83260e': 33,
    '0x9b817688': 34,
    '0x1cc61acf': 35,
    '0xaed7511f': 36,
    '0x95b3a727': 37,
    '0x63622355': 38,
    '0xb4c23f63': 39,
    '0xb688ba11': 40,
    '0xcaa523d4': 41, 
    '0x95dd20f6': 42,
    '0x6389954c': 43,
    '0x337fa741': 44,
    '0xbe3a2303': 45,
    '0x5792946': 46,
    '0xb621e029': 47,
    '0x2fbfec7d': 58,
    '0x33352b5f': 59,
    '0xcd9cf4e7': 60,
    '0x73912cb9': 61,
    '0xb6bcb494': 62,
    '0x63e8c0a4': 63,
    '0x918e219d': 64,
    '0xb95eb68e': 91,
    '0x2bc94a3': 92,
    '0xcdbf9be9': 93,
    '0xd8f3a55e': 94,
    '0x5a1b89d9': 95,
    '0x61096bbe': 96,
    '0xeb6552fe': 123,
    '0x5b5e5a4a': 124,
    '0xe59d8403': 125}

def check():
    count = 0
    for i in range(len(qword_4D22A0)):
        try:
            t = d[hex(int(qword_4D22A0[i], 16))]
            # print (t, chr(t))
        except:
            print (i, qword_4D22A0[i])
            count += 1
            # break
    print ('remain:', count)

flag = [''] * 36
for i in range(36):
    flag[mixedIdx[i]] = chr(d[hex(int(qword_4D22A0[i], 16))])
print (''.join(i for i in flag))