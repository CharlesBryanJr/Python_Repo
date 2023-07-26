'''map_filter.py'''
# pylint: disable=E1101
import math
print(" ")

lst = [1, 2, 3, 4, 5, 6, 7]

new_lst = list(map(lambda x: x ** 2, lst))
print(new_lst)
print(" ")
for num in new_lst:
    print(num)

print("-----")
lst = [[1, 2, 3], [4, 5], [6, 7], [1, 2], [10, 0]]
new_lst = list(map(lambda x: sum(x), lst))
print(new_lst)
print(" ")
for num in new_lst:
    print(num)

print("-----")
new_lst = list(filter(lambda x: sum(x) > 6, lst))
print(new_lst)
print(" ")
for num in new_lst:
    print(num)

print("-----")
print("-----")


new_lst = filter(lambda y: y % 2 == 0, map(lambda x: sum(x), lst))
print(list(new_lst))
print(" ")
for num in new_lst:
    print(num)
print(" ")
