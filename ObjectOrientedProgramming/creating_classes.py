'''creating_classes.py'''
print(" ")


class Person:
    '''Person'''

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


p1 = Person("John Doe", 25)
print(p1.name)
print(p1.age)

p2 = Person("Jane Doe", 20)
print(p2.name)
print(p2.age)

print(" ")
