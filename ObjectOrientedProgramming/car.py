'''Car.py'''
print(" ")


class Car:
    '''Car'''

    #Class Attributes
    number_of_cars = 0
    wheels = 4

    #Class Methods
    @classmethod
    def update_number_of_cars(cls, cars):
        cls.number_of_cars = cars

    #Constructor
    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model
        Car.number_of_cars += 1

print(Car.number_of_cars)
print(" ")

c1 = Car("BMW", "3 Series")
c2 = Car("Mercedes Benz", "C Class")
print(c1.number_of_cars)
print(c2.number_of_cars)
print(Car.number_of_cars)
print(" ")

Car.update_number_of_cars(13)
print(c1.number_of_cars)
print(c2.number_of_cars)
print(Car.number_of_cars)


print(" ")
