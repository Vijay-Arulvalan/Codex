import json

filename = 'user.json'

with open(filename) as file_object:
    username = json.load(file_object)
    print("Welcome back " + username.title() + ".")
