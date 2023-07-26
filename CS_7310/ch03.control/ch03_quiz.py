# pylint: disable=C0114
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
print(' ')

# The keyword "yield" is a Python keyword used in generator functions to produce a value to the caller while maintaining the function's state.

x = 10
x += 9
print(x)
x = 10
x **= 3
print(x)
x = 10
x //= 3
print(x)
print(range(10,0,-2))

for i in range(10):
    if i == 5:
       break
    else:
       print (i)

for i in range(10):
    if i == 5:
        continue
    else:
        print (i)

for character in 'Programming':
    print(character, end=' ')