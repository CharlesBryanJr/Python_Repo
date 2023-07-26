print(' ')
# Tuples are immutabile lists

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(' ')
print(my_tuple[2])
print(' ')
print(my_tuple.count(5))
print(' ')
print(my_tuple.index(5))
print(' ')
print(len(my_tuple))
print(' ')

x, y, z, *other = (1, 2, 3, 4, 5)
print(x)
print(y)
print(z)
print(other)
print(' ')

user = {
    (1, 2): [1, 2, 3],
    'greet': 'Hello',
    'age': 20
}

print(user[(1, 2)])
print(' ')
