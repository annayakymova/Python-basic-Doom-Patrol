x = {}
for num in range(10):
    if num ** 3 % 4 == 0:
        x[num] = num ** 3
    else:
        x[num] = num
print(x)