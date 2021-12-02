#def foo(x, y):
   # if x < y:
     #   return x
   # else:
      #  return y
foo = lambda x, y: x if x < y else y
print(foo(9, 2))