def par(typ):
	def dump(fn):
		def fu(*args):
			if any(type(a) is not typ for a in args):
				raise TypeError
			return fn(*args)
		return fu	
	return dump
		
@par(str)
def fun(a, b):
	return a*2+b
	
print(fun("as", "ds"))
print(fun(2, 1))
