import bcrypt
import sys

if len(sys.argv) < 2:
    raise Exception('Value to hash is required')

raw_value = bytes(sys.argv[1], 'utf-8')
hashed = bcrypt.hashpw(raw_value, bcrypt.gensalt())
print(hashed.decode('utf-8'))