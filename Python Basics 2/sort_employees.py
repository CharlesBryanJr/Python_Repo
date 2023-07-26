'''sort_employees'''
print(" ")


def sort_by_name(employees):
    '''sort_by_name'''
    return employees[0]


def sort_by_age(employees):
    '''sort_by_age'''
    return employees[1]


def sort_by_salary(employees):
    '''sort_by_salary'''
    return employees[2]


def sort_employees(employees, sort_by):
    '''sort_employees'''

    if sort_by == "name":
        employees.sort(key=sort_by_name)

    if sort_by == "age":
        employees.sort(key=sort_by_age)

    if sort_by == "salary":
        employees.sort(key=sort_by_salary)

    print(employees)


E = [
    ["John", 33, 65000],
    ["Sarah", 24, 75000],
    ["Josie", 29, 100000],
    ["Jason", 26, 55000],
    ["Connor", 25, 110000]
]

sort_employees(E, "age")
print(" ")
sort_employees(E, "salary")
print(" ")
sort_employees(E, "name")
print(" ")


# Copyright © 2022 AlgoExpert LLC. All rights reserved.

def sort_employees1(employees, sort_by):
    sort_indices = ["name", "age", "salary"]
    sort_index = sort_indices.index(sort_by)

    sorted_employees = []
    # Copy the employees list so we don't modify it
    employees_copy = employees[:]

    while len(employees_copy) > 0:
        smallest_employee_index = 0

        for i, employee in enumerate(employees_copy):
            current_smallest_value = employees_copy[smallest_employee_index][sort_index]
            if employee[sort_index] < current_smallest_value:
                smallest_employee_index = i

        # After looking through all remaining employees we will have found the employee
        # with the smallest sort_by value so we add it to the sorted list
        next_sorted_employee = employees_copy[smallest_employee_index]
        sorted_employees.append(next_sorted_employee)
        employees_copy.pop(smallest_employee_index)

    return sorted_employees


def sort_employees3(employees, sort_by):
    sort_indices = ["name", "age", "salary"]
    sort_index = sort_indices.index(sort_by)

    sorted_employees = sorted(employees, key=lambda x: x[sort_index])

    return sorted_employees