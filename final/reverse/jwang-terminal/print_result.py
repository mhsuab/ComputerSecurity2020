import sys

with open(sys.argv[1], 'rb') as f:
    raw = f.read()

print (raw.decode())