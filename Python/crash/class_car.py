#Working with class and instances:

class Car():
    """A simple attempt to represent a car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #adding the new attribute inside the method

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def update_odometer(self, millage):
        """set odometer value to given value, reject the change if any roll the odometer back"""
        if millage >= self.odometer_reading:
            self.odometer_reading = millage
        else:
            print("You can't roll back on odometer")

    def increment_odometer(self, miles):
        """Add a given amount of odometer reading"""
        self.odometer_reading += miles

    def read_odometer(self):
        print("My car starts with " + str(self.odometer_reading) + ' in the millage.')

my_car = Car('a4', 'audi', 2016)
print(my_car.get_descriptive_name())
my_car.update_odometer(44)
my_car.increment_odometer(100)
my_car.read_odometer()
print("The car name is " + my_car.model)

#Modifying the attribute value directly (way 1)
#my_car.odometer_reading = 23
#my_car.read_odometer()

#Modifying the attribute through the method (way 2)
#my_car.update_odometer(44)
#to create a method for update_odometer

#Modifying the attribute Incrementing an attribute value through a method
#def increment_odometer(self, miles):
#    """Add a given amount of odometer reading"""
#    self.odometer_reading += miles
