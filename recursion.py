def simple_forloop(x):
    print(x)
    if x == 10:
        return 10
    return simple_forloop(x + 1)

simple_forloop(0)
