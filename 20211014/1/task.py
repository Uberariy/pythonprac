from fractions import *
def Counter(*l):
	s = Fraction(l[0])
	w = Fraction(l[1])
	adeg = int(l[2])
	acoef = []
	for i in range(3,4+adeg):
		acoef += [Fraction(l[i])]
	bdeg = int(l[4+adeg])
	bcoef = []
	for i in range(5+adeg,6+adeg+bdeg):
		bcoef += [Fraction(l[i])]

	#print([s, w], "\n", [adeg, bdeg], "\n", acoef, "\n", bcoef)
	for i in range(adeg+1):
		acoef[i] = acoef[i]*(s)**(adeg-i)
	#print(bdeg, len(bcoef))
	for i in range(bdeg+1):
		bcoef[i] = bcoef[i]*(s)**(bdeg-i)

	if sum(bcoef) == 0:
		return False
	return sum(acoef)/sum(bcoef) == w
	
#ssstr = input()
#l = ssstr.split(",")
#print(fun(l))
import sys
exec(sys.stdin.read())
