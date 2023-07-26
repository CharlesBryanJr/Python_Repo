'''abstract_animal.py'''
print(" ")

class Animal:

    def sleep(self):
        print("ZzzZzz")
    
    def animal_sound(self):
        raise NotImplementedError("animal_sound has not been implemented")
    
    def wake_up(self):
        self.animal_sound()
        print("I am awake!")

class Lion(Animal):

    def animal_sound(self):
        print("Roar!")