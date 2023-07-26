'''__eq__.py'''
import math
print(" ")

class Line:

    def __init__(self, point1, point2) -> None:
        self.point1 = point1
        self.point2 = point2

    def __truediv__(self, factor):
        new_point1 = (self.point1[0] / factor, self.point1[1] / factor)
        new_point2 = (self.point2[0] / factor, self.point2[1] / factor)
        return Line(new_point1, new_point2)
    
    def __floordiv__(self, factor):
        new_point11 = (self.point1[0] // factor, self.point1[1] // factor)
        new_point22 = (self.point2[0] // factor, self.point2[1] // factor)
        return Line(new_point11, new_point22)
    
    def __len__(self):
        distance_x = (self.point1[0] - self.point2[0]) ** 2
        distance_y = (self.point1[1] - self.point2[1]) ** 2
        distance = math.sqrt(distance_x + distance_y)
        return round(distance)
    
    def __eq__(self, other):
        if not isinstance(other, Line):
            return False
        
        is_point1_equal = self.point1 == other.point1
        is_point2_equal = self.point2 == other.point2

        return is_point1_equal and is_point2_equal
    

line1 = Line((10, 5), (20, 10))
line2 = line1 / 2
print(line2.point1, line2.point2)
print(" ")

line3 = Line((10, 5), (20, 10))
line4 = line1 // 2
print(line4.point1, line4.point2)
print(" ")

line5 = Line((10, 5), (20, 10))
print(len(line5))
print(" ")

line6 = Line((10, 5), (20, 10))
line7 = Line((10, 5), (20, 10))
line8 = Line((100, 50), (200, 100))
print(line6 == 3)
print(line6 == line7)
print(line8 == line7)
print(" ")