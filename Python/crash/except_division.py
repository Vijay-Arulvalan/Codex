#python try this code if there is an error then it go to except

print("Give me two numbers and i'll divide it for you! ")
print("Enter 'q' to 'quit': ")

while True:
    first_number = input('\n First Number: ')
    if first_number == 'q':
        break
    second_number = input('\n Second Number: ')
    if second_number == 'q':
        break

    try:
        answer = int(first_number)/ int(second_number)

    except ZeroDivisionError:
        print("You can't divide any number by zero! ")
    else:
        print(answer)
