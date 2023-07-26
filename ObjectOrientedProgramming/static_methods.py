'''static_methods.py'''
print(" ")

class Student:
    # Class Attributes / Static Attributes
    grade_bump = 2.0

    # Constructor
    def __init__(self, name, grades=[]) -> None:
        self.name = name
        self.grades = grades

    # Instance Methods
    def average(self):
        return sum(self.grades) / len(self.grades)
    
    # Class Methods
    @classmethod
    def average_from_grades_plus_bump(cls, grades):
        average = cls.average_from_grades(grades)
        return min(average + cls.grade_bump, 100)

    # Static Methods
    @staticmethod
    def average_from_grades(grades):
        return sum(grades) / len(grades)

s1 = Student("John", [80, 75, 65, 100])
s2 = Student("Jane", [60 , 50, 65, 60])

average = Student.average_from_grades(s1.grades[:2])
print(average)

average = Student.average_from_grades(s2.grades[:3])
print(average)

average = Student.average_from_grades(s2.grades[:3]+s1.grades)
print(average)

print(" ")