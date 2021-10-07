from math import *
def calc(s, t ,u):
	a = lambda x: eval(s)
	b = lambda x: eval(t)
	c = lambda x, y: eval(u)
	def fun(x):
		return(c(a(x), b(x)))
	return fun
	
	
	
F = calc("sin(x)**2", "cos(x)**2", "x+y")
print(F(123))
