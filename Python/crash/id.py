id = {'first_name': 'mike', 'last_name': 'laurie', 'age': 25, 'city': 'mumbai'}
favourite_num = {'ken': 2, 'david': 7, 'peter': 3, 'sam': 23, 'lisa': 4}

print(id)
print(favourite_num)

for title, value in id.items():
    print('\n key: ' +title)
    print(' value: ' +str(value))
