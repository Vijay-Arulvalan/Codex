class Dog():
    """A Simple attempt to model a dog"""
    def __init__(self, name, age): # the function that is part of the class is Method.
        #“The self parameter is required in the method definition, and it must come first before the other parameters”
        """Initialize the name and age attribute""" #The init method is special the python runns automatically.
        self.name = name #“Any variable prefixed with self is available to every method in the class”
        self.age = age

    def sit(self):
        """Simulate the dog sitting in a command"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate the dog to roll over in a command"""
        print(self.name.title() + " is now rolling over!")

my_dog = Dog('willy', 6) #we store the instances in the variable my_dog
print("My dog name is " + my_dog.name.title() + '.') #accessing attributes
print('My dog age is ' + str(my_dog.age) + '.')

#Calling function inside the class
my_dog.sit()
my_dog.roll_over()

#Multiple instances
my_another_dog = Dog('scooby', 6)
print("\nMy another dog name is " + my_another_dog.name.title() + '.') #accessing attributes
print('My another dog age is ' + str(my_another_dog.age) + '.')
my_another_dog.sit()
my_another_dog.roll_over()
