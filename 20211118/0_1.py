class Num:
	val = 0
	def __get__(self, obj, cls):
		print("get")
		return self.val
	def __set__(self, obj, value):
		try:
			self.val = value.real
		except Exception:
			self.val = len(value)
		print("set", obj, value, self.val)
		return
	def __delete__(self, obj):
		print("del")
		
class C:
        num = Num()

print(C().num)
c, d = C(), C()
c.num = d.num = 2
print(c.num+d.num)
c.num = "qwerqwerqwer"
print(c.num+d.num)
d.num = range(10, 1000, 7)
print(c.num+d.num)
