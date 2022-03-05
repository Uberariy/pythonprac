import readline
import shlex

while s := input('> '):
    l = s.split()
    print(*l[1:])
    if (int(l[0]) > len(l)-1) or (int(l[0]) < 0):
        break
