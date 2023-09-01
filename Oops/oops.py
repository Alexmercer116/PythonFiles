'''class Car :
    pass #EmptyClass

ford = Car()
honda = Car()

ford.speed = 200
honda.speed = 220
'''

# __init__ method and self keyword
'''
self acts as an object or it points to current object
class Auto_Mobile:
    def __init__(self,speed,color): 
        #__init__ Serves as Constructor of class.. but not a constructor
        # Initialisation.....The __init__method is called 
        # Not possible to Create multiple init methods in a class
        # If created the last init method overrides above init method
        # first whenever an instance is Created
        self.speed = speed
        self.color = color
        print('The Method is Called')
        print(speed)
        print(color)


ford = Auto_Mobile(200,'red') #Object Creation : ford is object 
# Attributes
ford.speed = 200
ford.color = 'Red'

print(ford.speed,ford.color)
print(ford.speed)'''

# Python encapsulation
import pyproj.Password
class Car :
    # def __init__(self,speed,color):
    speed = 100
    def set_speed(self,val):
        self.__speed = val
    def get_speed(self):
        return self.speed
    def add_speed(self,val):
        Car.__speed = self.get_speed()+val
        return Car.__speed
        # return self.get_speed()

# print(Rectangle.peri(10,12))

Password.password_generate()


suzuki = Car()
# suzuki.speed = 200
print(suzuki.add_speed(15))

