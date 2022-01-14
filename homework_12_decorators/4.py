def type_check(correct_type):
    def type_decorator(func):
        def wrapper(*args):
            if type(*args) == correct_type:
                return func(*args)
            else:
                return f"Wrong Type: {type(*args)}"

        return wrapper

    return type_decorator


@type_check(int)
def times2(num):
    return num * 2



print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]



print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))