age = input('Enter your age: ')
age = int(age)

if age <= 3:
    price = 0
elif age <= 12:
    price = 10
else:
    price = 15

print('Your ticket cost is $' + str(price) + '.')
