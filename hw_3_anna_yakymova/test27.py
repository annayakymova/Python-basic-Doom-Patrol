#1 version ( with set)
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
old_list = list_1 + list_2
unique_numbers = list(set(old_list))
print(unique_numbers)
#2 version
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
numbers_u = list(filter(lambda x: x in list_2, list_1))
print(numbers_u)
