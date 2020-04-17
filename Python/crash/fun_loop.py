def get_formatted_name(first_name, last_name):
    """Return a full name formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

    #This is a infinite loop
    while True:
        print("\nTell your full name")
        f_name = input("First name: ")
        l_name = input("Last name: ")

        formatted_name = get_formatted_name(f_name, l_name)
        print("Hello, " + formatted_name + '!')
