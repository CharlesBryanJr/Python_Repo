'''Function_Closures.py'''
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
print(" ")

def outer(x):
    def inner(y):
        def inner2(z):
            print(x + y + z)
        
        return inner2

    return inner

outer(10)(10)(10)
print(" ")

def collection():
    lst = []

    def inner(value):
        lst.append(value)
        return lst
    
    return inner

class Collection():
    def __init__(self, value) -> None:
        self.lst = []

    def add_value(self, value):
        self.lst.append(value)
        return self.lst

add_value = collection()
print(collection())
print(collection())
print(collection())
print(add_value(1))
print(add_value(2))
print(add_value(3))
print(" ")

def counter(start):
    count = start
    
    def increment(value):
        nonlocal count
        count += value
        return count
    
    return increment

count = counter(2)
print(count(1))

print(" ")
