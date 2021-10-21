import math
d = {}
while True:
	l = input().split()
	if l[0][0] == ":":
		d[l[0][1::]] = [l[1], l[2]]
	elif l[0] == "quit":
		print(len(d)+1)
		break
	else:
		print(eval(d[l[0]][1], math.__dict__, {d[l[0]][0]: eval(l[1])}))
