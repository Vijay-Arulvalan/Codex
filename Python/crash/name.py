name = 'vijay arulvalan'
print(name.title()) # title() is to make name first letter to uppercase

name = 'Vijay Arulvalan'
print(name.upper())
print(name.lower())

first_name = 'Vijay'
last_name = 'Arulvalan'
full_name = first_name+' '+last_name

print(full_name)
print("Hello, " + full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message)

print("Languages: \n\tC \n\tPython \n\tC++ \n\tSwift")

favorite_languages = 'Python ' # ' Python'
print('\n\tmy favorite is '+ favorite_languages.rstrip()) #rstrip() removes extra space in line 20 'Python '
#rstrip() = Right strip
#lstrip() = Left strip

favorite_languages = favorite_languages.rstrip()
#to remove the extra space and permanently change that.
