# Attributes OR Properties CRUD

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
