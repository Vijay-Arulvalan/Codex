responses = {}

polling_active = True #flag as True

while polling_active:
    name = input('\nWhat is your name? ')
    response = input('Which mountain would you like to claim someday? ')
#Store the response in the dictionary
    responses[name] = response
#find if anyone is taking the poll
    repeat = input("Would you like to let another person respond? (yes/ no)")
    if repeat == 'no':
        polling_active = False

    print('\n ....Poll Results....')
    for name, response in responses.items():
        print(name + ' Would like to climb ' + response + ".")
