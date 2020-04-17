def build_person(first_name, last_name, age = ' '): #age is optional
    """Return a dictionary of information about the person"""
    person = {'first': first_name.title(), 'last': last_name.title(), 'age': int(age)}
    return person
    if age:
        person['age'] = age
        return person

test = build_person('vijay', 'arulvalan', 24)
print(test)
