class check:
#	field: int = 42
	
	def __init__(self, *args, **kwargs) -> None:
		return super().__init__()
	
#	def string(self, level: int = 1) -> str:
#		return f"{'<'*level}{self.field}{'>'*level}"
	
	def check_annotations(self) -> bool:
		print(self.__annotations__)

class C(metaclass=check):
    A: int
    B: str = "QQ"

c = C()
print(c.check_annotations())
c.A = "ZZ"
print(c.check_annotations())
c.A = 100500
print(c.check_annotations())
c.B = type("Boo",(str,),{})(42)
print(c.check_annotations())
