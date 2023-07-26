'''circle.py'''

class Circle:

    #Class Attributes
    pi = 3.14

    #Class Methods
    @classmethod
    def area(cls, radius):
        return cls.pi * (radius ** 2)
    
    @classmethod
    def perimeter(cls, radius):
        return 2 * cls.pi * radius
    
    @classmethod
    def get_area_and_perimeter(cls, radius):
        return (cls.area(radius), cls.perimeter(radius))
    
    #Constructor
    def __init__(self, radius) -> None:
        self.radius = radius


c1 = Circle(33)
print(Circle.get_area_and_perimeter(33))

print(" ")