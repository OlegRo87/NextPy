import functools


def add(x, y):
    return x + y


shopping_list = [200, 120, 330, 50]
print(functools.reduce(add, shopping_list, 15))


def f(a, b):
    if a < b:
        return a
    else:
        return b


print(functools.reduce(f, [47, 11, 42, 102, 13]))
