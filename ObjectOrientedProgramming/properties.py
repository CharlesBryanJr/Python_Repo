'''properties.py'''
print(" ")


class Person:
    def __init__(self, name) -> None:
        self.name = name
        self._salary = 0

    @property
    def salary(self):
        return round(self._salary)

    @salary.setter
    def salary(self, salary):
        if salary < 0:
            raise ValueError("Error: invaild salary")

        self._salary = salary
    
    #salary = property(get_salary, set_salary)

p = Person("Tim")
p.salary = 100.3
print(p._salary)

print(" ")

class Time:
    def __init__(self, second) -> None:
        self._second = second

    @property
    def second(self):
        return self._second
    
    @second.setter
    def second(self, second):
        if second < 0 or second > 60:
            raise ValueError("Invalid second")

        self._second = second

t = Time(54)
t.second = 59
print(t.second)