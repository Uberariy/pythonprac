
import sys
wav = sys.stdin.buffer.read()

import struct
f = "4sIf"
st = struct.pack(f, wav)

'''
>>> import pickle
>>> s = "QWERQWER"
>>> pickle.dumps(s)
b'\x80\x04\x95\x0c\x00\x00\x00\x00\x00\x00\x00\x8c\x08QWERQWER\x94.'
>>> pickle.dumps(s, 0)
b'VQWERQWER\np0\n.'
>>> pickle.dumps(2121, 0)
b'I2121\n.'
>>> pickle.dump
<built-in function dump>
>>> f = open("dump", "wb")
>>> pickle.dump("qwerqwr", f)
>>> pickle.dump([43,43,43,54], f)
>>> f.close()
>>> f.close()
>>> 
>>> 
>>> 
>>> import struct
>>> f = "I4sf"
>>> struct.calcsize(f)
12
>>> struct.pack(f,0x1234,b'QWER',12.54)
b'4\x12\x00\x00QWER\xd7\xa3HA'
>>> struct.pack(f,0xabcdefad,b'QWER',12.54)
b'\xad\xef\xcd\xabQWER\xd7\xa3HA'
>>> r = struct.pack(f,0xabcdefad,b'QWER',12.54)
>>> struct.unpack(f, r)
(2882400173, b'QWER', 12.539999961853027)
>>> 

'''
