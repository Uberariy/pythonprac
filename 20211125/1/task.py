#TODO tests
import sys
l = sys.stdin.buffer.read()
N = l[0]
o = l[0:1]
l = l[1:]
s = sorted([l[i:i+len(l)//N+1] for i in range(N)])
sys.stdout.buffer.write(s[0])

for i in s:
	o += i
sys.stdout.buffer.write(o)



