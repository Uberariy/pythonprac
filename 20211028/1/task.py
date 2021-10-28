def genfib(m, n):
	a = 1
	b = 0
	for i in range(0, n+1):
		if i >= m:
			yield a
		b, a = a, a+b

g = genfib(2, 4)
print(list(g))