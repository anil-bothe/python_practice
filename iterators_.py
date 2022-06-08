# # x = [1,3,5,25]

# class iter_by_ab:
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x

# res = iter_by_ab()

# x = res.__iter__()

# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())


"""
Generators - in python
"""
def range_by_anil(x):
    while x > 0:
        x -= 1
        yield x

x = list(range_by_anil(10))
print(x)
