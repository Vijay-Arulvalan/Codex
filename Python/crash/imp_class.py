#importing a class

from car_class import Car

my_car = Car('audi', 'a6', 2016)
print(my_car.get_descriptive_name())
my_car.odometer_reading = 23
my_car.read_odometer()

#storing multiple class in a module
#from class_elctric import ElectricCar

#Importing multiple class in a module
#from car import Car, ElectricCar

#importing an entire module
#import car

#“Importing All Classes from a Module”
#from module_name import *
