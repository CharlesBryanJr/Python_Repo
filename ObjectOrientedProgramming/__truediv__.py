'''__truediv__.py'''
print(" ")


class Line:
    '''Line'''

    def __init__(self, point1, point2) -> None:
        self.point1 = point1
        self.point2 = point2

    def __truediv__(self, factor):
        '''__truediv__'''
        new_point1 = (self.point1[0] / factor, self.point1[1] / factor)
        new_point2 = (self.point2[0] / factor, self.point2[1] / factor)
        return Line(new_point1, new_point2)


line1 = Line((10, 5), (20, 10))
line2 = line1 / 2
print(line2.point1, line2.point2)
print(" ")
