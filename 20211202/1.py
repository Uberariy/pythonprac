class dump(type):

    def __call__(self, *args, **kwargs):
        print("call", self, args, kwargs)
        return super().__call__(*args, **kwargs)

  #  def __new__(cls, name, parents, ns):
   #     print("new", cls, name, parents, ns)
    #    return super().__new__(cls, name, parents, ns)

    def __init__(self, name, parents, ns):
        print("__init__", self, parents, ns)
        for i in ns:
			def
        return super().__init__(name, parents, ns)

class C(metaclass=dump):
    def __init__(self, val):
        self.val = val

    def add(self, other, another=None):
        return self.val + other + (another or self.val)

c = C(10)
print(c.add(9))
print(c.add(9,another=10))
