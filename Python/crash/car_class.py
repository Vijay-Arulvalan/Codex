# importing class

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
