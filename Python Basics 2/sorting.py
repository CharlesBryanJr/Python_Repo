'''sorting'''
print(" ")

lst = [2, 1, 3, 4, 2, 3, 2, 1]
print(sorted(lst))
print(sorted(lst, reverse=True))
print(tuple(sorted(lst)))
print(tuple(sorted(lst, reverse=True)))
print(lst)
print(" ")


lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
print(" ")


def sort_second_index(item):
    '''Returns the second element'''
    return item[1]


def sum_item(item):
    '''sums the item'''
    return sum(item)


lst1 = [[1, -2], [3, -4], [11, -99], [7, -8], [1, -2], [5, 0]]
lst2 = sorted(lst1, key=sum_item)
print(lst2)
print(" ")

print(" ")
print(lst1)
lst1.sort()
print(lst1)
lst1.sort(key=sort_second_index)
print(lst1)
print(" ")

people = {"Tim": 21, "Joe": 18, "Sarah": 25, "Jennie": 26, "Bill": 34}

result = sorted(people, key=people.get)
print(result)
print(" ")
