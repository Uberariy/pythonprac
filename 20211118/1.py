def dumpc(cls):
	class declass(cls):
		count = 0
		def __init__(self, *args, **kwargs):
			res = super().__init__(*args, **kwargs)
			self.count += 1
			return f">{res}<"
	
		if "__del__" in locals():
			def __del__(self, *args):
				res = super().__del__(*args)
				self.count -= 1
				return f">{res}<"
	return declass
	
@dumpc
class A(str):
	pass
	
a = A("sds")
print(a)
