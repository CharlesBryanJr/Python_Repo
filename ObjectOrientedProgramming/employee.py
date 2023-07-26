'''employee.py'''
print(" ")

class Employee:
    
    # Class Attributes
    number_of_employees = 0
    average_age = 0
    average_salary = 0

    # Class Methods
    @classmethod
    def update_average_age(cls, age):
        total_age = cls.average_age * (cls.number_of_employees - 1) 
        cls.average_age = (total_age + age) / cls.number_of_employees
    
    @classmethod
    def update_average_salary(cls, salary):
        total_salary = cls.average_salary * (cls.number_of_employees - 1)
        cls.average_salary = (total_salary + salary) / cls.number_of_employees

    # Constructor
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary
        Employee.number_of_employees += 1
        Employee.update_average_age(age)
        Employee.update_average_salary(salary)

e1 = Employee("Charles", 25, 70000)
print(Employee.number_of_employees)
print(Employee.average_age)
print(Employee.average_salary)
print(" ")

e2 = Employee("Morgan", 32, 120000)
print(Employee.number_of_employees)
print(Employee.average_age)
print(Employee.average_salary)


print(" ")

