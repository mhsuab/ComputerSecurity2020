import subprocess
from Crypto.Util.number import long_to_bytes

longFlag = int(subprocess.check_output(['node', 'private.js'])[:-1].decode()[2:], 16)
flag = long_to_bytes(longFlag)

print (flag[:flag.find(b'}') + 1].decode())