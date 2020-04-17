#its a module i create for modules_pizza.py
def make_pizza(size, *toppings):
    """To input two parameter in the above function"""
    print("Making a " + str(size) + "-inch of pizza with the following toppings")
    for topping in toppings:
        print('- '+ topping)
