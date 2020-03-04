requested_toppings= ['cheese', 'mushroom', 'onions']

if 'mushroom' in requested_toppings:
    print("Add mushroom in the order")
if 'onions' in requested_toppings:
    print("Add extra onion on order")
if 'cheese' in requested_toppings:
    print("Add extra cheese in the order")
if 'pepperoni' in requested_toppings:
    print("Add extra pepperoni\n")
if 'ketch up' not in requested_toppings:
    print("Ketch up, Its complimentry add on")

#This code won't work in if elif else statement ...it will execute once and it prints ...
#another method using for

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + " in the order!")

#if inside the for

print('\n')
for requested_topping in requested_toppings:
    if requested_topping == 'mushroom':
        print('Sorry, We are run out of mushroom')
    else:
        print("Adding " + requested_topping + 'in the order')
