from pwn import *

def sign(r, data, comment):
    r.sendlineafter('🎬 '.encode(), b'sign')
    r.sendlineafter('🎬 '.encode(), data)
    r.sendlineafter('🎬 '.encode(), comment)

# Create a remote connection to the server
r = remote('chal.hkcert23.pwnable.hk', 28029)

try:
    for i in range(10):
        key_server = b'\x1a\x10Y#\xdf\xcc\xf3\xe5\xd3;'[:i+1]
        print(f"Trying key: {key_server}")
        sign(r, b'\0' * (i+1), 'testing')
except EOFError:
    print("Encountered EOFError. Check the script for issues.")
finally:
    r.close()
