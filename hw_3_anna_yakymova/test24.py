
import functools
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
foo = functools.reduce(lambda x,y: x+y, lst_to_sort)
print(foo)
