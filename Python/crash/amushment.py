age = 17

if age <= 4:
    print("Your admission cost is free!")
elif age <18:
    print("your admission cost is $5. ")
else:
    print("your admission cost is $10.")

#Another methods

age = 17

if age <=4:
    price = 0
elif age <18:
    price = 5
else:
    price = 10

print("Your admission price is $" + str(price) + ".")
