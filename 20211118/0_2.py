import string
class Alpha:
	__slots__ = [i for i in string.ascii_lowercase]
	
	def __str__(self):
		print(dir(self))
		for i in string.ascii_lowercase:
			print(i, ": ", self.i, ", ", end="")
			
	def __init__(self, **kwargs):
		for i, j in kwargs.items():
			self.i = j
			

alp = Alpha(c=10, z=2, a=42)
alp.e = 123
print(alp)
