def describe_pets(animal_type, pet_name): # describe_pets(pet_name, animal_type = 'dog')
#we can describe one parameter when we declare the function on above code.
    """Display the information of the pets"""
    print("I've animal type " + animal_type + " and the name of that is " +
            pet_name.title() )

describe_pets('dog', 'scoobie') # for one function calls
describe_pets('cat', 'tom') #for multiple function calls
describe_pets('rat', 'jerry')
# we can specify the keyword argument like following below:

describe_pets(pet_name = 'alexandria', animal_type = 'horse')
#if the function calls change also there no displacement of result like the first one to second
