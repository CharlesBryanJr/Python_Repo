'''__len__.py'''
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