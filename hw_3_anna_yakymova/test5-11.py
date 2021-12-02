#5
print("Anna has {} apples and {} peaches.".format(23, 8))
#6
print("Anna has {0} apples and {1} peaches.".format("twenty three", "eight"))
#7
print("Anna has {0} apples and {fv} peaches.".format("twenty tree", fv="eight"))
#8
print("Anna has {0:4} apples and {1:3} peaches.".format("seven", "six"))
#9
numereal_1 = "twenty three"
numereal_2 = "eight"
print(f"Anna has {numereal_1} apples and {numereal_2} peaches.")
#10
apples = "twenty three"
peaches = "eight"
print('Anna has %s apples and %s peaches.' % (apples, peaches))
#11
appls = "twenty three"
pchs = "eight"
data_dict = {"apples": appls, "peaches": pchs}
print('Anna has  %(apples)s apples and %(peaches)s peaches.' % data_dict)


