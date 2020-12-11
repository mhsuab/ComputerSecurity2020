import sys
from base64 import b64decode

with open(sys.argv[1], 'r') as f:
    _file = f.read()

with open(sys.argv[2], 'w') as f:
    f.write(b64decode(_file).decode())
