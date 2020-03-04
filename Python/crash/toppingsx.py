#enpty list

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + "in the order!")
else:
    print("Are you sure you want a plain pizza ?")

# in 5 python checks is there any value in by using for loop if there is no value then it executes else

#multiple list

availabe_toppings = ['onion', 'mushroom', 'pepperoni', 'corn', 'cheese']
requested_toppings = ['onion', 'pepperoni', 'ketch up']

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in availabe_toppings:
            print("Adding " + requested_topping + "in the order!")
        else:
            print("sorry we don't have " + requested_topping + "." )
