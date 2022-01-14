def only_odd_parameters(func):
    def inner(*args):
        for i in args:
            if i % 2 != 0:
                return func(*args)
            # if args passed to func are not odd - return "Please use only odd numbers!"
            else:
                return 'Please use only odd numbers!'

    return inner


@only_odd_parameters
def add_(a, b):
    return a + b



print(add_(5, 5))





@only_odd_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e



print(multiply(9, 8, 7, 5, 3))
print(multiply(1, 4, 7, 8, 9))
