dictonary = {
    'a': [1, 2, 3],
    'b': "Hello World",
    'c': ["python", "C++", 4.7, False],
    'x': True,
}

mylist = [
    {
        'a': [1, 2, 3],
        'b': "Hello World",
        'c': ["python", "C++", 4.7, False],
        'x': True,
    },
    {
        0: [1, 2, 3],
        1: "Hello World",
        'aa': ["python", "C++", 4.7, False],
        'True': True,
    }
]

print(' ')
print(dictonary)
print(' ')
print(dictonary['c'][0])
print(' ')
print(mylist)
print(' ')


# Dictionary Keys must be unique


# Dictionary Methods
print(dictonary.get('age', 25))
print(' ')
print('x' in dictonary)
print(' ')
print('x' in mylist)
print(' ')
print('python' in dictonary.keys())
print(' ')
print('python' in dictonary.values())
print(' ')
print(dictonary.items())
print(' ')
print(dictonary.update({'x': False}))
print(' ')
print(dictonary.pop('b'))
print(' ')
print(dictonary)
print(' ')
