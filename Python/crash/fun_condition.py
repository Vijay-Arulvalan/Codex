def get_formatted_name(first_name, last_name):
    """Return a full name with good formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

    while True:
        print("Enter your full name: ")
        print("(Enter 'q' to quit at any time)")
        f_name = input("First name: ")
        if f_name == 'q':
            break
        l_name = input("Last name: ")
        if l_name == 'q':
            break

        name = get_formatted_name(f_name, l_name)
        print("Hello, " + name + '!')
