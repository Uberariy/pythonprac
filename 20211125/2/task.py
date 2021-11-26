import sys
inp = sys.stdin.buffer.read()
res = inp.decode().encode("latin-1").decode('cp1251').encode('utf8')
sys.stdout.buffer.write(res)