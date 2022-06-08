class Person:
    name = "ANIL"
    age = 26

    @classmethod
    def get_name(self):
        return self.name

    @property # we can call this method without paranthisis
    def get_age(self):
        return self.age

    @staticmethod
    def calc(a, b):
        return a + b

# classmethod
result = Person.get_name()
print(result)

# property
print(Person().get_age)

# staticmethod
obj = Person()
res = obj.calc(23, 7)
print(res)

print(Person.calc(14, 6))
