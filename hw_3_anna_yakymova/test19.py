def foo(x, y, z):
    if x < y and x > z:
        return z
    else:
        return y
print(foo(9, 1, 3))