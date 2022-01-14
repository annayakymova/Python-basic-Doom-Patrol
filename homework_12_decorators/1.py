def double_result(func):
    def inner(a, b):
        return func(a, b) * 2
    return inner


def add(a, b):
    return a + b

@double_result
def add(a, b):
    return a + b

print(add(5, 5))