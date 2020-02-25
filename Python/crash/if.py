cars = ['bmw', 'audi', 'toyoto', 'swift', 'lambogini']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
#we can change the car value into lower and check it. #if car.lower() == 'bmw':
#this lower() won't change the value in original list so we can use the fuction to avoid errors.

#example for inequality
requested_topping = 'mushroom'
if requested_topping != 'anchovies':
    print("\nHold the anchovies! ")
