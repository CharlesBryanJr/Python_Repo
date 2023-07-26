class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def change_postion(self, x, y):
        self.x = x
        self.y = y

    def get_postion(self):
        return (self.x, self.y)

    def get_area(self):
        return self.x * self.y