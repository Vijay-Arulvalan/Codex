filename = 'pi_million_digits'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input("Enter your birthday in the form of mmddyy: ")
if birthday in pi_string:
    print("Your birthday is present on the file")
else:
    print("Your birthday is not present on the file")
