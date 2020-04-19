import json

username = input("What's your name: ")
filename = 'user.json'

with open(filename, 'w') as file_object:
    json.dump(username, file_object)
    print('We will remember you when you come back again ' + username +'.')
