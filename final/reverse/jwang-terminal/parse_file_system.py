import os
dump_files = 'files'
if not os.path.isdir(dump_files):
    os.mkdir(f'{dump_files}')
file_system = 'raw.bin'

def save_file(name, data):
    with open(f'{dump_files}/{name}', 'wb') as f:
        f.write(data)

with open(f'{file_system}', 'rb') as f:
    raw = f.read()

curr = 0
i = 0
while True:
    next_ptr = raw.find(b'\x00', curr)
    filename = raw[curr:next_ptr]
    if filename == b'README.txto\x01' or filename[-2:] == b' \x1b':
        filename = filename[:-2].decode()
        print (f'{filename}\r', end='')
        curr = next_ptr + 2
        next_ptr = raw.find(b'\x00' * 4, next_ptr)
        save_file(filename, raw[curr: next_ptr])
        curr = next_ptr + 10
    elif filename == b'Deprogrammer\xd0':
        curr = next_ptr + 3
        next_ptr = raw.find(b'\x00' * 4, next_ptr)
        save_file(filename, raw[curr: next_ptr])
        exit()
    else:
        # folder
        curr = next_ptr + 14
