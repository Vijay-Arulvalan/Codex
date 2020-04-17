def greet_user():
    """Display a simple greeting!"""
    name = input("Name: ")
    print('\nHello, ' + name.title())

greet_user()

#another program method:

def greet(username):
    """Display a simple greeting!"""
    print("\n Hello, " + username.title())

greet('vijay')
