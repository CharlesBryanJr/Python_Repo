'''methods.py'''
print(" ")


class Person:
    '''Person'''

    def __init__(self, name) -> None:
        self.name = name
        self.age = None
        self.weight = None
        self.height = None

    def say_hello(self):
        '''say_hello'''
        print(f"Hello, {self.name}")

    def set_age(self, age):
        '''set_age'''
        self.age = age


p1 = Person("Charles")
p1.say_hello()
p1.set_age(25)
print(p1.age)
print(" ")


class Counter:
    '''Counter'''

    def __init__(self) -> None:
        self.count = 0
        self.locked = False

    def increment(self):
        '''increment'''
        if self.locked:
            raise Exception("The counter is locked!")
        self.count += 1

    def decrement(self):
        '''decrement'''
        if self.locked:
            raise Exception("The counter is locked!")
        self.count -= 1

    def print_count(self):
        '''print_count'''
        print(f"The current count is {self.count}")
    
    def toggle_counter_lock(self):
        '''toggle_counter_lock'''
        self.locked = not self.locked


counter = Counter()
counter.increment()
counter.increment()
counter.decrement()
counter.print_count()
counter.increment()
counter.increment()
counter.print_count()

counter.toggle_counter_lock()
counter.decrement()

print(" ")
