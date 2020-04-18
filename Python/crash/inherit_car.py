# Inheritance

class Car(): #Parent class
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

class Electric(Car): #child class
    """To Initialize attributeof the parrent class"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        #call the __init__() method from ElectricCar’s parent class, which gives an ElectricCar instance all the attributes of its parent class
        # super() is a special function that helps python to make a connection between parent and child class.
        self.battery_size = 70
#defining attributes and methods to child class
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + '-kwh batter')
#overriding method from the parent class
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank")
my_car = Electric('tesla', 'model', 2016)
print(my_car.get_descriptive_name())
my_car.describe_battery()
