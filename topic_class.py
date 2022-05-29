
class Person:

    def __init__(self, name) -> None:
        self.var_name = name
        self.age = 23

    def get_name(self):
        print("My name is, ", self.var_name)
        print("My age is, ", self.age)

obj1 = Person("Anil")

print(obj1.var_name)
