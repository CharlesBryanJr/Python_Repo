# fig05_01.py
"""Displaying a bar chart"""
numbers = [19, 3, 15, 7, 11]

print('\nCreating a bar chart from numbers:')
print(f'Index{"Value":>8}   Bar')

for index, value in enumerate(numbers):
    print(f'{index:>5}{value:>8}   {"*" * value}')


print(" ")

a = [1,2,3,-1,-2,0]
b = a[::-1]
print(b)
print(reversed(a))
print(enumerate(a))
print(zip(a,b))
a.sort()
a.reverse()
print(a)

c = 'charles'
print(c.upper())

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
arr = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, numbers)))
print(arr)

print([x ** 2 for x in filter(lambda x: x % 2 != 0, numbers)])

for x in (map(lambda x: x ** 2, filter(lambda x: x != 0, numbers))):
    print(x)

t1 = [1, 2, 3]
t1 += (4, 5)
print(t1)
a = [9, (12,13) , [6,7,8], 10]
b = a[:]
print(id(a))
print(id(b))

s = 'zxab'
s = sorted(s)
print(s)
print([x + 1 for x in range(1,5) if x % 2 == 0])
data = [1,2,3,4,5,6,7,8,9]
print(list(filter(lambda y: y % 3 != 0, data)))
a = ['foo', 'bar']
b = [11, 66]
print(list(zip (a, b)))

a = [[77, 68, 86, 73], [96, 87, 89, 81], [70, 90, 86, 81]]
for row in a:
    for item in row:
        print(item, end=' ')
