from math import *
def calc(s, t ,u):
	a = lambda x: eval(s)
	b = lambda x: eval(t)
	c = lambda x, y: eval(u)
	return lambda x,y: c(a, b)
	
	
	
F = calc("sin(x)**2", "cos(x)**2", "x+y")
print(123)
