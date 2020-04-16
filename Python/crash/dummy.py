dummy = ('Enter your age: ')
age = ""

while age >= 60:
    age =input(dummy)
    age = str(dummy)

    if age > 60:
        break
    elif age <= 12:
        price = 10
    else:
        price = 15

    print('Your ticket cost is $' + str(price) + '.')
