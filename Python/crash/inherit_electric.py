#instances as attributes

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

class Battery():
    def __init__(self, battery_size=85):
        """Initialize the battery's attribute"""
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def get_range(self):
        if self.battery_size >= 70:
            range = 270
        elif self.battery_size >= 85:
            range = 300
        message = "This car can go approximately " + str(range)
        message += "  Miles on full charge"
        print(message)

class ElectricCar(Car):
    def __init__(self, make, model, year):
        """Initialize attribute of a parrent class"""
        super().__init__(make, model, year)
        self.battery = Battery()
        #This line tells Python to create a new instance of Battery (with a default size of 70, because we’re not specifying a value) and store that instance in the attribute self.battery.

my_tesla = ElectricCar('tesla','model', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
