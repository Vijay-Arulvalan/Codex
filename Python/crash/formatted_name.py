def get_formatted_name(first_name, last_name):
    """Display the name of the person"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
#“When you call a function that returns a value, you need to provide a variable where the return value can be stored. In this case, the returned value is stored in the variable musician”

musician = get_formatted_name('vijay', 'arulvalan')
print(musician)

#######

def get_full_name(first_name, last_name,  middle_name=''): #to make a middle_name optional
    """Display the full name of the person"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
        return full_name.title()
    else:
        full_name = first_name + ' ' + last_name
        return full_name.title()

person = get_full_name('vijay', 'arulvalan')
print(person)
