def is_even(x: int) -> bool:
    """
    this func checks wheather x is even or odd
    :return bool
    """
    return x % 2 == 0


# print(is_even(34))

# is_even = lambda x: x % 2 == 0
# result = is_even(34)
# print(result)


res = map(lambda x: x ** 2, [2,5,6,23,6,3])
# print(list(res))

res = map(lambda x: int(x) **2, ["23"])
# print(list(res))

def myFunc(x: str) -> int:
    return int(x) ** 3

res = map(myFunc, ["2", "1", "4"])
# print("output: ", list(res))


# def myFunc(x, y, *args):
#     print(args)
#     return [x, y]

# res = myFunc("anil", "b", 23,23,12,3,234,23,23,23,4,23)


def myFunc(first_element, *args, **kwargs):
    print(first_element)
    print(args)
    print(kwargs)

res = myFunc( first_element=234)
# print(res)

