'''geometry.py'''
import math
print(" ")


class Polygon:
    '''class Polygon'''

    def get_sides(self):
        '''get_sides'''
        raise NotImplementedError

    def get_area(self):
        '''get_area'''
        raise NotImplementedError

    def get_perimeter(self):
        '''get_perimeter'''
        return sum(self.get_sides())


class Triangle(Polygon):
    '''class Triangle'''

    def __init__(self, side1, side2, side3):
        super().__init__()
        self.sides = [side1, side2, side3]

    def get_sides(self):
        '''get_sides'''
        return self.sides

    def get_area(self):
        '''get_area'''
        side1, side2, side3 = self.sides
        return get_triangle_area(side1, side2, side3)


class Rectangle(Polygon):
    '''class Rectangle'''

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_sides(self):
        '''get_sides'''
        return [self.width, self.height, self.width, self.height]

    def get_area(self):
        return get_rectangle_area(self.width, self.height)


class Square(Rectangle):
    '''class Square'''

    def __init__(self, side_length):
        super().__init__(side_length, side_length)


def get_triangle_area(side1, side2, side3):
    '''get_triangle_area'''
    semi_perimeter = (side1 + side2 + side3) / 2
    return math.sqrt(
        semi_perimeter *
        (semi_perimeter - side1) *
        (semi_perimeter - side2) *
        (semi_perimeter - side3)
    )


def get_rectangle_area(width, height):
    '''get_rectangle_area'''
    return width * height
