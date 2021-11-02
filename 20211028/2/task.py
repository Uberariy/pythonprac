import itertools
def slide(seq, n):
	for i in range(len(seq)):
		yield from itertools.islice(seq, i, i+n)

import sys
exec(sys.stdin.read())
