#1
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)
#2
lst_c = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst_c)