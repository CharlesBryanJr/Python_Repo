'''inheritance.py'''
print(" ")


class Person:
    '''Person.py'''

    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def say_hello(self):
        '''say_hello'''
        print(f"Hi my name is {self.first_name} {self.last_name}")


class Employee(Person):
    '''Employee'''

    def __init__(self, first_name, last_name, salary) -> None:
        super().__init__(first_name, last_name)
        self.salary = salary

    def say_hello(self):
        '''say_hello'''
        super().say_hello()
        print(f"Your salary is {self.salary}")


class Manager(Employee):
    '''Manager'''

    def __init__(self, first_name, last_name, salary, deparment) -> None:
        super().__init__(first_name, last_name, salary)
        self.deparment = deparment

    def say_hello(self):
        '''say_hello'''
        super().say_hello()
        print(f"Your salary is {self.salary}")
        print(f"How is the {self.deparment} deparment?")


class Owner(Person):
    '''Owner'''

    def __init__(self, first_name, last_name) -> None:
        super().__init__(first_name, last_name)


p1 = Person("Charles", "Bryan")
p1.say_hello()
print(" ")

p2 = Employee("Charles", "Bryan", 70000)
p2.say_hello()
print(" ")

p3 = Manager("Charles", "Bryan", 70000, "Retail")
p3.say_hello()
print(" ")

p4 = Owner("Charles", "Bryan")
p4.say_hello()
print(" ")


print(type(p1))
print(isinstance(p1, Person))
print(isinstance(p1, Employee))
print(isinstance(p1, Manager))
print(isinstance(p1, Owner))
print(" ")
print(type(p2))
print(isinstance(p2, Person))
print(isinstance(p2, Employee))
print(isinstance(p2, Manager))
print(isinstance(p2, Owner))
print(" ")
print(type(p3))
print(isinstance(p3, Person))
print(isinstance(p3, Employee))
print(isinstance(p3, Manager))
print(isinstance(p3, Owner))
print(" ")
print(type(p4))
print(isinstance(p4, Person))
print(isinstance(p4, Employee))
print(isinstance(p4, Manager))
print(isinstance(p4, Owner))
print(" ")

print(" ")
