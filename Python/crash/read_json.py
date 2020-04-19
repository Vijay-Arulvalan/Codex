import json

filename = 'numbers.json'

with open(filename) as file_object:
    numbers = json.load(file_object) #load the information stored in the file and stored it in the variable numbers.

print(numbers)
