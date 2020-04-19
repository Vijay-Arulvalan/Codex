# try and except in json method

import json

#load the username if it has already stored
#if it is not there then promt the user

filename = 'user.json'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("Enter your name: ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We will remember you when you come back " + username + '!')
else:
    print("Welcome back " + username.title() + '!')
