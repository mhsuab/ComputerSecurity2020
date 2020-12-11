import sys

with open(sys.argv[1], 'r') as f:
    ipnports = [(i.replace(':', ' ')).split() for i in f.readlines()]

def parseIP(ip):
    tmp = [ip[i:i+2] for i in range(0, len(ip), 2)][::-1]
    return '.'.join(str(int(i, 16)) for i in tmp)

def parse(ipnport):
    t = parseIP(ipnport[0])
    # if t[:3] == '127':
    #     return ''
    tmp = [t, str(int(ipnport[1], 16)), parseIP(ipnport[2]), str(int(ipnport[3], 16))]
    return '\t'.join(i for i in tmp)

# s = ''
# for i in ipnports:
#     tmp = parse(i)
#     if tmp:
#         s += (tmp + '\n')

with open(sys.argv[2], 'w') as f:
    f.write('\n'.join(parse(i) for i in ipnports))