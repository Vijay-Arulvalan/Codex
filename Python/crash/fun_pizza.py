def make_pizza(*toppings): #the * tells python to make a empty tuple called toppings and pack whatever
#value it receives into the tuple
    """To print the list of toppings added with pizza"""

    print('Making a pizza with following toppings: ')
    for topping in toppings:
        print('- ' + topping)


make_pizza('pepperonni')
make_pizza('cheese', 'green pepper', 'mushroom')

print("\n **************************")

def pizza(size, *toppins):
    """To input two parameter in the above function"""
    print("Making a " + str(size) + "-inch of pizza with the following toppings")
    for toppin in toppins:
        print('- '+ toppin)

pizza(12, 'pepperonni')
pizza(16,'cheese', 'green pepper', 'mushroom')
