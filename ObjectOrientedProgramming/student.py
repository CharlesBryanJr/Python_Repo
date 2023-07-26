'''Student.py'''
print(" ")


class Student:
    '''Student'''
    all_students = []

    def __init__(self, name, grade):
        self.name = name
        self._grade = grade
        Student.all_students.append(self)

    @property
    def grade(self):
        '''grade'''
        return self._grade

    @grade.setter
    def grade(self, new_grade):
        '''grade'''
        if new_grade < 0 or new_grade > 100:
            raise ValueError("New grade not in the accepted range of [0-100].")
        self._grade = new_grade

    @classmethod
    def get_best_student(cls):
        '''get_best_student'''
        best_student = None
        for student in cls.all_students:
            if best_student is None or student.grade > best_student.grade:
                best_student = student
        return best_student

    @classmethod
    def get_average_grade(cls):
        '''get_average_grade'''
        return cls.calculate_average_grade(cls.all_students)

    @staticmethod
    def calculate_average_grade(students):
        '''calculate_average_grade'''
        if len(students) == 0:
            return -1

        total = 0
        for student in students:
            total += student.grade
        return total / len(students)
