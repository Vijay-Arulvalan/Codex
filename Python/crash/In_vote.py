name = input("Name: ")
age = input("Age: ")

age = int(age)

if age >= 18:
    print("Hello " + name.title() +", You are eligible to vote!")
else:
    print("Sorry " + name.title() + ", You are not eligible to vote!")
