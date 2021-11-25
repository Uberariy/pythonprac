
import sys
l = sys.stdin.buffer.read()
N = l[0]
o = l[0:1]
l = l[1:]
seg = len(l)/N 
if seg > len(l)//N:
	seg = int(seg//1) + 1
else:
	seg = int(seg)
#print(seg*N, len(l), N, sorted([l[i:i+seg] for i in range(0, seg*N, seg)]))
s = sorted([l[i:i+seg] for i in range(0, seg*N, seg)])
sys.stdout.buffer.write(o)

for i in s:
	sys.stdout.buffer.write(i)



