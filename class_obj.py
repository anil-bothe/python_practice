# Attributes OR Properties CRUD

"""
class A:
    name = "Anil"
    pass

obj = A()
obj.age = 23
obj.name = "Sunil"

print(obj.age)
print(obj.name)

del obj.name

print(obj.name)

"""

class A:
    name = "A"
    def __init__(self, ) -> None:
        print("init 1st class")
        self.secrete_value = 1234

    def myFunc1(self):
        print("my func1 exec") 

class B(A):
    def __init__(self, x) -> None:
        super().__init__()
        self.x = x

    def myFunc2(self):
        print("my func2 exec")

obj = B("anil")
print(obj.secrete_value)
