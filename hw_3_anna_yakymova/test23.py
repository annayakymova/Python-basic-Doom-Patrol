list_A = [2, 3, 4]
list_B = [5, 6, 7]
lst_num = list(map(lambda x, y: x ** y, list_A, list_B))
print(lst_num)