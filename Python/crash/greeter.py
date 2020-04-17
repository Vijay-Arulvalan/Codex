def greet_user():
    """Display a simple greeting!"""
    name = input("Name: ")
    print('\nHello, ' + name.title())

greet_user()

#the above one ask a input from the user after running the program
#another program method:

def greet(username): #username is a parameter
    """Display a simple greeting!"""
    print("\n Hello, " + username.title())

greet('vijay') #vijay is a argument
