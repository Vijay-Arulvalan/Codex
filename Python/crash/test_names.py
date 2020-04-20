import name_function

print("Enter 'q' to exit anytime: ")

while True:
    first = input("Enter the first name: ")
    if first == 'q':
        break
    last = input("Enter the last name: ")
    if last == 'q':
        break

    name = formatted_name(first, last)
    print("Your neatly formatted name is: " + name + '.')
